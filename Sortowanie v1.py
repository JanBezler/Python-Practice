def sortowanie():
	for i in range(int(min(liczba)),int(max(liczba))+1):
		for j in range(liczba.count(str(i))):
			sort.append(i)

liczba = list(input("Podaj liczbę do sortowania: "))
ktore = input('Rosnąco "+", czy malejąco "-"? ')
sort = []
if ktore == "+": sortowanie()
elif ktore == "-": sortowanie(); sort.reverse()
else: print("oke")
print(sort)