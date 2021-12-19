import copy
adata = [[[[[7,7],2],[[9,2],4]],[[[9,1],5],[[9,6],[6,4]]]],[[[2,0],[8,[9,4]]],[[1,0],0]],[8,[[[9,5],7],[9,7]]],[[[[1,3],[1,8]],[[8,8],5]],[[7,[4,0]],2]],[[[[7,8],3],[9,3]],5],[[5,[[9,3],4]],[[[0,1],7],[6,[8,3]]]],[[[[1,6],[4,1]],[0,3]],[9,[[4,3],[3,2]]]],[[[[7,9],8],4],[[[9,0],1],[[9,8],[0,5]]]],[[[8,7],[6,1]],[[[1,3],[6,6]],[5,[4,5]]]],[[[[9,8],[2,1]],[[2,3],2]],5],[6,3],[[[9,1],6],[[[7,1],[6,8]],[[8,3],[6,4]]]],[4,[[8,[7,1]],[8,[7,2]]]],[[[1,6],[9,[0,8]]],[[6,7],[2,[4,5]]]],[[[[1,8],[9,2]],5],[[[8,6],[2,1]],[0,6]]],[[[[0,2],4],[4,[3,6]]],7],[[[[7,5],5],7],[[[6,0],4],[5,0]]],[[2,1],[[[3,0],[1,4]],7]],[[[[9,4],[2,8]],9],[[[9,1],[7,3]],[1,[2,1]]]],[[[[4,2],3],[6,4]],[[6,0],[1,5]]],[2,6],[[4,6],[[2,2],[3,0]]],[[[[6,4],[0,7]],[0,8]],[[[6,7],2],7]],[[8,[[4,0],[8,4]]],1],[[3,[6,6]],[[[6,4],[1,5]],[4,0]]],[[[9,5],[5,[4,0]]],[[1,[0,6]],[[5,8],0]]],[[[[6,1],8],[3,7]],[[[6,4],0],[[4,8],4]]],[[[[3,1],3],[[3,6],[3,8]]],[[[6,7],0],2]],[[4,1],[[[4,8],7],[3,0]]],[[[[0,6],[1,3]],[[0,8],[1,9]]],3],[[0,[3,1]],[[[0,0],6],[[7,6],3]]],[[6,[[5,4],7]],[8,[5,5]]],[[[6,3],[[8,9],6]],2],[9,[[8,3],7]],[[[1,[3,0]],[[3,7],5]],[[5,8],[[3,7],[8,6]]]],[[[[6,1],2],[[7,8],[3,9]]],[[[3,6],[6,8]],[5,5]]],[[[[6,8],[7,1]],[8,1]],[[[1,6],9],[[3,3],[7,9]]]],[[[[6,9],0],[5,6]],3],[[[9,6],[[0,5],[2,0]]],[[[6,7],7],[2,6]]],[[0,[5,8]],[[1,[4,6]],[4,6]]],[[[[3,3],4],[0,1]],[[[6,5],0],[2,3]]],[0,4],[[5,5],[[[6,5],8],7]],[[[[7,3],[9,1]],[[9,0],2]],[[7,[8,3]],[[9,5],[7,3]]]],[[[[1,2],[7,7]],[9,0]],[0,7]],[[[0,[8,6]],[1,3]],[[6,6],9]],[[[0,2],[4,7]],0],[[[9,[9,6]],1],[[[1,5],[1,7]],[[5,1],[8,1]]]],[[[6,9],4],0],[[[[4,9],6],5],[7,[3,[9,8]]]],[[6,[6,[5,7]]],[0,[[7,4],8]]],[[4,[5,0]],[2,3]],[[[[8,6],9],[3,[1,2]]],[1,[8,[3,8]]]],[[[8,4],[7,2]],9],[[[[6,3],[6,2]],[2,[0,0]]],[[[6,4],[1,6]],[[3,5],6]]],[7,[[[2,4],0],[9,[9,9]]]],[[[9,2],8],[[2,[9,9]],[9,[7,4]]]],[1,[[0,7],[[1,6],0]]],[[[[5,5],4],8],[[9,[6,5]],[[7,4],7]]],[[[[7,6],4],[8,4]],[2,[1,[5,1]]]],[[[2,[1,2]],7],[7,[[9,9],3]]],[1,[[3,[9,9]],[5,6]]],[[3,[[1,8],4]],[[9,[6,9]],2]],[[[2,[4,5]],[1,[9,0]]],[4,1]],[[[7,[5,9]],[7,7]],[[3,[4,0]],[2,[0,0]]]],[[[0,[9,8]],0],[8,[7,1]]],[[[6,6],[0,[4,8]]],3],[[1,[[8,2],[9,9]]],3],[[2,[5,[6,7]]],[[5,3],3]],[[2,[[5,0],[8,5]]],[[7,[0,5]],[[5,7],3]]],[[[[9,4],[4,0]],[6,[7,8]]],[[7,6],1]],[[0,2],6],[[[7,5],[[7,4],[4,1]]],[3,[[6,6],[5,5]]]],[[3,[[0,7],8]],[[1,7],[5,0]]],[[9,[[9,7],[3,0]]],6],[[[[7,9],2],[3,[5,4]]],[[[9,4],[5,8]],[[5,0],[4,2]]]],[[[[4,3],6],7],[[2,6],[5,[0,1]]]],[[1,[3,5]],[[4,[5,0]],1]],[[[9,[3,9]],8],[9,[[2,9],[2,2]]]],[[[0,[5,0]],[[4,4],3]],6],[[[9,3],[[2,4],[8,4]]],[[[6,8],[3,6]],[[4,6],[1,2]]]],[[[[8,2],[3,2]],[4,[1,1]]],[[[7,2],1],[[9,9],[0,5]]]],[[[6,3],[[3,6],9]],[6,5]],[8,[[[8,7],3],[4,3]]],[[[[8,3],3],[[6,1],9]],[[[2,4],[5,9]],[[9,7],1]]],[[[2,[6,4]],[[0,1],3]],[[[1,2],9],[4,7]]],[7,9],[[[3,[1,4]],5],[[4,[5,1]],8]],[[[[7,6],4],0],[5,5]],[[4,[[5,2],5]],[[[0,4],[6,1]],[[3,0],[4,9]]]],[[[[8,6],[6,1]],9],[[[4,1],2],[[9,2],3]]],[[[6,1],[[8,9],[9,0]]],[[[4,4],[3,0]],[[4,2],[9,9]]]],[1,[[[8,8],3],7]],[[1,[4,[6,8]]],[1,[7,0]]],[6,[[3,[2,4]],[[4,5],[5,3]]]],[8,[[9,[6,0]],[[2,5],0]]],[[5,[0,8]],[[7,1],[[5,9],2]]],[[[5,8],[[1,1],4]],[[0,1],[4,3]]],[[3,[1,[7,3]]],[[[6,4],9],[[2,8],[0,1]]]],[[[6,[2,5]],5],[0,[[5,3],[4,2]]]]]
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
