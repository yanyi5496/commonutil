import queue
import socket
import threading

q = queue.Queue()
all_port = []


def port_scan(dest_ip: str):
    while not q.empty():
        dest_port = q.get()
        success = True
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((dest_ip, dest_port))
        except socket.error as msg:
            success = False
        s.close()
        if success:
            print("%s:%d\tsuccess to connect\t" % (dest_ip, dest_port))
            all_port.append(dest_port)
        else:
            print("%s:%d\tfail to connect\t" % (dest_ip, dest_port))


if __name__ == '__main__':
    threads = []
    for port in range(1, 65535):
        q.put(port)
    for i in range(50):  # 控制线程的数量
        t = threading.Thread(target=port_scan, args=('101.204.168.219',))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()  # 将线程加入到主线程中
    print(all_port)
