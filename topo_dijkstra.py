from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel


class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Add links
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)
        self.addLink(s1, s5)
        self.addLink(s2, s5)
        self.addLink(s3, s5)
        self.addLink(s4, s5)
        self.addLink(h2, s3)


def main():
    topo = MyTopo()
    mn = Mininet(topo=topo, controller=RemoteController)
    mn.start()
    CLI(mn)
    mn.stop()


if __name__ == '__main__':
    setLogLevel('info')
    main()

topos = {'ciclo': (lambda: MyTopo())}
