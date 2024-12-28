data = """my input""".split("\n")
data = [i.split(" | ") for i in data]
data = [[i.split(" ") for i in j] for j in data]
data = [[[''.join(sorted(i)) for i in j] for j in k] for k in data]
count = 0
for i in data:
	value = 0
	digits = ["","","","","","","","","",""]
	digits[1] = [j for j in i[0] if len(j)==2][0]
	digits[4] = [j for j in i[0] if len(j)==4][0]
	digits[7] = [j for j in i[0] if len(j)==3][0]
	digits[8] = [j for j in i[0] if len(j)==7][0]
	digits[9] = [j for j in i[0] if sum([k in j for k in digits[4]])==4 and len(j)==6][0]
	digits[0] = [j for j in i[0] if sum([k in j for k in digits[1]])==2 and len(j)==6 and j!=digits[9]][0]
	digits[6] = [j for j in i[0] if len(j)==6 and j!=digits[9] and j!=digits[0]][0]
	digits[3] = [j for j in i[0] if sum([k in j for k in digits[7]])==3 and len(j)==5][0]
	digits[5] = [j for j in i[0] if sum([k in j for k in digits[6]])==5 and len(j)==5][0]
	digits[2] = [j for j in i[0] if len(j)==5 and j!=digits[3] and j!=digits[5]][0]
	for j in i[1]:
		for x,k in enumerate(digits):
			if j==k:
				value*=10
				value+=x
				break
	count+=value
	print(value)
print(count)
