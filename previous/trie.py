class Node:
	def __init__(self, val, leaf=None):
		self.val = val
		self.leaf = leaf
		self.cnt = 0
		self.child = {}

class Trie:
	def __init__(self):
		self.head = Node(None)

	def insert(self, string):
		cur = self.head

		for c in string:
			if c not in cur.child:
				cur.child[c] = Node(c)

			cur.cnt+=1
			cur = cur.child[c]

		cur.leaf = string
		cur.cnt+=1

	def search(self, string):
		cur = self.head

		for c in string:
			if c in cur.child:
				cur = cur.child[c]
			else:
				return False

		if cur.leaf != Node:
			return True

	def dfs(self):
		cur = self.head

		stack = []
		for i in cur.child:
			stack.append(cur.child[i])
		
		while len(stack)!=0:
			cur = stack.pop()

			print(cur.val + ", " + str(cur.cnt))
			for i in cur.child:
				stack.append(cur.child[i])

	def search2(self, prefix, num):
		ret = 0
		cur = self.head

		for c in prefix:
			if c in cur.child:
				cur = cur.child[c]
			else:
				return 0

		ans = []
		for c in cur.child:
			ans.append(cur.child[c])

		for i in range(num-1):
			temp=[]
			for node in ans:
				for c in node.child:
					temp.append(node.child[c])
			ans = temp

		for i in ans:
			if i.leaf != None: ret+=1

		return ret


if __name__=="__main__":
	root = Trie()
	root.insert("asd")
	root.insert("asc")
	root.insert("asg")
	root.insert("avvv")
	root.insert("baby")
	
	#root.dfs()
	print(root.search2("a",2))