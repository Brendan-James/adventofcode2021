p1 = 8
p2 = 7

p1score = 0
p2score = 0

rolls = 0
die = 1

def modinc(n,m,mod):
	total = n+m
	while total>mod:
		total-=mod
	return total

while True:
	p1=modinc(die,p1,10)
	die = modinc(die,1,100)
	rolls+=1
	p1=modinc(die,p1,10)
	die = modinc(die,1,100)
	rolls+=1
	p1=modinc(die,p1,10)
	die = modinc(die,1,100)
	rolls+=1
	p1score+=p1
	if p1score>=1000:
		print("a:",p2score*rolls)
		break
	p2=modinc(die,p2,10)
	die = modinc(die,1,100)
	rolls+=1
	p2=modinc(die,p2,10)
	die = modinc(die,1,100)
	rolls+=1
	p2=modinc(die,p2,10)
	die = modinc(die,1,100)
	rolls+=1
	p2score+=p2
	if p2score>=1000:
		print("a:",p1score*rolls)
		break

scores = {"0,0,8,7":1}
p1wins = 0
p2wins = 0
step = 0

while len(scores)>0:
	step+=1
	newscores = {}
	for i, v in scores.items():
		i = i.split(",")
		for A in range(1,4):
			if 0<step%6<4:
				p1 = modinc(int(i[2]),A,10)
				if step%3==0:
					p1score = int(i[0])+p1
				else:
					p1score = int(i[0])
				if p1score>=21:
					p1wins+=v
					continue
				p2 = int(i[3])
				p2score = int(i[1])
			else:
				p2 = modinc(int(i[3]),A,10)
				if step%3==0:
					p2score = int(i[1])+p2
				else:
					p2score = int(i[1])
				if p2score>=21:
					p2wins+=v
					continue
				p1 = int(i[2])
				p1score = int(i[0])
			if f"{p1score},{p2score},{p1},{p2}" not in newscores:
				newscores[f"{p1score},{p2score},{p1},{p2}"] = v
			else:
				newscores[f"{p1score},{p2score},{p1},{p2}"]+= v
	scores = newscores
print("b:",max(p1wins,p2wins))
