data = """my input""".split("\n")

newdata = []
for i in data:
	onoff = i[:2]=="on"
	i = i[5 if onoff else 6:]
	x = [0,0]
	x[0] = int(i[:i.find("..")])
	i = i[i.find("..")+2:]
	x[1] = int(i[:i.find(",y=")])
	i = i[i.find(",y=")+3:]
	y = [0,0]
	y[0] = int(i[:i.find("..")])
	i = i[i.find("..")+2:]
	y[1] = int(i[:i.find(",z=")])
	i = i[i.find(",z=")+3:]
	z = [0,0]
	z[0] = int(i[:i.find("..")])
	i = i[i.find("..")+2:]
	z[1] = int(i)
	newdata.append([onoff,sorted(x),sorted(y),sorted(z)])
data = newdata

def intersect(a,b):
	Ax,Ay,Az = a
	Bx,By,Bz = b
	Ox = [max(Ax[0],Bx[0]),min(Ax[1],Bx[1])]
	if Ox[0]>Ox[1]:
		return "nope"
	Oy = [max(Ay[0],By[0]),min(Ay[1],By[1])]
	if Oy[0]>Oy[1]:
		return "nope"
	Oz = [max(Az[0],Bz[0]),min(Az[1],Bz[1])]
	if Oz[0]>Oz[1]:
		return "nope"
	return [Ox,Oy,Oz]

plusregions = []
minusregions = []

count = 0
for i in reversed(data[:20]):
	onoff,x,y,z = i
	newminusregions = [[x,y,z]]
	newplusregions = []
	if onoff:
		count+=(x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1)
	for j in minusregions:
		result = intersect([x,y,z],j)
		if result=="nope":
			continue
		else:
			newplusregions.append(result)
			if onoff:
				count-=(result[0][1]-result[0][0]+1)*(result[1][1]-result[1][0]+1)*(result[2][1]-result[2][0]+1)
	for j in plusregions:
		result = intersect([x,y,z],j)
		if result=="nope":
			continue
		else:
			newminusregions.append(result)
			if onoff:
				count+=(result[0][1]-result[0][0]+1)*(result[1][1]-result[1][0]+1)*(result[2][1]-result[2][0]+1)
	plusregions+=newplusregions
	minusregions+=newminusregions

print("a:",count)

plusregions = []
minusregions = []

count = 0
for i in reversed(data):
	onoff,x,y,z = i
	newminusregions = [[x,y,z]]
	newplusregions = []
	if onoff:
		count+=(x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1)
	for j in minusregions:
		result = intersect([x,y,z],j)
		if result=="nope":
			continue
		else:
			newplusregions.append(result)
			if onoff:
				count-=(result[0][1]-result[0][0]+1)*(result[1][1]-result[1][0]+1)*(result[2][1]-result[2][0]+1)
	for j in plusregions:
		result = intersect([x,y,z],j)
		if result=="nope":
			continue
		else:
			newminusregions.append(result)
			if onoff:
				count+=(result[0][1]-result[0][0]+1)*(result[1][1]-result[1][0]+1)*(result[2][1]-result[2][0]+1)
	plusregions+=newplusregions
	minusregions+=newminusregions

print("b:",count)
