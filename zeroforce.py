import copy
import math

class graph:
	def __init__(self, incident, colored):
		self.incident = incident
		self.colored = colored
		self.vertexlist = list(incident.keys())
	def is_colored(self, verticy):
		return self.colored[verticy]
	def print_graph(self):
		for vertex in self.vertexlist:
			print(vertex, self.colored[vertex], self.incident[vertex])
	def do_color_change_step(self):
		for vertex in self.vertexlist:
			#print(vertex)
			if self.colored[vertex] == True:
				non_c_adj_count = 0
				nonc_neighbor = None
				for neighbor in self.incident[vertex]:
					if self.colored[neighbor] == False:
						non_c_adj_count +=1
						nonc_neighbor= neighbor
				if non_c_adj_count == 1:
					self.colored[nonc_neighbor] = True
					#print("colored " + nonc_neighbor)
				
			
	def check_if_zfs(self): #checks if the graph is a zero forcing set
		#print("checking a graph...")
		maxiters = len(self.incident)
		i = 0
		tempgraph = copy.deepcopy(self)
		while i < maxiters:
			#print(i)
			tempgraph.do_color_change_step()
			#tempgraph.print_graph()
			i += 1
		#print("done checking")
		for vertex in self.vertexlist:
			if tempgraph.colored[vertex] != True:
				return False
		return True
	def try_all_possible_colorings(self): #that return as a zfs
		blankgraph = copy.deepcopy(self)
		for vertex in blankgraph.vertexlist:
			blankgraph.colored[vertex] = False
		zfsgraphcolorings = []
		for i in range(0, 2**(len(blankgraph.vertexlist))):
			bincount = list('0'*(len(blankgraph.vertexlist)-len(bin(i)[2:]))+bin(i)[2:]) #0s' and 1s
			testgraph = copy.deepcopy(blankgraph)
			for vertex in testgraph.vertexlist:
				testgraph.colored[vertex] = bool(int(bincount[testgraph.vertexlist.index(vertex)]))
			if testgraph.check_if_zfs():
				zfsgraphcolorings.append(testgraph)
		return zfsgraphcolorings

	def num_colored_verticies(self):
		numcolored = 0 
		for vertex in self.colored:
			if self.colored[vertex]:
				 numcolored +=1 
			else:
				pass
		return numcolored

	def get_zfszfn(self):
		zfn = len(self.vertexlist)
		zfsofzfn = None
		zfses = self.try_all_possible_colorings()
		for zfs in zfses:
			thisone = zfs.num_colored_verticies()
			if zfn >= thisone:
				zfn = thisone
				zfsofzfn = zfs
		
		return (zfsofzfn, zfn)
	def get_zfn(self):
		return self.get_zfszfn()[1]
	def get_zfs_example(self):
		return self.get_zfszfn()[0]
		
#coloredgraph = graph({'a' : ["b", "c"], 'b' : ["a", "c"], 'c' : ["a", "b"]},
#{'a' : True, 'b' : True, 'c' : False})
#print(coloredgraph.check_if_zfs())
#print("zfn k3:")
#print(coloredgraph.get_zfn())
test = graph(
{'a' : ['e', 'f', 'g', 'h', 'i'],
'b' : ['e', 'f', 'g', 'h', 'i'],
'c' : ['e', 'f', 'g', 'h', 'i'],
'd' : ['e', 'f', 'g', 'h', 'i'],
'e' : ['a', 'b', 'c', 'd', 'j'],
'f' : ['a', 'b', 'c', 'd', 'j'],
'g' : ['a', 'b', 'c', 'd', 'j'],
'h' : ['a', 'b', 'c', 'd', 'j'],
'i' : ['a', 'b', 'c', 'd', 'j'],
'j' : ['e', 'f', 'g', 'h', 'i']
},
{'a': False,
'b' : True,
'c' : True,
'd' : True,
'e' : True,
'f' : True,
'g' : True,
'h' : False,
'i' : False,
'j' : False
})


 
print(test.get_zfn())
test.get_zfs_example().print_graph()

