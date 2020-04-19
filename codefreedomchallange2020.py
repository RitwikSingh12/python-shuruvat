n = int(input())
index = []
jaanvar = []
for idx in range(0,n):
	x = int(input())
	index.append(x)
for idx in range(0,n):
	y = input()
	jaanvar.append(y)


for x in range(0,n):
	for y in range(0,n):
		if x == (index[y]-1):
			if y == x:
				print(jaanvar[y])
				
			elif x+1 == len(jaanvar[y]):
				print(jaanvar[y].upper())

			else:
				print(jaanvar[y].lower())
		