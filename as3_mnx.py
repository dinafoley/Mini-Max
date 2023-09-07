#Assignment 3
from as3_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return
        
	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):		
		terminal_val = self.min_v(self.root)
		traversed = self.successors #example of solution_array
		res=Result();


#################  Return the solution here  #################
		res.value=terminal_val #you put the best terminal value for root node here
		res.solution=traversed #you put the solution_array here
#################  Return the solution here  #################

		return res


	def max_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		max_v = 1000  # we use 1000 as the initial_maximum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = min(max_v, self.min_v(deeper_node))
			if max_v > self.currentNode.value:
				self.currentNode = deeper_node
		return max_v

	def min_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		self.currentNode = node
		min_v = -1000  # we use -1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			a = self.max_v(deeper_node)
			b = min_v
			min_v = max(min_v, a)
			if min_v == self.currentNode.value :
				if min_v != b:
					self.successors.append(node.Name)
					self.successors.append(deeper_node.Name)
					self.successors.append(self.currentNode.Name)

		return min_v