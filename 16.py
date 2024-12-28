import numpy
data = "my input"


data = bin(int(data, 16))[2:].zfill(len(data) * 4)

index = 0
depthchart = []
total = 0
subpackets = []
math = []
formulachart = {0:"+",1:"*",2:"min",3:"max",5:">",6:"<",7:"="}

while sum(int(i) for i in data[index:]) != 0:
	while len(subpackets)!=0:
		if index==subpackets[-1]:
			subpackets.pop()
			depthchart.pop()
			while len(depthchart)!=0:
				if len(depthchart)!=0:
					depthchart[-1]-=1
				if depthchart[-1]==0:
					depthchart.pop()
				else:
					break
		else:
			break
	version = int(data[index:index+3],2)
	total+=version
	index+=3
	ptype = int(data[index:index+3],2)
	index+=3
	if ptype==4:
		num = ""
		while data[index]=="1":
			num+=data[index+1:index+5]
			index+=5
		num+=data[index+1:index+5]
		index+=5
		num = int(num,2)
		target = math
		for i in range(len(depthchart)):
			target = target[-1]
		target.append(num)
	else:
		target = math
		for i in range(len(depthchart)):
			target = target[-1]
		target.append([formulachart[ptype]])
		length = data[index]=="0"
		index+=1
		if length:
			length = int(data[index:index+15],2)
			index+=15
			subpackets.append(index+length)
			depthchart.append(-1)
		else:
			depthchart.append(int(data[index:index+11],2)+1)
			index+=11
	while len(depthchart)!=0:
		if len(depthchart)!=0:
			depthchart[-1]-=1
		if depthchart[-1]==0:
			depthchart.pop()
		else:
			break
	if len(depthchart)==0:
		break

def calc(x):
	if type(x)==int:
		return x
	nums=[]
	for i,v in enumerate(x):
		if i==0:
			continue
		nums.append(calc(v))
	if x[0]=="+":
		return sum(nums)
	if x[0]=="*":
		return numpy.prod(nums)
	if x[0]=="min":
		return min(nums)
	if x[0]=="max":
		return max(nums)
	if x[0]==">":
		return 1 if nums[0]>nums[1] else 0
	if x[0]=="<":
		return 1 if nums[0]<nums[1] else 0
	if x[0]=="=":
		return 1 if nums[0]==nums[1] else 0


print("a:",total)
#print(math)
print("b:",calc(math[0]))
