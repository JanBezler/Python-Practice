text=input("Podaj liczbę czterocyfrową: ")
if len(text)!=4:
	text=input("Podaj liczbę CZTEROCYFROWĄ: ")
	if len(text)!=4:
		print("Dobra spadaj pajacu")
		exit()
i4=0
for i1 in range(len(text)):
	for i2 in range(len(text)):
		if i1==i2: continue
		for i3 in range(len(text)):
			if i3==i1 or i3==i2: continue
			i4=6-i1-i2-i3
			print(text[i1],text[i2],text[i3],text[i4])