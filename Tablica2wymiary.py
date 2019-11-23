def wyswietl(tab):
    sum1=0 #suma liczb pierwszej przekątnej
    sum2=0 #suma liczb drugiej przekątnej
    sum3=0 #wszystkie liczby
    hor1=0 #pierwsza linia horyzontalna
    hor2=0 #ostatnia linia horyzontalna
    for i in range(size):
        k=i+1
        for j in range(size):
            l=j+1
            tab[i][j]=k*l

            if i==j: sum1+=k*l
            if i==len(tab[0])-1-j: sum2+=k*l
            if i==0 : hor1+=tab[0][j]
            if j==len(tab[0])-1: hor2+=tab[i][len(tab[0])-1]
            sum3 += tab[i][j]

    if len(tab[0]) % 2 == 0:
        sum12 = sum1 + sum2
        divisor=len(tab[0])*2
    else:
        sum12 = (sum1 + sum2) - tab[int(len(tab[0]) / 2 - 0.5)][int(len(tab[0]) / 2 - 0.5)]
        divisor=len(tab[0])*2-1

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in tab]))
    print("\n", "Suma liczb pierwszego wiersza: ", hor1,"| Średnia liczb pierwszego wiersza: ",round(hor1/len(tab[0]),2))
    print("\n", "Suma liczb ostatniego wiersza: ", hor2,"| Średnia liczb ostatniego wiersza: ",round(hor2/len(tab[0]),2))
    print("\n","Suma liczb pierwszej przekątnej: ",sum1,"| Średnia liczb pierwszej przekątnej: ",round(sum1/len(tab[0]),2))
    print("\n","Suma liczb drugiej przekątnej: ",sum2,"| Średnia liczb drugiej przekątnej: ",round(sum2/len(tab[0]),2))
    print("\n","Suma liczb obu przekątnych: ",sum12,"| Średnia liczb obu przekątnych: ",round(sum12/divisor,2))
    print("\n","Suma wszystkich liczb: ",sum3,"| Średnia wszystkich liczb: ",round(sum3/(len(tab[0])*len(tab[0])),2))

    #--------------------------------- MAIN ----------------------------------#
tablica = []
size = int(input("Podaj wielkosć tabliczki: "))
if size!=0:
    for i in range(size):
        tablica.append([])
        for j in range(size):
            tablica[i].append(j)
            tablica[i][j]=0

    wyswietl(tablica)
else: print("\n Good idea")