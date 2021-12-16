import numpy
data = "6051639005B56008C1D9BB3CC9DAD5BE97A4A9104700AE76E672DC95AAE91425EF6AD8BA5591C00F92073004AC0171007E0BC248BE0008645982B1CA680A7A0CC60096802723C94C265E5B9699E7E94D6070C016958F99AC015100760B45884600087C6E88B091C014959C83E740440209FC89C2896A50765A59CE299F3640D300827902547661964D2239180393AF92A8B28F4401BCC8ED52C01591D7E9D2591D7E9D273005A5D127C99802C095B044D5A19A73DC0E9C553004F000DE953588129E372008F2C0169FDB44FA6C9219803E00085C378891F00010E8FF1AE398803D1BE25C743005A6477801F59CC4FA1F3989F420C0149ED9CF006A000084C5386D1F4401F87310E313804D33B4095AFBED32ABF2CA28007DC9D3D713300524BCA940097CA8A4AF9F4C00F9B6D00088654867A7BC8BCA4829402F9D6895B2E4DF7E373189D9BE6BF86B200B7E3C68021331CD4AE6639A974232008E663C3FE00A4E0949124ED69087A848002749002151561F45B3007218C7A8FE600FC228D50B8C01097EEDD7001CF9DE5C0E62DEB089805330ED30CD3C0D3A3F367A40147E8023221F221531C9681100C717002100B36002A19809D15003900892601F950073630024805F400150D400A70028C00F5002C00252600698400A700326C0E44590039687B313BF669F35C9EF974396EF0A647533F2011B340151007637C46860200D43085712A7E4FE60086003E5234B5A56129C91FC93F1802F12EC01292BD754BCED27B92BD754BCED27B100264C4C40109D578CA600AC9AB5802B238E67495391D5CFC402E8B325C1E86F266F250B77ECC600BE006EE00085C7E8DF044001088E31420BCB08A003A72BF87D7A36C994CE76545030047801539F649BF4DEA52CBCA00B4EF3DE9B9CFEE379F14608"


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
