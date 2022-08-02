from kamene.all import *
import ipaddress

from kamene.layers.inet import IP, ICMP


def host_scan(net):
    net = ipaddress.ip_network(net)
    ip_list = []
    for ip in net.hosts():  # 迭代可用的主机地址
        id_no = random.randint(1, 65535)
        pkt = IP(dst=str(ip)) / ICMP(id=id_no, seq=1)
        # print(pkt.summary())
        result_raw = sr1(pkt, timeout=0.2, verbose=False)
        if result_raw is None:
            print(str(ip) + "不在线")
        elif result_raw is not None:
            ip_list.append(str(ip))  # ip默认类型未IPv4adress，需转换为str类型
            print(str(ip) + "在线")
    print("在线主机如下：\n%s" % ip_list)


if __name__ == '__main__':
    host_scan('192.168.2.0/24')
