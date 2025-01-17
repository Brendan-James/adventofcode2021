data = """my input""".split("\n")

data = [[int(i) for i in j] for j in data]

def gridadj(x,y):
	adj = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
	adj = [i for i in adj if i[0]>=0 and i[0]<10 and i[1]>=0 and i[1]<10]
	return adj

flashes = 0

for step in range(1000):
	data = [[i+1 for i in j] for j in data]
	flag = True
	while flag:
		flag = False
		for x in range(10):
			for y in range(10):
				if data[x][y]>9:
					flag=True
					data[x][y] = -999999999
					flashes+=1
					for i in gridadj(x,y):
						data[i[0]][i[1]]+=1
	data = [[max(0,i) for i in j] for j in data]
	if step==99:
		print("a:",flashes)
	flag = True
	for x in range(10):
		for y in range(10):
			if data[x][y]!=0:
				flag = False
				break
		if not flag:
			break
	if flag:
		print("b:",step+1)
		break
