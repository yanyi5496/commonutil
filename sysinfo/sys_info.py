import datetime

import psutil as ps
from dateutil.parser import parse


def boot_info():
    boot_time = ps.boot_time()
    boot_time_2human = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    boot_time_p = parse(boot_time_2human)
    now = parse(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    day = (now - boot_time_p).days
    seconds = (now - boot_time_p).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print(
        f"The device boot time is {boot_time_2human}, now time is {now}, run time: {day}:{h}:{m}:{s}")


def load_average():
    load = ps.getloadavg()
    print("Load Average： \n\t1Min：%s, 5Min：%s, 15Min：%s" % load)


def memory_issue():
    print("Memory Info：")
    mem = ps.virtual_memory()
    total = round(mem.total / 1024 / 1024, 2)  # round函数保留两位小数
    used = round(mem.used / 1024 / 1024, 2)
    percent = str(round(mem.used / mem.total * 100, 2)) + '%'
    print(f'\ttotal: {total}MB, used: {used}MB, used%: {percent}')


def disk_issue():
    print("Disk Info：")
    disk = ps.disk_partitions()
    for i in disk:
        if 'rw' in i.opts:
            disuse = ps.disk_usage(i.device)
            used = round(disuse.used / 1024 / 1024 / 1024, 2)
            total = round(disuse.total / 1024 / 1024 / 1024, 2)
            percent = str(round(used / total * 100, 2)) + '%'
            print(f'\t{i.device}: total: {total}, used: {used}, used%: {percent}')
        else:
            print(f'\t{i.device}: may unuseful')


def io_issue():
    print("Disk I/O Info：")
    counter = ps.disk_io_counters(perdisk=True)
    for i in counter.keys():
        io_counter = counter.get(i)
        io_r_count = io_counter.read_count
        io_w_count = io_counter.write_count
        io_r_bytes = '{0:.2f} MB'.format(io_counter.read_bytes / 1024 / 1024)
        io_w_bytes = '{0:.2f} MB'.format(io_counter.write_bytes / 1024 / 1024)
        print(f'\tread count: {io_r_count}\n'
              f'\tread bytes: {io_r_bytes}\n'
              f'\twrite count: {io_w_count}\n'
              f'\twrite bytes: {io_w_bytes}')


def cpu_issue():
    print("CPU Info：")
    cpu_logical_count = ps.cpu_count()
    cpu_physical_count = ps.cpu_count(logical=False)
    cpu_percent = ps.cpu_percent(interval=None, percpu=True)
    cpu_freq = ps.cpu_freq()
    cpu_user_times = round(ps.cpu_times().user, 2)
    print(f'\tcpu physical count: {cpu_physical_count} \n'
          f'\tcpu logical count: {cpu_logical_count} \n'
          f'\tcpu percent: {cpu_percent} \n'
          f'\tcpu freq: {cpu_freq} \n'
          f'\tcpu user times: {cpu_user_times}')


def net_issue():
    print('Net Info: ')
    net = ps.net_io_counters()
    bytes_sent = '{0:.2f} MB'.format(net.bytes_sent / 1024 / 1024)
    bytes_recv = '{0:.2f} MB'.format(net.bytes_recv / 1024 / 1024)
    print(f"\tnet_recv：{bytes_recv}, net_send: {bytes_sent}")


def main():
    boot_info()
    load_average()
    memory_issue()
    disk_issue()
    io_issue()
    cpu_issue()
    net_issue()


if __name__ == '__main__':
    main()
