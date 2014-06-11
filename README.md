pyNFRouter - Netfilter Router
=============================

Netfilter Router on UserSpace


Instalation
----------

Install library libnetfilter-queue (Ubuntu 12.04):
```sh
$ sudo apt-get install libnetfilter-queue-dev libnetfilter-queue1
```

NetfilterQueue module install:

```sh
$ pip install NetfilterQueue 
```

Usage
-----

```sh
$ iptables -t nat -A PREROUTING -j NFQUEUE --queue-num 0
$ cd /usr/local/pyNFRouter
$ python Main.py
```

Configuration
-------------

```config
[general]
logfile=/var/log/pyNFRouter/pyNFRouter.log
path=/usr/local/pyNFRouter

[queue0]
number=0
tablename=queue0
logqueue=/var/log/pyNFRouter/queue0.log
```