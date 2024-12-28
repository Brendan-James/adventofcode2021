data = """my input""".split("\n")

data = [i.split(",") for i in data]
data = [[int(i) for i in j] for j in data]

folds2 = ["my input pt 2"]
for i in folds2:
	if i[0]=="x":
		data = [[i[1]*2-j[0],j[1]] if j[0]>i[1] else j for j in data]
	else:
		data = [[j[0],i[1]*2-j[1]] if j[1]>i[1] else j for j in data]
	hashbrowns = {}
	for j in data:
		hashbrowns[str(j)] = 1
	print(sum([hashbrowns[j] for j in hashbrowns]))
grid = [[" " for i in range(6)] for j in range(40)]
for i in data:
	grid[i[0]][i[1]] = "#"
output = ""
for y in range(6):
	for x in range(40):
		output+=grid[x][y]
	output +="\n"
print(output)
