from netfilterqueue import NetfilterQueue
from dpkt import ip, icmp, tcp, udp
from scapy.all import *
import socket

def print_and_accept(pkt):
    data=pkt.get_payload()
    res = ip.IP(data)
    res2 = IP(data)
    i = ICMP(data)
    t = TCP(data)
    u = UDP(data)
    print "SOURCE IP: %s\tDESTINATION IP: %s" % (socket.inet_ntoa(res.src),socket.inet_ntoa(res.dst))

    print res2.show2()
    resp=srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst='192.168.0.34'),iface="eth0",timeout=2)
    print resp.dst
    eth_dst = resp.src
    eth_src = resp.dst
    eth = Ether(src=eth_src, dst=eth_dst)
    eth.type = 2048
    sendp(eth/res2/res2,iface="eth0")
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(2, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt, ex:
    print ex