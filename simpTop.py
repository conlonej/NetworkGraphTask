from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import random

class FullTopology(Topo):
	def __init__(self, n=4): 
		Topo.__init__(self)
		hosts = [] 
		switch = self.addSwitch('s0')
		for i in range(n):
			host = self.addHost('h%s' % i)
			self.addLink(host, switch)
			hosts.append(host)
		for j in range(n):
			for k in range(1,n-j):
				self.addLink(hosts[j], hosts[j+k])

class StarTopology(Topo):

	def __init__(self, n=4):
		Topo.__init__(self)
		hosts = []
		switch = self.addSwitch('s0')
		for i in range(n):
			host = self.addHost('h%s' % i)
			self.addLink(host, switch)
			hosts.append(host)
		for j in range(1,n):
			self.addLink('h0', hosts[j])

class RandomTopology(Topo):

	def __init__(self, n=4, alpha=0.5):
		Topo.__init__(self)
		hosts = []
		switch = self.addSwitch('s0')
		for i in range(n):
			host = self.addHost('h%s' % i)
			self.addLink(host, switch)
			hosts.append(host)
		
		for j in range(n):
			for k in range(1, n-j):
				coin = random.randint(0,1)
				if coin == 1:
					self.addLink(hosts[j], hosts[j+k])	

class LinearTopology(Topo):
	
	def __init__(self, n=4):
		Topo.__init__(self)
		hosts = []
		switch = self.addSwitch('s0')
		for i in range(n):
			host = self.addHost('h%s' % i)
			self.addLink(host, switch)
			hosts.append(host)
		for j in range(n-1):
			self.addLink(hosts[j], hosts[j+1])



def TopTest():

	filename = raw_input('Enter a configuration file: ')

	with open(filename, 'r') as file:
		configs = file.read().splitlines()
		
	nodes = int(configs[0])
	topology = configs[1]
	alpha = float(configs[2])
	print configs
	if topology == 'linear':
		topo = LinearTopology(nodes)
	elif topology == 'random':
		topo = RandomTopology(nodes,alpha)
	elif topology == 'star':
		topo = StarTopology(nodes)
	elif topology == 'full':
		topo = FullTopology(nodes)
	else:
		print "No topology was recognized.\n"

	net = Mininet(topo)
	net.start()
	print  "Dumping connections"
	dumpNodeConnections(net.hosts)
	print "Testing network connectivity"
	net.pingAll()
	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	TopTest()

 	
