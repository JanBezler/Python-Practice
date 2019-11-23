# 1: Utwórz tablice kwadratową 5x5, obwód wypełnik cyfrą "5", wnętrze cyfrą "2". oblicz średnią arytmetyczną dla przekątnej
# 2: Wprowadź dwa słowa jako tablice do 20 znaków. Podaj długośc obydwu oraz sprawdź, czy druga litera jednego i drugiego są tożsame
##############################################################################################
def pierwsze():
	def wyswietl(tab): 
		suma=0
		for i in range(len(tab[0])): 
			for j in range(len(tab[0])): 
				if i==len(tab[0])-1 or i==0 or j==len(tab[0])-1 or j==0:
					tab[i][j]=5
				else:
					tab[i][j]=2
				if i==j: suma+=tab[i][j]

		print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in tab]))
		print('\n', "Średnia przekątnej: ", suma/len(tab[0]))

	tablica = []
	size=int(input("Szerokość: "))
	if size!=0:
	    for i in range(size):
	        tablica.append([])
	        for j in range(size):
	            tablica[i].append(j)
	            tablica[i][j]=0
	wyswietl(tablica)
###############################################################################################
def drugie():
	jeden=list(input("Pierwsze słowo (maksymalnie 20 znaków): "))
	dwa=list(input("Drugie słowo (maksymalnie 20 znaków): "))
	if len(jeden)>=20 or len(dwa)>=20: print("\n Jeden z wyrazów jest dłuższy niż 20 znaków!")
	else:
		print("Długość pierwszego wyrazu: ",len(jeden))
		print("Długość drugiego wyrazu: ",len(dwa))
	if len(jeden)<2:
		for i in range(2): jeden.append("null")
	if len(dwa)<2:
		for i in range(2): dwa.append("null")
	if jeden[1]==dwa[1]: print("Drugie litery obu wyrazów są tożsame!")
	else: print("Drugie znaki obu wyrazów nie są tożsame!")

print("----------Pierwszy program----------")
pierwsze()
print("\n ----------Drugi program----------")
drugie()