target = [[111,161],[-154,-101]]

besty = 0
yranges = {}

for vel in range(target[1][0],((target[1][0]*-1)+1)*2):
	ypos = 0
	steps = 0
	ranger = []
	top = 0
	while ypos>=target[1][0]:
		steps+=1
		ypos+=vel
		vel-=1
		if ypos>top and ypos>besty:
			top = ypos
		if target[1][1]>=ypos>=target[1][0]:
			besty=top
			ranger.append(steps)
	if len(ranger)!=0:
		if min(ranger) not in yranges:
			yranges[min(ranger)] = {}
		if max(ranger) not in yranges[min(ranger)]:
			yranges[min(ranger)][max(ranger)] = 1
		else:
			yranges[min(ranger)][max(ranger)] += 1

print("a:",besty)

xranges = {}
for vel in range(1,target[0][1]+1):
	xpos = 0
	steps = 0
	ranger = []
	while vel!=0:
		steps += 1
		xpos+=vel
		vel-=1
		if target[0][0]<=xpos<=target[0][1]:
			ranger.append(steps)
	if target[0][0]<=xpos<=target[0][1]:
		ranger.append(9999999999999999999999999)
	if len(ranger)!=0:
		if min(ranger) not in xranges:
			xranges[min(ranger)] = {}
		if max(ranger) not in xranges[min(ranger)]:
			xranges[min(ranger)][max(ranger)] = 1
		else:
			xranges[min(ranger)][max(ranger)] += 1

total = 0

for xmin in xranges:
	for xmax in xranges[xmin]:
		for ymin in yranges:
			for ymax in yranges[ymin]:
				if ymin<=xmin<=ymax or ymin<=xmax<=ymax or xmin<=ymin<=xmax or xmin<=ymax<=xmax:
					total+=xranges[xmin][xmax]*yranges[ymin][ymax]
print("b:",total)
