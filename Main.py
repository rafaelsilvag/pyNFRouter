# -*- coding: utf-8 -*-
__author__ = 'Rafael S. Guimarães e João Paulo de Brito Gonçalves'

from netfilterqueue import NetfilterQueue
from scapy.all import conf
conf.ipv6_enable=False
from scapy.all import IP
import os
import ipaddr
import socket
from net.InjectPacket import Inject


class Rota(object):
    """
        Objeto Rota
    """
    def __init__(self):
        self.network = None
        self.gateway = ipaddr.IPv4Network("0.0.0.0/0")
        self.interface = ""

def print_and_accept(pkt):
    # Abre o pacote
    data = pkt.get_payload()

    # Transforma em um objeto para ser utilizado no scapy
    packet = IP(data)
    if_out = None
    print "SRC: %s -> DST: %s" % (socket.inet_ntoa(packet.src), socket.inet_ntoa(packet.dst))

    # Verifica qual a interface de destino.
    dest_ip = ipaddr.IPv4Address(packet.dst)
    for rota in rotas:
        if dest_ip in rota.network:
            # Verifica interface de destino
            if_out = rota.interface
            #Injeta pacote em uma determinada interface
            Inject.send(packet=packet, if_out=if_out)
            break

    #pkt.accept()

# Tabela de rotas
rotas = []
# Construindo tabela de roteamento
redeA = Rota()
redeA.network = ipaddr.IPv4Network("172.31.1.0/24")
redeA.interface = "r01-eth0"
# Adicionando rota na tabela de roteamento
rotas.append(redeA)

redeB = Rota()
redeB.network = ipaddr.IPv4Network("172.31.2.0/24")
redeB.interface = "r01-eth1"
# Adicionando rota na tabela de roteamento
rotas.append(redeB)

redeC = Rota()
redeC.network = ipaddr.IPv4Network("172.31.3.0/24")
redeC.interface = "r01-eth2"
# Adicionando rota na tabela de roteamento
rotas.append(redeC)

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)

try:
    # Espera requisições do NetfilterQueue
    nfqueue.run()
    # Adicionando Regra IPTABLES
    os.system("iptables -t nat -F")
    os.system("iptables -t nat -A PREROUTING -j NFQUEUE --queue-num 1")
    #
except KeyboardInterrupt, ex:
    os.system("iptables -t nat -D PREROUTING -j NFQUEUE --queue-num 1")

