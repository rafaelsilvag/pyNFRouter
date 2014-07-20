# -*- coding: utf-8 -*-
__author__ = 'Rafael S. Guimarães e João Paulo de Brito Gonçalves'

# Lib ScaPy
from scapy.all import conf
conf.ipv6_enable=False
from scapy.all import sendp, srp1, Ether, ARP

class Inject(object):
    """
        Classe para manipulação do pacote a ser
        enviado para uma determinada interface.
    """

    def __init__(self):
        pass

    def sendPacket(self, packet, if_out, rota):
        # Envia informação para interface de saída.
        #  Detecta o tipo do pacote para montar corretamente para ser enviado.
        #  Monta cabeçalhos ethernet de origem e destino.
        #  Verifica o MAC do endereço IP de destino
        #resp = srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=packet.dst), iface=if_out, timeout=2)
        # #print "Resposta ARP destino %s : %s"  % (packet.dst, resp)
        # Monta cabeçalho ethernet
        print rota.src_mac
        print rota.dst_mac
        #eth_dst = resp.src
        #eth_src = resp.dst
        eth = Ether(src=rota.src_mac, dst=rota.dst_mac)
        eth.type = 2048
        packet.show2()
        #Envia pacote para a interface de saida delimitada.
        sendp(eth/packet, iface=if_out)
