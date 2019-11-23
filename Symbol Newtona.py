def silnia(x):
	if x==0:return(1)
	else: return(silnia(x-1)*x)
def newton(n,k):
	if n>=k: return(silnia(n)/(silnia(k)*silnia(n-k)))
	else: return('"n" musi być większe lub równe "k"')

print(newton(int(input('Podaj "n":')),int(input('Podaj "k":'))))