data = """my input""".split("\n")

data = [[i for i in j] for j in data]

for step in range(9999999999):
	#print("\n".join([str(i) for i in data]),"\n")
	moved = False
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]==">" and data[i][(j+1)%len(data[0])]==".":
				moved = True
				data[i][j] = "/"
				data[i][(j+1)%len(data[0])] = "*"
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == "/":
				data[i][j] = "."
			if data[i][j] == "*":
				data[i][j] = ">"
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]=="v" and data[(i+1)%len(data)][j]==".":
				moved = True
				data[i][j] = "/"
				data[(i+1)%len(data)][j] = "V"
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == "/":
				data[i][j] = "."
			if data[i][j] == "V":
				data[i][j] = "v"
	if not moved:
		print(step+1)
		break
