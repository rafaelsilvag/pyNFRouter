pyNFRouter - Netfilter Router
=============================

Netfilter Router on UserSpace


Instalation
----------

NetfilterQueue module install:

```sh
pip install NetfilterQueue 
```

Usage
-----

```sh
iptables -t nat -A PREROUTING -j NFQUEUE --queue-num 0
python Main.py
```