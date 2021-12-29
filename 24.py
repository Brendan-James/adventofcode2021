data = """inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -1
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y""".split("\n")

buckets = {}

for i,v in enumerate(data):
	if i%18 not in buckets:
		buckets[i%18] = []
	buckets[i%18].append(v[4:])

def halt_and_catch_fire():
 	return 1/0

x=0
z=0

digits = "94499992996199" # my input, 14 digits none of which are 0
d = [1,1,1,1,1,26,1,26,26,1,26,26,26,26] 
n = [13,11,12,10,14,-1,14,-16,-8,12,-16,-13,-6,-6] 
m = [6,11,5,6,8,14,9,4,7,13,11,11,6,1] 

for i,w in enumerate(digits):
 	w = int(w)
 	if z<0:
 		halt_and_catch_fire()
 	x = z%26+n[i]
 	z = z//d[i]
 	if x!=w:
 		z *= 26
 		z += w+m[i]

print(z)
#halt_and_catch_fire()

def step(w,z,i):
	d = [1,1,1,1,1,26,1,26,26,1,26,26,26,26] 
	n = [13,11,12,10,14,-1,14,-16,-8,12,-16,-13,-6,-6] 
	m = [6,11,5,6,8,14,9,4,7,13,11,11,6,1] 
	if z<0:
		return 100000000000000000000000000000000000000
	x = z%26+n[i]
	z = z//d[i]
	if x!=w:
		z*=26
		z+=w+m[i]
	return z


d = [1,1,1,1,1,26,1,26,26,1,26,26,26,26] 
n = [13,11,12,10,14,-1,14,-16,-8,12,-16,-13,-6,-6] 
m = [6,11,5,6,8,14,9,4,7,13,11,11,6,1] 

valid = {0:""}

for i in reversed(range(14)):
	new = {}
	for goal in valid:
		for w in range(1,10):
			if d[i]==1:
				if goal%26+n[i]==w:
					if goal not in new:
						new[goal] = str(w)+valid[goal]
					else:
						if int(str(w)+valid[goal])<int(new[goal]):
							new[goal] = str(w)+valid[goal]
			else:
				for bonus in range(26):
					z = goal*26+bonus
					if z%26+n[i]==w:
						new[z] = str(w)+valid[goal]
			z = goal - (w+m[i])
			if z%26!=0:
				continue
			z = z//26
			if d[i]==1:
				if z%26+n[i]!=w and z>=0:
					new[z] = str(w)+valid[goal]
			else:
				for bonus in range(26):
					if (z+bonus)%26+n[i]!=w and z+bonus>=0:
						if z+bonus not in new:
							new[z+bonus] = str(w)+valid[goal]
						else:
							if int(str(w)+valid[goal])<int(new[z+bonus]):
								new[z+bonus] = str(w)+valid[goal]
	if i==0:
		print(i,new)
	valid = new


valid = {0:""}
highest = 0

for i in reversed(range(14)):
	nexth = (26+highest)*27
	highest = 0
	print(i)
	new = {}
	for w in reversed(range(1,10)):
		for z in range(nexth):
			if step(w,z,i) in valid:
				new[z] = str(w)+valid[step(w,z,i)]
				highest = max(highest,z)
				if i==0:
					print(new[z],z)
	valid = new
