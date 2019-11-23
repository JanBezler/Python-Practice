def palindrom():
	iletego=0
	napis=list(input("Pisz słówko: "))
	if napis.count(" ")>=1:
		for i in range(napis.count(" ")):napis.remove(" ")

	if len(napis)%2==0: 
		polowa=len(napis)/2
		for i in range(int(polowa)):
			if(napis[i]==napis[len(napis)-i-1]): iletego+=1
		if iletego*2==len(napis): print("To palindrom")
		else: print("To nie palindrom")

	elif len(napis)%2!=0: 
		polowa=len(napis)/2+0.5
		for i in range(int(polowa)):
			if(napis[i]==napis[len(napis)-i-1]): iletego+=1
		if iletego*2-1==len(napis): print("To palindrom")
		else: print("To nie palindrom")
		
palindrom()
while True:
	odpowiedz=input("Chcesz kontynuować? (tak/nie): ")
	if odpowiedz=="tak": palindrom()
	else: break