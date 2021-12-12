import copy
data = """fw-ll
end-dy
tx-fw
tx-tr
dy-jb
ZD-dy
dy-BL
dy-tr
dy-KX
KX-start
KX-tx
fw-ZD
tr-end
fw-jb
fw-yi
ZD-nr
start-fw
tx-ll
ll-jb
yi-jb
yi-ll
yi-start
ZD-end
ZD-jb
tx-ZD""".split("\n")
data = [i.split("-") for i in data]
def search(node,visited):
	if node=="end":
		return 1
	if node.lower()==node:
		visited.append(node)
	count = 0
	for i in data:
		if i[0]==node and i[1] not in visited:
			count += search(i[1],copy.deepcopy(visited))
		if i[1]==node and i[0] not in visited:
			count += search(i[0],copy.deepcopy(visited))
	return count

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
print("a:",search("start",[]))
print("b:",doublesearch("start",[],False))
