def goradol(wysokosc):
	for i in range(wysokosc):
		print("*",end="")
	print("\n",end="")

def bok(wysokosc,szerokosc):
	wysokosc-=2
	szerokosc-=2
	for i in range(wysokosc):
		print("*",end="")
		for i in range(szerokosc):
			print(" ",end="")
		print("*",end="\n")

szerokosc=int(input("Szerokość: "))
wysokosc=int(input("Wyskokość: "))

if wysokosc==1:goradol(szerokosc)
elif szerokosc==1:
	for i in range(wysokosc):
		print("*",end="\n")
else:
	goradol(szerokosc)
	bok(wysokosc,szerokosc)
	goradol(szerokosc)