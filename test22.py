import socket
import sys


def getServiceName(port, proto):
    try:
        name = socket.getservbyport(int(port), proto)
    except:
        return None
    return name


def udp_scan():
    UDP_IP = '192.168.2.248'
    for RPORT in range(1810, 1820):
        MESSAGE = "ping"
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        if client == -1:
            print("udp socket creation failed")
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        if sock1 == -1:
            print("icmp socket creation failed")
        try:
            client.sendto(MESSAGE.encode('utf_8'), (UDP_IP, RPORT))
            sock1.settimeout(1)
            data, addr = sock1.recvfrom(1024)
        except socket.timeout:
            serv = getServiceName(RPORT, 'udp')
            if not serv:
                print('Port {}:      Close'.format(RPORT))
                pass
            else:
                print('Port {}:      Open'.format(RPORT))
        except socket.error as sock_err:
            if (sock_err.errno == socket.errno.ECONNREFUSED):
                print(sock_err('Connection refused'))
            client.close()
            sock1.close()


if __name__ == '__main__':
    udp_scan()
