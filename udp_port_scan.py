from kamene.all import *

from kamene.layers.inet import IP, UDP, ICMP


def udp_port_scan(dstip, lport, hport):
    port_list = []
    for p in range(int(lport), int(hport) + 1):
        source_port = random.randint(1024, 65535)
        pkt = IP(dst=dstip) / UDP(sport=source_port, dport=p)
        print(pkt.summary())
        result_raw = sr1(pkt, verbose=False, timeout=0.3)  # 发送三层包，等待接收一个回应
        if result_raw is not None:
            if result_raw.haslayer(ICMP):
                icmpfields = result_raw.getlayer(ICMP).fields
                if icmpfields["type"] == 3 and icmpfields["code"] == 3:
                    print("UDP " + str(p) + "端口不可达,close")
                else:
                    print("UDP " + str(p) + "端口被过滤,filtered")
            if result_raw.haslayer(UDP):
                print("UDP " + str(p) + "端口open")
                port_list.append(str(p))
        elif result_raw is None:
            print("UDP " + str(p) + "端口无响应")
    print("%s 开放的UDP端口为:%s\n" % (dstip, port_list))


if __name__ == '__main__':
    udp_port_scan('192.168.2.248', 1810, 1820)
