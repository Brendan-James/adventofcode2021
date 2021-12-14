import copy

data = """KO -> C
SO -> S
BF -> V
VN -> B
OV -> K
VH -> O
KV -> N
KB -> F
NB -> C
HS -> K
PF -> B
HB -> N
OC -> H
FS -> F
VV -> S
KF -> C
FN -> F
KP -> S
HO -> N
NH -> K
OO -> S
FB -> C
BP -> F
CH -> N
SN -> O
KN -> B
CV -> O
CC -> B
VB -> C
PH -> V
CO -> K
KS -> K
BK -> N
FH -> S
PV -> H
CB -> P
FO -> F
BB -> K
OB -> C
HH -> F
ON -> O
FK -> B
NF -> F
SV -> F
CP -> H
SS -> B
OP -> H
NS -> O
HK -> N
BC -> P
NV -> V
VS -> F
PC -> V
CS -> F
NP -> V
PS -> F
VC -> F
KK -> S
PO -> P
HF -> H
KC -> P
SF -> N
BV -> N
FF -> V
FV -> V
BO -> N
OS -> C
OF -> H
CN -> S
NO -> O
NC -> B
VK -> C
HN -> B
PK -> N
SK -> S
HV -> F
BH -> B
OK -> S
VO -> B
BS -> H
PP -> N
SC -> K
BN -> P
FC -> S
SB -> B
SH -> H
NN -> V
NK -> N
VF -> H
CF -> F
PB -> C
SP -> P
KH -> C
VP -> N
CK -> H
HP -> P
FP -> B
HC -> O
PN -> F
OH -> H""".split("\n")

polymer = "CKKOHNSBPCPCHVNKHFFK"

data = [i.split(" -> ") for i in data]

key = {}
for i in data:
	key[i[0][0]+i[0][1]] = [i[0][0]+i[1],i[1]+i[0][1]]

last = polymer[-1]

basesets = {}
for i in data:
	basesets[i[0]] = 0
newpolymer = copy.copy(basesets)
for i,v in enumerate(polymer):
	if i==len(polymer)-1:
		break
	newpolymer[v+polymer[i+1]]+=1
polymer = newpolymer

for step in range(40):
	newpolymer = copy.copy(basesets)
	for i in polymer:
		newpolymer[key[i][0]]+=polymer[i]
		newpolymer[key[i][1]]+=polymer[i]
	polymer = newpolymer

elements = {}
for i in polymer:
	if i[0] not in elements:
		elements[i[0]] = 0
	elements[i[0]]+=polymer[i]
elements[last]+=1
highest = 0
lowest = sum([polymer[i] for i in polymer])
for i in elements:
	if elements[i]>highest:
		highest = elements[i]
	if elements[i]<lowest:
		lowest = elements[i]

print(highest-lowest)
