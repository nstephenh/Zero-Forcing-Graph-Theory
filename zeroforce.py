import copy


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
		for vertex in blankgraph.vertexlist:
			result = None
			for i in (range(0, len(blankgraph.vertexlist))):
				result = blankgraph.colornextvertex(vertex)
				if result != None:
					zfsgraphcolorings.append(result)
			
		return zfsgraphcolorings
	def colornextvertex(self, vertex):
		self.colored[vertex] = not self.colored[vertex]
		# print("reversed color of vertex " + vertex) debug line
		# self.print_graph() # debug line
		if self.check_if_zfs() == True:
			return copy.deepcopy(self)
		else:
			#print("not a zfs") #debug line
			pass	
		if self.colored[vertex] == False:
			try:
				nextvertex = self.vertexlist[self.vertexlist.index(vertex) + 1]			
				return self.colornextvertex(nextvertex)
			except:
				pass
		return None
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
			#print(thisone)
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
{'a' : ['b', 'p', 'q'],
'b' : ['a', 'c', 'h', 'p'],
'c' : ['b', 'd', 'g', 'o'],
'd' : ['e', 'f', 'h', 'c'],
'e' : ['f', 'd', 'q'],
'f' : ['d', 'e', 'g', 'l'],
'g' : ['c', 'h', 'k', 'f'],
'h' : ['b', 'g', 'i', 'j'],
'i' : ['h', 'j', 'q'],
'j' : ['h', 'i', 'k', 'p'],
'k' : ['g', 'j', 'l', 'o'],
'l' : ['f', 'k', 'm', 'n'],
'm' : ['l', 'n', 'q'],
'n' : ['d', 'l', 'm', 'o'],
'o' : ['c', 'k', 'n', 'p'],
'p' : ['a', 'b', 'j', 'o'],
'q' : ['a', 'e', 'i', 'm']
},
{'a': False,
'b' : False,
'c' : False,
'd' : False,
'e' : False,
'f' : False,
'g' : False,
'h' : False,
'i' : False,
'j' : False,
'k' : False,
'l' : False,
'm' : False,
'n' : False,
'o' : False,
'p' : False,
'q' : False
}) 
print(test.get_zfn())
test.get_zfs_example().print_graph()

