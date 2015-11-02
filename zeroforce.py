import copy
import math
from assort import assort

class graph:
	def __init__(self, adjacency_matrix, colored = {}): #Initialize a graph object
		self.adjacency_matrix = adjacency_matrix #with this adjacency matrix 
		self.colored = colored # and these points colored
		self.vertexlist = list(adjacency_matrix.keys()) # give us a list of vertices
		try:
			self.vertexlist.sort(reverse = True) #try to sort these vertices if they are sortable
		except Exception as e:
			print(e)	#If not, then say that they aren't
		if colored == {}: #If this object was created not specifying no colored vertices
			for vertex in self.vertexlist: #Make the dictionary of non-colored vertices
				self.colored[vertex] = False
		
	def is_colored(self, verticy): #Is this vertex colored?
		return self.colored[verticy]
	def print_graph(self): # Print the graph in a vaugley human readable way
		for vertex in self.vertexlist:
			print(vertex, self.colored[vertex], self.adjacency_matrix[vertex])
	def do_color_change_step(self): # Do the color change step on the graph
		for vertex in self.vertexlist: # For each vertex
			#print(vertex)
			if self.colored[vertex] == True: # If that vertex is colored
				non_c_adj_count = 0
				nonc_neighbor = None
				for neighbor in self.adjacency_matrix[vertex]: #Count the number of non-colored adjacent verticies
					if self.colored[neighbor] == False:
						non_c_adj_count +=1
						nonc_neighbor= neighbor
				if non_c_adj_count == 1: # and if there is only one...
					self.colored[nonc_neighbor] = True # Color it
					#print("colored " + nonc_neighbor)
				
			
	def check_if_zfs(self): #checks if the graph is a zero forcing set
		#print("checking a graph...")
		maxiters = len(self.adjacency_matrix) #The color change step cannot happen more times then points on the graph.
		i = 0
		tempgraph = copy.deepcopy(self) #Don't harm the original graph, color solely on a seperate graph
		while i < maxiters: #Do the color change step maxiters times
			#print(i)
			tempgraph.do_color_change_step()
			#tempgraph.print_graph()
			i += 1
		#print("done checking")
		for vertex in self.vertexlist: # If any of the verticies in the graph aren't colored
			if tempgraph.colored[vertex] != True:
				return False #Say that this isn't a zero forcing set
		return True # If its not not a zero forcing set, then it is a zero forcing set.
	def try_all_possible_colorings(self, verbose = False): #return all possible colorings of the graph
		blankgraph = copy.deepcopy(self) # base this all on a copy of the original graph...
		for vertex in blankgraph.vertexlist: #that has all verticies uncolred
			blankgraph.colored[vertex] = False
		zfsgraphcolorings = []
		for i in range(0, 2**(len(blankgraph.vertexlist))): # try 2^n different combinations

			bincount = list('0'*(len(blankgraph.vertexlist)-len(bin(i)[2:]))+bin(i)[2:]) #0s' and 1s
			#The above line is a binary counter, in the literal sense, and is a good way to try all
			# possible colorings
			testgraph = copy.deepcopy(blankgraph) #make a copy of the graph
			for vertex in testgraph.vertexlist: #and color it based off of the binary counter
				testgraph.colored[vertex] = bool(int(bincount[testgraph.vertexlist.index(vertex)]))
			if testgraph.check_if_zfs(): #then check and see if it is a zero forcing set
				zfsgraphcolorings.append(testgraph) # and append that to a list of zfs colorings.
				if verbose == True:
					testgraph.print_graph()
		return zfsgraphcolorings #return the list of all colorings

	def num_colored_verticies(self): # this counts the number of verticies in the graph
		numcolored = 0 
		for vertex in self.colored: #for each verex
			if self.colored[vertex]: #count that vertex if its colored
				 numcolored +=1 
			else:
				pass
		return numcolored #return the number of colored vertices

	def get_zfszfn(self): # Get the zfs and the zfn for the graph
		zfn = len(self.vertexlist) # the zero forcing number will be at a maximum the number of verteces in g
		zfsofzfn = None
		zfses = self.try_all_possible_colorings() # try all possible colorings
		zfsbyzfn = {} # this will be a list of zero forcing set
		for zfs in zfses: #for each zero focing set
			thisone = zfs.num_colored_verticies() #count the number of colored verticies
			if zfn >= thisone: #if the number of colored verticies is not larger than the current zfn
				zfn = thisone # set the zfn to this graph
				zfsofzfn = zfs 
				zfsbyzfn[zfs] = zfn # add this to the dictonary of zero forcing numbers and zero forcing sets
		
		return (zfsbyzfn, zfn)
	def get_zfn(self):
		return self.get_zfszfn()[1] # this just returns the zero forcing numer
	def get_all_zfs_and_zfn(self):
		zfszfn = self.get_zfszfn() # get the zero forcing set and zero forcing number
		zfs = zfszfn[0] # the list of zero forcing sets is this
		bynumber = assort(zfs) #change from a dictionary of zfns by zfses to zfses by zfns
		numbers = list(bynumber.keys()) #get a list of zfnumbers
		numbers.sort(reverse=True) # sort them greatest to least
		return bynumber[numbers[-1]], zfszfn[1]	# return all of the zero forcing sets and the zero forcing number
		
#coloredgraph = graph({'a' : ["b", "c"], 'b' : ["a", "c"], 'c' : ["a", "b"]},
#{'a' : True, 'b' : True, 'c' : False})
#print(coloredgraph.check_if_zfs())
#print("zfn k3:")
#print(coloredgraph.get_zfn())
from exgraphs import * #grab the dictionaries from the other file
both = graph(notpete6).get_all_zfs_and_zfn() #get info from  the graph noted in graph() from exgraphs.py
for example in both[0]: #print all the zfsets
	print("ZFS:")
	example.print_graph()
	print("")

print(both[1]) #print the zero forcing number

#graph(tree_k_3_3).try_all_possible_colorings(True)
