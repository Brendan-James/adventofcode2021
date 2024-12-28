data = """my input""".split("\n")
matches = {"(":")","[":"]","<":">","{":"}"}
errors = {")":3,"]":57,"}":1197,">":25137}
completes = {"(":1,"[":2,"{":3,"<":4}
ascore = 0
bscores = []
for i in data:
	stack = []
	for j in i:
		if j in matches:
			stack.append(j)
		else:
			if matches[stack.pop()]!=j:
				ascore+=errors[j]
				break
	else:
		tally = 0
		for j in reversed(stack):
			tally*=5
			tally+=completes[j]
		bscores.append(tally)

print("a:",ascore)
print("b:",sorted(bscores)[len(bscores)//2])
