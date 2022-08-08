import queue
import socket
import threading
import time

q = queue.Queue()
all_port = []


def port_scan(dest_ip: str):
    while not q.empty():
        dest_port = q.get()
        success = True
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(2)
            s.connect((dest_ip, dest_port))
        except socket.error as msg:
            success = False
        finally:
            s.close()
        if success:
            print("%s:%d\tsuccess to connect\t" % (dest_ip, dest_port))
            all_port.append(dest_port)
        # else:
        #     print("%s:%d\tfail to connect\t" % (dest_ip, dest_port))


if __name__ == '__main__':
    start_time = time.strftime('%H:%M:%S', time.localtime())
    threads = []
    for port in range(1024, 10000):
        q.put(port)
    for i in range(500):
        t = threading.Thread(target=port_scan, args=('192.168.2.248',))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    end_time = time.strftime('%H:%M:%S', time.localtime())
    print('start time is %s, end time is %s' % (start_time, end_time))
    print(all_port)

