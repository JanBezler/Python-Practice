def euklides(a,b):
	while b!=0:
		k=b
		b=a%b
		a=k
	return(a)

print("NWD to ",euklides(float(input("Podaj A: ")),float(input("Podaj B: "))))