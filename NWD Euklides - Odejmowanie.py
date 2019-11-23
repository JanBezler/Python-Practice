def euklides(a,b):
	while a != b:
		if a > b:
			a=a-b
		else:
			b=b-a
	return(a)
	
print("NWD to ",euklides(float(input("Podaj A: ")),float(input("Podaj B: "))))