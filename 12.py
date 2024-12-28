import copy
data = """my input""".split("\n")
data = [i.split("-") for i in data]

def doublesearch(node,visited,doublevisited):
	if node=="end":
		return 1
	if node.lower()==node:
		if node not in visited:
			visited.append(node)
		else:
			if node == "start":
				return 0
			doublevisited = True
	count = 0
	for i in data:
		if i[0]==node and (i[1] not in visited or not doublevisited):
			count += doublesearch(i[1],copy.deepcopy(visited),doublevisited)
		if i[1]==node and (i[0] not in visited or not doublevisited):
			count += doublesearch(i[0],copy.deepcopy(visited),doublevisited)
	return count
print("a:",doublesearch("start",[],True))
print("b:",doublesearch("start",[],False))
