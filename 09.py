data = """my input""".split("\n")
data = [[int(i) for i in j] for j in data]
visited = []
basins = []
for i in range(100):
	for j in range(100):
		size = 0
		probes = [[i,j]]
		for p in probes:
			if p[0]<0 or p[0]>=100 or p[1]<0 or p[1]>=100:
				continue
			if p[0]*1000+p[1] in visited:
				continue
			visited.append(p[0]*1000+p[1])
			if data[p[0]][p[1]]==9:
				continue
			size+=1
			probes.append([p[0]+1,p[1]])
			probes.append([p[0]-1,p[1]])
			probes.append([p[0],p[1]+1])
			probes.append([p[0],p[1]-1])
		if size>0:
			basins.append(size)
print(sorted(basins))
print(111*106*105)
