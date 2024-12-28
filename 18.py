import copy
adata = ["my input concatenated into one big list"]
bdata = copy.deepcopy(adata)

def find(data):
	splitting = False
	for i1,v1 in enumerate(data):
			if type(v1)==list:
				for i2,v2 in enumerate(v1):
					if type(v2)==list:
						for i3,v3 in enumerate(v2):
							if type(v3) == list:
								for i4,v4 in enumerate(v3):
									if type(v4)==list:
										return ["explode",[i1,i2,i3,i4]]
									else:
										if v4>9 and not splitting:
											splitter = ["split",[i1,i2,i3,i4]]
											splitting = True
							else:
								if v3>9 and not splitting:
									splitter = ["split",[i1,i2,i3]]
									splitting = True
					else:
						if v2>9 and not splitting:
							splitter = ["split",[i1,i2]]
							splitting = True
			else:
				if v1>9 and not splitting:
					splitter = ["split",[i1]]
					splitting = True
	if splitting:
		return splitter
	return ["good",[]]

def read(location):
	global data
	if len(location)==0:
		return data
	if len(location)==1:
		return data[location[0]]
	elif len(location)==2:
		return data[location[0]][location[1]]
	elif len(location)==3:
		return data[location[0]][location[1]][location[2]]
	elif len(location)==4:
		return data[location[0]][location[1]][location[2]][location[3]]
	elif len(location)==5:
		return data[location[0]][location[1]][location[2]][location[3]][location[4]]

def modify(location,value):
	global data
	if len(location)==1:
		data[location[0]] = value
	elif len(location)==2:
		data[location[0]][location[1]] = value
	elif len(location)==3:
		data[location[0]][location[1]][location[2]] = value
	elif len(location)==4:
		data[location[0]][location[1]][location[2]][location[3]] = value
	elif len(location)==5:
		data[location[0]][location[1]][location[2]][location[3]][location[4]] = value

data = adata[0]
del adata[0]

def evaluate(data):
	if type(data)==int:
		return data
	else:
		return 3*evaluate(data[0])+2*evaluate(data[1])


while len(adata)>=1:
	data = [data,adata[0]]
	del adata[0]
	while True:
		result = find(data)
		if result[0]=="good":
			break
		elif result[0]=="split":
			storage = read(result[1])
			modify(result[1],[storage//2,storage-storage//2])
		elif result[0]=="explode":
			storage = read(result[1])
			modify(result[1],0)
			path = copy.deepcopy(result[1])
			while len(path)>0:
				if path[-1]>0:
					path[-1]-=1
					while type(read(path))==list:
						path.append(len(read(path))-1)
					modify(path,read(path)+storage[0])
					break
				else:
					path.pop()
			path = copy.deepcopy(result[1])
			while len(path)>0:
				if path[-1]<len(read(path[:-1]))-1:
					path[-1]+=1
					while type(read(path))==list:
						path.append(0)
					modify(path,read(path)+storage[1])
					break
				else:
					path.pop()
print("a:",evaluate(data))
best = 0
for i,v in enumerate(bdata):
	for j,w in enumerate(bdata):
		if i==j:
			continue
		data = [copy.deepcopy(v),copy.deepcopy(w)]
		while True:
			result = find(data)
			if result[0]=="good":
				break
			elif result[0]=="split":
				storage = read(result[1])
				modify(result[1],[storage//2,storage-storage//2])
			elif result[0]=="explode":
				storage = read(result[1])
				modify(result[1],0)
				path = copy.deepcopy(result[1])
				while len(path)>0:
					if path[-1]>0:
						path[-1]-=1
						while type(read(path))==list:
							path.append(len(read(path))-1)
						modify(path,read(path)+storage[0])
						break
					else:
						path.pop()
				path = copy.deepcopy(result[1])
				while len(path)>0:
					if path[-1]<len(read(path[:-1]))-1:
						path[-1]+=1
						while type(read(path))==list:
							path.append(0)
						modify(path,read(path)+storage[1])
						break
					else:
						path.pop()
		value = evaluate(data)
		best = max(best,value)
print("b:",best)
