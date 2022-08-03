import queue
import threading

import nmap

open_ports = []
open_filter_ports = []
close_ports = []
unknown_ports = []
threads = []


def scap_udp(host, port):
    nm = nmap.PortScanner()
    arg = '-p ' + str(port) + ' -sU'
    x = nm.scan(hosts=host, arguments=arg)
    # print(x)
    # print(x.get('scan').get('192.168.2.248').keys())
    info = x.get('scan').get(host).get('udp').get(port)
    # print(info)
    state = info.get('state')
    reason = info.get('reason')
    if state == 'open|filtered':
        open_filter_ports.append(port)
    elif state == 'close':
        close_ports.append(port)
    elif state == 'open':
        open_ports.append(port)
    else:
        unknown_ports.append(port)
    print("port: %d, state: %s, reason: %s" % (port, state, reason))


def mut_scan(host):
    while not q.empty():
        scap_udp(host, q.get())


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(10000, 20000):
        q.put(i)
    for i in range(500):
        t = threading.Thread(target=mut_scan, args=('192.168.2.248',))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
