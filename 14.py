import copy

data = """my input pt 1""".split("\n")

polymer = "my input pt 2"

data = [i.split(" -> ") for i in data]

key = {}
for i in data:
	key[i[0][0]+i[0][1]] = [i[0][0]+i[1],i[1]+i[0][1]]

last = polymer[-1]

basesets = {}
for i in data:
	basesets[i[0]] = 0
newpolymer = copy.copy(basesets)
for i,v in enumerate(polymer):
	if i==len(polymer)-1:
		break
	newpolymer[v+polymer[i+1]]+=1
polymer = newpolymer

for step in range(40):
	newpolymer = copy.copy(basesets)
	for i in polymer:
		newpolymer[key[i][0]]+=polymer[i]
		newpolymer[key[i][1]]+=polymer[i]
	polymer = newpolymer

elements = {}
for i in polymer:
	if i[0] not in elements:
		elements[i[0]] = 0
	elements[i[0]]+=polymer[i]
elements[last]+=1
highest = 0
lowest = sum([polymer[i] for i in polymer])
for i in elements:
	if elements[i]>highest:
		highest = elements[i]
	if elements[i]<lowest:
		lowest = elements[i]

print(highest-lowest)
