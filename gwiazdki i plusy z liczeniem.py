bloki=int(input("Ilość bloków: "))
wblokach=int(input("Ilość linii w blokach: "))
dlugosc=int(input("Długość wierszy: "))

x=0
p=0

def iksy(x):
	for i in range(dlugosc):
		print("x",end='')
		x+=1
	print("\n")
	return(x)

def plusy(p):
	for i in range(dlugosc):
		print("+",end='')
		p+=1
	print("\n")
	return(p)

for i in range(bloki):
	if i%2==0: 
		for j in range(wblokach):x=iksy(x)
	else:
		for j in range(wblokach):p=plusy(p)

print("x= {0}".format(x))
print("+= {0}".format(p))