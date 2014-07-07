# -*- coding: utf-8 -*-
__author__ = 'Rafael S. Guimarães e João Paulo de Brito Gonçalves'

# Lib ScaPy
from scapy.all import sendp, conf, Ether, IP, ICMP, TCP, UDP

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
		# Detecta o tipo do pacote para montar corretamente para ser enviado.
		# Monta cabeçalhos ethernet de origem e destino.
		# Verifica o MAC do endereço IP de destino
		resp,sresp=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst='192.168.1.1'),timeout=2)
		# Monta cabeçalho ethernet
		eth_dst = resp[0][1].src
		eth_src = resp[0][1].dst
		eth = Ether(src=eth_src, dst=eth_dst)
		eth.type = 2048
		# Monta cabeçalho IPv4
		ip = IP()
		ip.src = '127.0.0.1'
		ip.dst = '127.0.0.1'
		## Define protocolo de envio
		pdest = None
		if packet == 'ICMP':
			# Monta cabeçalho ICMP
			pdest = ICMP()
			pdest.type = 'echo-request'
			pdest.code = 1
			pdest.chksum = '123123'
			pdest.id = 12
			pdest.seq = 1
		elif packet == 'TCP':
			# Monta cabeçalho TCP
			pdest = TCP()
			pdest.sport = 1234
			pdest.dport = 1234
			pdest.seq = 1
			pdest.ack = 1
			pdest.dataofs = 2
			pdest.reserved = 1
			pdest.flags = 'S'
			pdest.window = 1234
			pdest.chksum = '1123123'
			pdest.urgptr = 0
		elif packet == 'UDP':
			# Monta cabeçalho UDP
			pdest = UDP()
			pdest.sport = 1234
			pdest.dport = 1234
			pdest.len = 12
			pdest.chksum = '1123123'
		if pdest == None:
			pdest = ICMP()
		
		#Envia pacote para a interface de saida delimitada.
		sendp(eth/ip/pdest,iface=if_out)