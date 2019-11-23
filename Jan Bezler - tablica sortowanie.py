tablica = [[[6],[8],[1]],[[7],[4],[9]],[[5],[2],[3]]]

for item in tablica:
	print(item)
mini=tablica[0][0]
maxi=tablica[0][0]
for x in range(3):
	for y in range(3):
		if tablica[x][y] > maxi: maxi = tablica[x][y]
		if tablica[x][y] < mini: mini = tablica[x][y]