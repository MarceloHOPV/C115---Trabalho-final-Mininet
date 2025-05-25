from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSSwitch, DefaultController
from mininet.cli import CLI

class TopologiaPersonalizada(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s5 = self.addSwitch('s5')

        h1 = self.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03', ip='10.0.0.3/8')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04', ip='10.0.0.4/8')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05', ip='10.0.0.5/8')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06', ip='10.0.0.6/8')
        h7 = self.addHost('h7', mac='00:00:00:00:00:07', ip='10.0.0.7/8')
        h8 = self.addHost('h8', mac='00:00:00:00:00:08', ip='10.0.0.8/8')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s5)
        self.addLink(h4, s5)
        self.addLink(h5, s2)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(h8, s3)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s5)

def run():
    topo = TopologiaPersonalizada()
    net = Mininet(topo=topo, link=TCLink, controller=DefaultController, switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
