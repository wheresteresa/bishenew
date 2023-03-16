#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
import time
import os


class LinuxRouter(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable forwarding on the router
        self.cmd('sysctl -w net.ipv4.ip_forward=1')				# '-w' is not necessary
        self.cmd('sysctl -w net.ipv6.conf.all.forwarding=1')    # this enable ipv6 forwarding on router ! ! !

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        self.cmd('sysctl -w net.ipv6.conf.all.forwarding=0')
        super(LinuxRouter, self).terminate()


class NetworkTopo(Topo):


    def build(self, **_opts):
        
        router1 = self.addNode('r1', cls=LinuxRouter, ip='10.0.15.10/24')
        router2 = self.addNode('r2', cls=LinuxRouter, ip='10.0.15.20/24')
        router3 = self.addNode('r3', cls=LinuxRouter, ip='10.0.15.30/24')
        router4 = self.addNode('r4', cls=LinuxRouter, ip='10.0.15.40/24')
        router5 = self.addNode('r5', cls=LinuxRouter, ip='10.0.15.50/24')
        router6 = self.addNode('r6', cls=LinuxRouter, ip='10.0.15.60/24')
        router7 = self.addNode('r7', cls=LinuxRouter, ip='10.0.15.70/24')
        router8 = self.addNode('r8', cls=LinuxRouter, ip='10.0.15.80/24')
        router9 = self.addNode('r9', cls=LinuxRouter, ip='10.0.15.90/24')
        router10 = self.addNode('r10', cls=LinuxRouter, ip='10.0.15.100/24')
        router11 = self.addNode('r11', cls=LinuxRouter, ip='10.0.15.110/24')
        router12 = self.addNode('r12', cls=LinuxRouter, ip='10.0.15.120/24')
        router13 = self.addNode('r13', cls=LinuxRouter, ip='10.0.15.130/24')
        router14 = self.addNode('r14', cls=LinuxRouter, ip='10.0.15.140/24')

        h1 = self.addHost('h1', ip='10.0.1.100/24', defaultRoute='via 10.0.1.10')
        h2 = self.addHost('h2', ip='10.0.2.100/24', defaultRoute='via 10.0.2.20')
        h3 = self.addHost('h3', ip='10.0.3.100/24', defaultRoute='via 10.0.3.30')
        h4 = self.addHost('h4', ip='10.0.4.100/24', defaultRoute='via 10.0.4.40')
        h5 = self.addHost('h5', ip='10.0.5.100/24', defaultRoute='via 10.0.5.50')
        h6 = self.addHost('h6', ip='10.0.6.100/24', defaultRoute='via 10.0.6.60')
        h7 = self.addHost('h7', ip='10.0.7.100/24', defaultRoute='via 10.0.7.70')
        h8 = self.addHost('h8', ip='10.0.8.100/24', defaultRoute='via 10.0.8.80')
        h9 = self.addHost('h9', ip='10.0.9.100/24', defaultRoute='via 10.0.9.90')
        h10 = self.addHost('h10', ip='10.0.10.100/24', defaultRoute='via 10.0.10.100') #careful with this default route
        h11 = self.addHost('h11', ip='10.0.11.100/24', defaultRoute='via 10.0.11.110')
        h12 = self.addHost('h12', ip='10.0.12.100/24', defaultRoute='via 10.0.12.120')
        h13 = self.addHost('h13', ip='10.0.13.100/24', defaultRoute='via 10.0.13.130')
        h14 = self.addHost('h14', ip='10.0.14.100/24', defaultRoute='via 10.0.14.140')
        

        self.addLink(router1, router12, intfName1='r1-eth1', intfName2='r12-eth1')
        self.addLink(router2, router12, intfName1='r2-eth1', intfName2='r12-eth2')
        self.addLink(router3, router12, intfName1='r3-eth1', intfName2='r12-eth3')
        self.addLink(router7, router12, intfName1='r7-eth1', intfName2='r12-eth4')
        self.addLink(router9, router12, intfName1='r9-eth1', intfName2='r12-eth5')
        self.addLink(router13, router12, intfName1='r13-eth1', intfName2='r12-eth6')
        self.addLink(router14, router12, intfName1='r14-eth1', intfName2='r12-eth7')
        self.addLink(router2, router5, intfName1='r2-eth2', intfName2='r5-eth1')
        self.addLink(router2, router11, intfName1='r2-eth3', intfName2='r11-eth1')
        self.addLink(router4, router5, intfName1='r4-eth1', intfName2='r5-eth2') 
        self.addLink(router4, router13, intfName1='r4-eth2', intfName2='r13-eth2')
        self.addLink(router11, router10, intfName1='r11-eth2', intfName2='r10-eth1')
        self.addLink(router10, router9, intfName1='r10-eth2', intfName2='r9-eth2')
        self.addLink(router9, router8, intfName1='r9-eth3', intfName2='r8-eth1')
        self.addLink(router8, router7, intfName1='r8-eth2', intfName2='r7-eth2')
        self.addLink(router7, router6, intfName1='r7-eth3', intfName2='r6-eth1')
        self.addLink(router6, router13, intfName1='r6-eth2', intfName2='r13-eth3')
        
        self.addLink(h1, router1, intfName2='r1-eth0', params2={'ip': '10.0.1.10/24'})
        self.addLink(h2, router2, intfName2='r2-eth0', params2={'ip': '10.0.2.20/24'})
        self.addLink(h3, router3, intfName2='r3-eth0', params2={'ip': '10.0.3.30/24'})
        self.addLink(h4, router4, intfName2='r4-eth0', params2={'ip': '10.0.4.40/24'})
        self.addLink(h5, router5, intfName2='r5-eth0', params2={'ip': '10.0.5.50/24'})
        self.addLink(h6, router6, intfName2='r6-eth0', params2={'ip': '10.0.6.60/24'})
        self.addLink(h7, router7, intfName2='r7-eth0', params2={'ip': '10.0.7.70/24'})
        self.addLink(h8, router8, intfName2='r8-eth0', params2={'ip': '10.0.8.80/24'})
        self.addLink(h9, router9, intfName2='r9-eth0', params2={'ip': '10.0.9.90/24'})
        self.addLink(h10, router10, intfName2='r10-eth0', params2={'ip': '10.0.10.100/24'})
        self.addLink(h11, router11, intfName2='r11-eth0', params2={'ip': '10.0.11.110/24'})
        self.addLink(h12, router12, intfName2='r12-eth0', params2={'ip': '10.0.12.120/24'})
        self.addLink(h13, router13, intfName2='r13-eth0', params2={'ip': '10.0.13.130/24'})
        self.addLink(h14, router14, intfName2='r14-eth0', params2={'ip': '10.0.14.140/24'})



def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet(controller=None, topo=topo)  # no controller
    net.start()
    info('*** Routing Table on Router:\n')

    r1 = net.getNodeByName('r1')
    r2 = net.getNodeByName('r2')
    r3 = net.getNodeByName('r3')
    r4 = net.getNodeByName('r4')
    r5 = net.getNodeByName('r5')
    r6 = net.getNodeByName('r6')
    r7 = net.getNodeByName('r7')
    r8 = net.getNodeByName('r8')
    r9 = net.getNodeByName('r9')
    r10 = net.getNodeByName('r10')
    r11 = net.getNodeByName('r11')
    r12 = net.getNodeByName('r12')
    r13 = net.getNodeByName('r13')
    r14 = net.getNodeByName('r14')
    
    
    h1 = net.getNodeByName('h1')
    h2 = net.getNodeByName('h2')
    h3 = net.getNodeByName('h3')
    h4 = net.getNodeByName('h4')
    h5 = net.getNodeByName('h5')
    h6 = net.getNodeByName('h6')
    h7 = net.getNodeByName('h7')
    h8 = net.getNodeByName('h8')
    h9 = net.getNodeByName('h9')
    h10 = net.getNodeByName('h10')
    h11 = net.getNodeByName('h11')
    h12 = net.getNodeByName('h12')
    h13 = net.getNodeByName('h13')
    h14 = net.getNodeByName('h14')

    ''' 
    Configure ipv6 for interface. 
    '''
    r1.cmd('ifconfig r1-eth1 inet6 add 2001:1::12/96')
    r12.cmd('ifconfig r12-eth1 inet6 add 2001:1::21/96')
    r2.cmd('ifconfig r2-eth1 inet6 add 2002:1::12/96')
    r12.cmd('ifconfig r12-eth2 inet6 add 2002:1::21/96')
    r3.cmd('ifconfig r3-eth1 inet6 add 2003:1::12/96')
    r12.cmd('ifconfig r12-eth3 inet6 add 2003:1::21/96')
    r7.cmd('ifconfig r7-eth1 inet6 add 2007:1::12/96')
    r12.cmd('ifconfig r12-eth4 inet6 add 2007:1::21/96')
    r9.cmd('ifconfig r9-eth1 inet6 add 2009:1::12/96')
    r12.cmd('ifconfig r12-eth5 inet6 add 2009:1::21/96')
    r13.cmd('ifconfig r13-eth1 inet6 add 2012:1::21/96')
    r12.cmd('ifconfig r12-eth6 inet6 add 2012:1::12/96')
    r14.cmd('ifconfig r14-eth1 inet6 add 2014:1::12/96')
    r12.cmd('ifconfig r12-eth7 inet6 add 2014:1::21/96')
    r2.cmd('ifconfig r2-eth2 inet6 add 2005:1::21/96')
    r5.cmd('ifconfig r5-eth1 inet6 add 2005:1::12/96')
    r2.cmd('ifconfig r2-eth3 inet6 add 2011:1::21/96')
    r11.cmd('ifconfig r11-eth1 inet6 add 2011:1::12/96')
    r4.cmd('ifconfig r4-eth1 inet6 add 2015:1::12/96')
    r5.cmd('ifconfig r5-eth2 inet6 add 2015:1::21/96')
    r4.cmd('ifconfig r4-eth2 inet6 add 2004:1::12/96')
    r13.cmd('ifconfig r13-eth2 inet6 add 2004:1::21/96')
    r11.cmd('ifconfig r11-eth2 inet6 add 2019:1::21/96')
    r10.cmd('ifconfig r10-eth1 inet6 add 2019:1::12/96')
    r10.cmd('ifconfig r10-eth2 inet6 add 2010:1::12/96')
    r9.cmd('ifconfig r9-eth2 inet6 add 2010:1::21/96')
    r9.cmd('ifconfig r9-eth3 inet6 add 2018:1::21/96')
    r8.cmd('ifconfig r8-eth1 inet6 add 2018:1::12/96')
    r8.cmd('ifconfig r8-eth2 inet6 add 2008:1::12/96')
    r7.cmd('ifconfig r7-eth2 inet6 add 2008:1::21/96')
    r7.cmd('ifconfig r7-eth3 inet6 add 2017:1::21/96')
    r6.cmd('ifconfig r6-eth1 inet6 add 2017:1::12/96')
    r6.cmd('ifconfig r6-eth2 inet6 add 2006:1::12/96')
    r13.cmd('ifconfig r13-eth3 inet6 add 2006:1::21/96')
    
    
    
    r1.cmd('ifconfig r1-eth0 inet6 add 1::10/96')
    h1.cmd('ifconfig h1-eth0 inet6 add 1::1/96')
    h1.cmd('route -6 add default gw 1::10 dev h1-eth0')  # add ipv6 default route for h1
    
    r2.cmd('ifconfig r2-eth0 inet6 add 2::20/96')
    h2.cmd('ifconfig h2-eth0 inet6 add 2::2/96')
    h2.cmd('route -6 add default gw 2::20 dev h2-eth0')  # add ipv6 default route for h2
    
    r3.cmd('ifconfig r3-eth0 inet6 add 3::30/96')
    h3.cmd('ifconfig h3-eth0 inet6 add 3::3/96')
    h3.cmd('route -6 add default gw 3::30 dev h3-eth0')  # add ipv6 default route for h3
    
    r4.cmd('ifconfig r4-eth0 inet6 add 4::40/96')
    h4.cmd('ifconfig h4-eth0 inet6 add 4::4/96')
    h4.cmd('route -6 add default gw 4::40 dev h4-eth0')  # add ipv6 default route for h4
    
    r5.cmd('ifconfig r5-eth0 inet6 add 5::50/96')
    h5.cmd('ifconfig h5-eth0 inet6 add 5::5/96')
    h5.cmd('route -6 add default gw 5::50 dev h5-eth0')  # add ipv6 default route for h5
    
    r6.cmd('ifconfig r6-eth0 inet6 add 6::60/96')
    h6.cmd('ifconfig h6-eth0 inet6 add 6::6/96')
    h6.cmd('route -6 add default gw 6::60 dev h6-eth0')  # add ipv6 default route for h6
    
    r7.cmd('ifconfig r7-eth0 inet6 add 7::70/96')
    h7.cmd('ifconfig h7-eth0 inet6 add 7::7/96')
    h7.cmd('route -6 add default gw 7::70 dev h7-eth0')  # add ipv6 default route for h7
    
    r8.cmd('ifconfig r8-eth0 inet6 add 8::80/96')
    h8.cmd('ifconfig h8-eth0 inet6 add 8::8/96')
    h8.cmd('route -6 add default gw 8::80 dev h8-eth0')  # add ipv6 default route for h8
    
    r9.cmd('ifconfig r9-eth0 inet6 add 9::90/96')
    h9.cmd('ifconfig h9-eth0 inet6 add 9::9/96')
    h9.cmd('route -6 add default gw 9::90 dev h9-eth0')  # add ipv6 default route for h9
    
    r10.cmd('ifconfig r10-eth0 inet6 add 10::100/96')
    h10.cmd('ifconfig h10-eth0 inet6 add 10::10/96')
    h10.cmd('route -6 add default gw 10::100 dev h10-eth0')  # add ipv6 default route for h10
    
    r11.cmd('ifconfig r11-eth0 inet6 add 11::110/96')
    h11.cmd('ifconfig h11-eth0 inet6 add 11::11/96')
    h11.cmd('route -6 add default gw 11::110 dev h11-eth0')  # add ipv6 default route for h11
    
    r12.cmd('ifconfig r12-eth0 inet6 add 12::120/96')
    h12.cmd('ifconfig h12-eth0 inet6 add 12::12/96')
    h12.cmd('route -6 add default gw 12::120 dev h12-eth0')  # add ipv6 default route for h12
    
    r13.cmd('ifconfig r13-eth0 inet6 add 13::130/96')
    h13.cmd('ifconfig h13-eth0 inet6 add 13::13/96')
    h13.cmd('route -6 add default gw 13::130 dev h13-eth0')  # add ipv6 default route for h13
    
    r14.cmd('ifconfig r14-eth0 inet6 add 14::140/96')
    h14.cmd('ifconfig h14-eth0 inet6 add 14::14/96')
    h14.cmd('route -6 add default gw 14::140 dev h14-eth0')  # add ipv6 default route for h14
    
    

    info('starting zebra and ospfd service:\n')

    r1.cmd('zebra -f /usr/local/etc/r1zebra.conf -d -z /tmp/r1zebra.api -i /tmp/r1zebra.interface')
    time.sleep(1)  # time for zebra to create api socket
    r2.cmd('zebra -f /usr/local/etc/r2zebra.conf -d -z /tmp/r2zebra.api -i /tmp/r2zebra.interface')
    r3.cmd('zebra -f /usr/local/etc/r3zebra.conf -d -z /tmp/r3zebra.api -i /tmp/r3zebra.interface')
    r4.cmd('zebra -f /usr/local/etc/r4zebra.conf -d -z /tmp/r4zebra.api -i /tmp/r4zebra.interface')
    r5.cmd('zebra -f /usr/local/etc/r5zebra.conf -d -z /tmp/r5zebra.api -i /tmp/r5zebra.interface')
    r6.cmd('zebra -f /usr/local/etc/r6zebra.conf -d -z /tmp/r6zebra.api -i /tmp/r6zebra.interface')
    r7.cmd('zebra -f /usr/local/etc/r7zebra.conf -d -z /tmp/r7zebra.api -i /tmp/r7zebra.interface')
    r8.cmd('zebra -f /usr/local/etc/r8zebra.conf -d -z /tmp/r8zebra.api -i /tmp/r8zebra.interface')
    r9.cmd('zebra -f /usr/local/etc/r9zebra.conf -d -z /tmp/r9zebra.api -i /tmp/r9zebra.interface')
    r10.cmd('zebra -f /usr/local/etc/r10zebra.conf -d -z /tmp/r10zebra.api -i /tmp/r10zebra.interface')
    r11.cmd('zebra -f /usr/local/etc/r11zebra.conf -d -z /tmp/r11zebra.api -i /tmp/r11zebra.interface')
    r12.cmd('zebra -f /usr/local/etc/r12zebra.conf -d -z /tmp/r12zebra.api -i /tmp/r12zebra.interface')
    r13.cmd('zebra -f /usr/local/etc/r13zebra.conf -d -z /tmp/r13zebra.api -i /tmp/r13zebra.interface')
    r14.cmd('zebra -f /usr/local/etc/r14zebra.conf -d -z /tmp/r14zebra.api -i /tmp/r14zebra.interface')
    
    r1.cmd('ospfd -f /usr/local/etc/r1ospfd.conf -d -z /tmp/r1zebra.api -i /tmp/r1ospfd.interface')
    r2.cmd('ospfd -f /usr/local/etc/r2ospfd.conf -d -z /tmp/r2zebra.api -i /tmp/r2ospfd.interface')
    r3.cmd('ospfd -f /usr/local/etc/r3ospfd.conf -d -z /tmp/r3zebra.api -i /tmp/r3ospfd.interface')
    r4.cmd('ospfd -f /usr/local/etc/r4ospfd.conf -d -z /tmp/r4zebra.api -i /tmp/r4ospfd.interface')
    r5.cmd('ospfd -f /usr/local/etc/r5ospfd.conf -d -z /tmp/r5zebra.api -i /tmp/r5ospfd.interface')
    r6.cmd('ospfd -f /usr/local/etc/r6ospfd.conf -d -z /tmp/r6zebra.api -i /tmp/r6ospfd.interface')
    r7.cmd('ospfd -f /usr/local/etc/r7ospfd.conf -d -z /tmp/r7zebra.api -i /tmp/r7ospfd.interface')
    r8.cmd('ospfd -f /usr/local/etc/r8ospfd.conf -d -z /tmp/r8zebra.api -i /tmp/r8ospfd.interface')
    r9.cmd('ospfd -f /usr/local/etc/r9ospfd.conf -d -z /tmp/r9zebra.api -i /tmp/r9ospfd.interface')
    r10.cmd('ospfd -f /usr/local/etc/r10ospfd.conf -d -z /tmp/r10zebra.api -i /tmp/r10ospfd.interface')
    r11.cmd('ospfd -f /usr/local/etc/r11ospfd.conf -d -z /tmp/r11zebra.api -i /tmp/r11ospfd.interface')
    r12.cmd('ospfd -f /usr/local/etc/r12ospfd.conf -d -z /tmp/r12zebra.api -i /tmp/r12ospfd.interface')
    r13.cmd('ospfd -f /usr/local/etc/r13ospfd.conf -d -z /tmp/r13zebra.api -i /tmp/r13ospfd.interface')
    r14.cmd('ospfd -f /usr/local/etc/r14ospfd.conf -d -z /tmp/r14zebra.api -i /tmp/r14ospfd.interface')
    
    r1.cmd('ospf6d -f /usr/local/etc/r1ospf6d.conf -d -z /tmp/r1zebra.api -i /tmp/r1ospf6d.interface')
    r2.cmd('ospf6d -f /usr/local/etc/r2ospf6d.conf -d -z /tmp/r2zebra.api -i /tmp/r2ospf6d.interface')
    r3.cmd('ospf6d -f /usr/local/etc/r3ospf6d.conf -d -z /tmp/r3zebra.api -i /tmp/r3ospf6d.interface')
    r4.cmd('ospf6d -f /usr/local/etc/r4ospf6d.conf -d -z /tmp/r4zebra.api -i /tmp/r4ospf6d.interface')
    r5.cmd('ospf6d -f /usr/local/etc/r5ospf6d.conf -d -z /tmp/r5zebra.api -i /tmp/r5ospf6d.interface')
    r6.cmd('ospf6d -f /usr/local/etc/r6ospf6d.conf -d -z /tmp/r6zebra.api -i /tmp/r6ospf6d.interface')
    r7.cmd('ospf6d -f /usr/local/etc/r7ospf6d.conf -d -z /tmp/r7zebra.api -i /tmp/r7ospf6d.interface')
    r8.cmd('ospf6d -f /usr/local/etc/r8ospf6d.conf -d -z /tmp/r8zebra.api -i /tmp/r8ospf6d.interface')
    r9.cmd('ospf6d -f /usr/local/etc/r9ospf6d.conf -d -z /tmp/r9zebra.api -i /tmp/r9ospf6d.interface')
    r10.cmd('ospf6d -f /usr/local/etc/r10ospf6d.conf -d -z /tmp/r10zebra.api -i /tmp/r10ospf6d.interface')
    r11.cmd('ospf6d -f /usr/local/etc/r11ospf6d.conf -d -z /tmp/r11zebra.api -i /tmp/r11ospf6d.interface')
    r12.cmd('ospf6d -f /usr/local/etc/r12ospf6d.conf -d -z /tmp/r12zebra.api -i /tmp/r12ospf6d.interface')
    r13.cmd('ospf6d -f /usr/local/etc/r13ospf6d.conf -d -z /tmp/r13zebra.api -i /tmp/r13ospf6d.interface')
    r14.cmd('ospf6d -f /usr/local/etc/r14ospf6d.conf -d -z /tmp/r14zebra.api -i /tmp/r14ospf6d.interface')

    CLI(net)
    net.stop()
    os.system("killall -9 ospfd ospf6d zebra")  # this command can also be used to check whether the daemons had been set up
    os.system("rm -f *api*")
    os.system("rm -f *interface*")


if __name__ == '__main__':
    setLogLevel('info')
    run()
