import threading

from kamene.all import *
from kamene.layers.inet import IP, ICMP

ip_list = []
threads = []


def host_scan(ip):
    id_no = random.randint(3000, 65535)
    pkt = IP(dst=str(ip)) / ICMP(id=id_no, seq=1)
    # print(pkt.summary())
    result_raw = sr1(pkt, timeout=0.2, verbose=False)
    if result_raw is None:
        print(str(ip) + " offline")
    elif result_raw is not None:
        ip_list.append(str(ip))
        print(str(ip) + " online")


def mut_scan():
    while not q.empty():
        host_scan(q.get())


if __name__ == '__main__':
    net = '192.168.2.0/24'
    net = ipaddress.ip_network(net)
    q = queue.Queue()
    for i in net.hosts():
        q.put(i)
    for i in range(20):
        t = threading.Thread(target=mut_scan, args=())
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('Online Host:\n %s' % ip_list)
