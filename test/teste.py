import nfqueue
#from netfilterqueue import NetfilterQueue
from dpkt import ip
import socket 

def print_and_accept(pkt):
    data=pkt.get_data()
    res = ip.IP(data)    
    print "SOURCE IP: %s\tDESTINATION IP: %s" % (socket.inet_ntoa(res.src),socket.inet_ntoa(res.dst))
    #pkt.set_verdict(nfqueue.NF_ACCEPT)
    pkt.set_verdict_mark(nfqueue.NF_ACCEPT, 1)
    print dir(pkt)
    #pkt.accept()

q = nfqueue.queue()
#q.open()
#q.bind(1)
q.set_callback(print_and_accept)
q.fast_open(0, socket.AF_INET)
q.set_mode(nfqueue.NFQNL_COPY_PACKET)
#q.create_queue(1)
#nfqueue = NetfilterQueue()
#nfqueue.bind(1, print_and_accept)
try:
    q.try_run()
except KeyboardInterrupt:
    print
