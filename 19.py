import copy
plain = [[0,1,2],[1,2,0],[2,0,1]]
swapped = [[2,1,0],[0,2,1],[1,0,2]]
plan = [[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]]
spaw = [[-1,-1,-1],[1,1,-1],[1,-1,1],[-1,1,1]]
options = []
for i in plain:
	for j in plan:
		option = []
		for n in range(3):
			option.append([i[n],j[n]])
		options.append(option)
for i in swapped:
	for j in spaw:
		option = []
		for n in range(3):
			option.append([i[n],j[n]])
		options.append(option)

data = """my input""".split("\n\n--- scanner  ---\n")

data = [i.split("\n") for i in data]
data = [[i.split(",") for i in j] for j in data]
data = [[[int(i) for i in j] for j in k] for k in data]
hardbreak = False
todo = [0]
done = []
basis = {0:[0,0,0]}
for i in todo:
	done.append(i)
	scannerA = data[i]
	print(i)
	for j,amoungus in enumerate(data):
		if j in done:
			continue
		for a in options:
			scannerB = []
			for l in amoungus:
				newburt = []
				for g in range(3):
					newburt.append(l[a[g][0]]*a[g][1])
				scannerB.append(newburt)
			newbasis = []
			for k in scannerB:
				for l in scannerA:
					relative = [l[0]-k[0],l[1]-k[1],l[2]-k[2]]
					newburt = copy.deepcopy(scannerB)
					for x,y in enumerate(newburt):
						newburt[x] = [y[0]+relative[0],y[1]+relative[1],y[2]+relative[2]]
					if sum([g in scannerA for g in newburt])>=12:
						data[j] = newburt
						basis[j] = copy.deepcopy(relative)
						if j not in todo:
							todo.append(j)
						hardbreak = True
						break
				if hardbreak:
					hardbreak = False
					break

beacons = []
for i in data:
	for j in i:
		if j not in beacons:
			beacons.append(j)
print("a:"+str(len(beacons)))
best = 0
for i in basis:
	for j in basis:
		if i==j:
			continue
		best = max(best,abs(basis[i][0]-basis[j][0])+abs(basis[i][1]-basis[j][1])+abs(basis[i][2]-basis[j][2]))
print("b:"+str(best))
