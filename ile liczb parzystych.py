wyniki=[]
for i in range(int(input("Ile liczb chcesz zprawdzić mordeczko? "))):
	liczba=int(input("Podaj liczbę nr {0}:".format(i+1)))
	if liczba%2==0: wyniki.append(liczba)
print("Parzyste to: ", wyniki)