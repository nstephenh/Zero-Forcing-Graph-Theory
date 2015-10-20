import copy


class graph:
	def __init__(self, incident, colored):
		self.incident = incident
		self.colored = colored
		self.vertexlist = list(incident.keys())
		for vertex in self.colored:
			if not vertex in self.incident:
				 raise (Exception("coloring non-existent vertex"))
	def is_colored(self, verticy):
		return self.colored[verticy]
	def print_graph(self):
		for vertex in self.incident:
			print(vertex, self.colored[vertex], self.incident[vertex])
	def do_color_change_step(self):
		for vertex in self.colored:
			if self.colored[vertex] == True:
				non_c_adj_count = 0
				for neighbor in self.incident[vertex]:
					if self.colored[neighbor] == False:
						 non_c_adj_count +=1
				if non_c_adj_count == 1:
					for neighbor in self.incident[vertex]:
						if self.colored[neighbor] == False:
							self.colored[neighbor] = True
							print("colored " + neighbor)
	def check_if_zfs(self): #checks if the graph is a zero forcing set
		maxiters = len(self.incident)
		i = 0
		tempgraph = copy.deepcopy(self)
		while i < maxiters:
			tempgraph.do_color_change_step()
			i += 1
		for vertex in tempgraph.colored:
			if tempgraph.colored[vertex] != True:
				return False
		return True
	def try_all_possible_colorings(self): #that return as a zfs
		blankgraph = copy.deepcopy(self)
		for vertex in blankgraph.colored:
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
		print("reversed color of vertex " + vertex)
		self.print_graph()
		if self.check_if_zfs() == True:
			return copy.deepcopy(self)
		else:
			print("not a zfs")	
		if self.colored[vertex] == False:
			try:
				nextvertex = self.vertexlist[self.vertexlist.index(vertex) + 1]			
				return self.colornextvertex(nextvertex)
			except:
				pass
		return None
				
				
coloredgraph = graph({'a' : ["b", "c"], 'b' : ["a", "c"], 'c' : ["a", "b"]},
{'a' : True, 'b' : True, 'c' : False})
print(coloredgraph.is_colored('c'))
print(coloredgraph.check_if_zfs())	
print(coloredgraph.is_colored('c'))
coloredgraph.print_graph()
print("now trying every possible coloring")
print(coloredgraph.try_all_possible_colorings())
# petersontest = graph({'a' : ["
