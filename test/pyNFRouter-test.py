""" Teste pyNFRouter

authors: Rafael S. Guimaraes (rafaelg@ifes.edu.br)
         Joao Paulo Brito Goncalves (jpaulo@ifes.edu.br)

Three switches connected:

       h1 --- r1 ---- h2
               |      
               |            
               |      
               h3

"""

from mininet.topo import Topo


class pyNFRouter(Topo):
    """
        pyNFRouter Test
    """

    def __init__(self):
        """
            Create custom topo.
        """

        Topo.__init__(self)

        h1 = self.addHost("h1",
                          ip="172.31.1.100/24",
                          defaultRoute="gw 172.31.1.1")

        h2 = self.addHost("h2",
                          ip="172.31.2.100/24",
                          defaultRoute="gw 172.31.2.1")

        h3 = self.addHost("h3",
                          ip="172.31.3.100/24",
                          defaultRoute="gw 172.31.3.1")

        r01 = self.addHost("r01",
                           ip="172.31.1.1/24")
 
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")

        # Add Hosts on switch on private LAN
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)

        # Add Router on switch on LANs
        self.addLink(r01, s1)
        self.addLink(r01, s2)
        self.addLink(r01, s3)

topos = {'pyNFRouter': (lambda: pyNFRouter())}
