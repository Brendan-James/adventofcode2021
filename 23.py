import copy
import heapq

troughs = ["my input where ABCD = 0123 and amphipods are listed from the bottom to the top"]


hallway = [-1,-1,-1,-1,-1,-1,-1]

def blocked(hallway,troughspot,hallspot):
	blockages = [[[False,True,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,True,False,False,False,False],[False,False,True,True,False,False,False],[False,False,True,True,True,False,False],[False,False,True,True,True,True,False]],[[False,True,True,False,False,False,False],[False,False,True,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,True,False,False,False],[False,False,False,True,True,False,False],[False,False,False,True,True,True,False]],[[False,True,True,True,False,False,False],[False,False,True,True,False,False,False],[False,False,False,True,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,True,False,False],[False,False,False,False,True,True,False]],[[False,True,True,True,True,False,False],[False,False,True,True,True,False,False],[False,False,False,True,True,False,False],[False,False,False,False,True,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,True,False]]]
	for i,v in enumerate(blockages[troughspot][hallspot]):
		if hallway[i]!=-1 and v:
			return True
	return False


distance = [[3,2,2,4,6,8,9],[5,4,2,2,4,6,7],[7,6,4,2,2,4,5],[9,8,6,4,2,2,3]]
todo = [(0,troughs,hallway)]
done = []
added = {f"{0}{troughs}{hallway}":True}

part = "b"

while part == "a":
	score,troughs,hallway = heapq.heappop(todo)
	if (troughs,hallway) in done:
		continue
	done.append((troughs,hallway))
	print(score)
	if troughs == [[0,0],[1,1],[2,2],[3,3]]:
		print(score)
		break
	for i,v in enumerate(hallway):
		if v==-1:
			continue
		if (troughs[v]==[] or troughs[v]==[v]) and not blocked(hallway,v,i):
			newtroughs = copy.deepcopy(troughs)
			newhallway = copy.deepcopy(hallway)
			newtroughs[v].append(v)
			newhallway[i]=-1
			if f"{score+(distance[v][i]+1-len(troughs[v]))*10**v}{newtroughs}{newhallway}" not in added:
				added[f"{score+(distance[v][i]+1-len(troughs[v]))*10**v}{newtroughs}{newhallway}"] = True
				heapq.heappush(todo,(score+(distance[v][i]+1-len(troughs[v]))*10**v,newtroughs,newhallway))

	for i,v in enumerate(troughs):
		if len(v)==0:
			continue
		if v == [i,i] or v == [i]:
			continue
		for j in range(len(hallway)):
			if hallway[j]==-1 and not blocked(hallway,i,j):
				newtroughs = copy.deepcopy(troughs)
				newhallway = copy.deepcopy(hallway)
				newhallway[j] = newtroughs[i].pop()
				if f"{score+(distance[i][j]+2-len(v))*10**v[-1]}{newtroughs}{newhallway}" not in added:
					added[f"{score+(distance[i][j]+2-len(v))*10**v[-1]}{newtroughs}{newhallway}"]=True
					heapq.heappush(todo,(score+(distance[i][j]+2-len(v))*10**v[-1],newtroughs,newhallway))

troughs = ["my input where ABCD = 0123 and amphipods are listed from the bottom to the top"]

todo = [(0,troughs,hallway)]
done = []
added = {f"{0}{troughs}{hallway}":True}

while part == "b":
	score,troughs,hallway = heapq.heappop(todo)
	if (troughs,hallway) in done:
		continue
	done.append((troughs,hallway))
	print(score)
	if troughs == [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]:
		print(score)
		break
	for i,v in enumerate(hallway):
		if v==-1:
			continue
		if (troughs[v]==[] or troughs[v]==[v] or troughs[v]==[v,v] or troughs[v]==[v,v,v]) and not blocked(hallway,v,i):
			newtroughs = copy.deepcopy(troughs)
			newhallway = copy.deepcopy(hallway)
			newtroughs[v].append(v)
			newhallway[i]=-1
			if f"{score+(distance[v][i]+3-len(troughs[v]))*10**v}{newtroughs}{newhallway}" not in added:
				added[f"{score+(distance[v][i]+3-len(troughs[v]))*10**v}{newtroughs}{newhallway}"] = True
				heapq.heappush(todo,(score+(distance[v][i]+3-len(troughs[v]))*10**v,newtroughs,newhallway))
				
	for i,v in enumerate(troughs):
		if len(v)==0:
			continue
		if v == [i,i,i,i] or v == [i,i,i] or v == [i,i] or v == [i]:
			continue
		for j in range(len(hallway)):
			if hallway[j]==-1 and not blocked(hallway,i,j):
				newtroughs = copy.deepcopy(troughs)
				newhallway = copy.deepcopy(hallway)
				newhallway[j] = newtroughs[i].pop()
				if f"{score+(distance[i][j]+4-len(v))*10**v[-1]}{newtroughs}{newhallway}" not in added:
					added[f"{score+(distance[i][j]+4-len(v))*10**v[-1]}{newtroughs}{newhallway}"]=True
					heapq.heappush(todo,(score+(distance[i][j]+4-len(v))*10**v[-1],newtroughs,newhallway))
