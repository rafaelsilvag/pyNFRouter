# -*- coding: utf-8 -*-
__author__ = 'Rafael S. Guimarães e João Paulo de Brito Gonçalves'

from netfilterqueue import NetfilterQueue
from scapy.all import conf
conf.ipv6_enable=False
from scapy.all import IP
import ipaddr
from net.InjectPacket import Inject


class Rota(object):
    """
        Objeto Rota
    """
    def __init__(self):
        self.network = None
        self.gateway = ipaddr.IPv4Network("0.0.0.0/0")
        self.interface = ""
    self.src_mac = ""
    self.dst_mac = ""

def print_and_accept(pkt):
    # Abre o pacote
    data = pkt.get_payload()
    inj = Inject()
    
    # Transforma em um objeto para ser utilizado no scapy
    packet = IP(data)
    if_out = None
    
    print "SRC: %s -> DST: %s" % (packet.src, packet.dst)

    # Verifica qual a interface de destino.
    dest_ip = ipaddr.IPv4Address(packet.dst)
    prefixlen = 0
    if_out=None 
    rota_dst=None
    for rota in rotas:
        if dest_ip in rota.network:
        print rota.network.prefixlen
        # Verifica interface de destino
        if rota.network.prefixlen > prefixlen:
                prefixlen = rota.network.prefixlen
                if_out = rota.interface
        rota_dst = rota
        print "Injetando pacote na interface %s" % (if_out)
        #Injeta pacote em uma determinada interface
    if if_out:
        inj.sendPacket(packet=packet, if_out=if_out, rota=rota_dst)

    if if_out is None:
        pkt.accept()

### Construindo tabela de roteamento
# Tabela de rotas
rotas = []
# Construindo tabela de roteamento
redeA = Rota()
redeA.network = ipaddr.IPv4Network("172.31.1.0/24")
redeA.interface = "eth1"
redeA.src_mac = "08:00:27:93:89:f2"
redeA.dst_mac = "08:00:27:BF:8F:22"
# Adicionando rota na tabela de roteamento
rotas.append(redeA)

redeB = Rota()
redeB.network = ipaddr.IPv4Network("172.31.2.0/24")
redeB.interface = "eth2"
redeB.src_mac = "08:00:27:55:dc:c0"
redeB.dst_mac = "08:00:27:a4:d7:e8"
# Adicionando rota na tabela de roteamento
rotas.append(redeB)

redeC = Rota()
redeC.network = ipaddr.IPv4Network("172.31.3.0/24")
redeC.interface = "r01-eth2"
# Adicionando rota na tabela de roteamento
rotas.append(redeC)
######################

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    # Espera requisições do NetfilterQueue
    nfqueue.run()
    # Adicionando Regra IPTABLES
    #os.system("iptables -t nat -F")
    #os.system("iptables -t nat -A PREROUTING -j NFQUEUE --queue-num 1")
    #
except KeyboardInterrupt, ex:
    print "Finalizado..."
    #os.system("iptables -t nat -D PREROUTING -j NFQUEUE --queue-num 1")

