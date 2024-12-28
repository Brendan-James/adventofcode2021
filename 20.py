import copy
key = [i=="#" for i in "my input pt 1"]

data = """my input pt 2""".split("\n")

data = [[i=="#" for i in j] for j in data]


fill = False

for step in range(50):
	if step==2:
		print("a:",sum([sum([1 if i else 0 for i in j]) for j in data]))
	for i in data:
		i.insert(0,fill)
		i.append(fill)
	data.insert(0,[fill for i in range(len(data[0]))])
	data.append([fill for i in range(len(data[0]))])

	newdata = copy.deepcopy(data)

	for i,v in enumerate(data):
		for j,w in enumerate(v):
			binder = ""
			if i>0 and j>0:
				binder+= "1" if data[i-1][j-1] else "0"
			else:
				binder+= "1" if fill else "0"

			if i>0:
				binder+= "1" if data[i-1][j] else "0"
			else:
				binder+= "1" if fill else "0"

			if i>0 and j<len(data)-1:
				binder+= "1" if data[i-1][j+1] else "0"
			else:
				binder+= "1" if fill else "0"

			if j>0:
				binder+= "1" if data[i][j-1] else "0"
			else:
				binder+= "1" if fill else "0"

			binder+= "1" if data[i][j] else "0"

			if j<len(data)-1:
				binder+= "1" if data[i][j+1] else "0"
			else:
				binder+= "1" if fill else "0"

			if i<len(data)-1 and j>0:
				binder+= "1" if data[i+1][j-1] else "0"
			else:
				binder+= "1" if fill else "0"

			if i<len(data)-1:
				binder+= "1" if data[i+1][j] else "0"
			else:
				binder+= "1" if fill else "0"

			if i<len(data)-1 and j<len(data)-1:
				binder+= "1" if data[i+1][j+1] else "0"
			else:
				binder+= "1" if fill else "0"

			newdata[i][j]=key[int(binder,2)]
	data = newdata
	if key[0] and not fill:
		fill = True
	elif not key[-1] and fill:
		fill = False

#print("\n".join(["".join(["#" if i else "." for i in j]) for j in data]))

print("b:",sum([sum([1 if i else 0 for i in j]) for j in data]))
