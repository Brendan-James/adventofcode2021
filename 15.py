import copy

data = """my input""".split("\n")

data = [[int(i) for i in j] for j in data]

bigdata = []
for x in range(5):
	for i in data:
		segment = []
		for y in range(5):
			for j in i:
				num = j+x+y
				while num>9:
					num-=9
				segment.append(num)
		bigdata.append(segment)


part = "b"

if part=="b":
	data = bigdata

data[0][0] = 0

working = copy.deepcopy(data)

for i in range(len(data)):
	for j in range(len(data)):
		if i==0 and j==0:
			continue
		options = []
		if i!=0:
			options.append(working[i-1][j])
		if j!=0:
			options.append(working[i][j-1])
		working[i][j]=data[i][j]+min(options)

prev = 0

while prev!=working[-1][-1]:
	prev = working[-1][-1]
	print(working[-1][-1])
	for i in range(len(data)):
		for j in range(len(data)):
			if i==0 and j==0:
				continue
			options = []
			if i!=0:
				options.append(working[i-1][j])
			if j!=0:
				options.append(working[i][j-1])
			if i+1!=len(data):
				options.append(working[i+1][j])
			if j+1!=len(data):
				options.append(working[i][j+1])
			working[i][j]=data[i][j]+min(options)

print(working[-1][-1])
