# -*- coding: utf-8 -*-
__author__ = 'Rafael S. Guimarães e João Paulo de Brito Gonçalves'

# Lib ScaPy
from scapy.all import conf
conf.ipv6_enable=False
from scapy.all import sendp, srp1, Ether

class Inject(object):
    """
        Classe para manipulação do pacote a ser
        enviado para uma determinada interface.
    """

    def __init__(self):
        pass

    @classmethod
    def send(packet, if_out):
        # Envia informação para interface de saída.
        #  Detecta o tipo do pacote para montar corretamente para ser enviado.
        #  Monta cabeçalhos ethernet de origem e destino.
        #  Verifica o MAC do endereço IP de destino
        resp = srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=packet.dst), iface=if_out, timeout=2)
        # Monta cabeçalho ethernet
        eth_dst = resp.src
        eth_src = resp.dst
        eth = Ether(src=eth_src, dst=eth_dst)
        eth.type = 2048
        #Envia pacote para a interface de saida delimitada.
        sendp(eth/packet,iface=if_out)