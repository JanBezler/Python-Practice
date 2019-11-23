def srednia(a,b):
	return((a+b)/2)

def majn():
	print("Podaj dwie liczby:")
	x=float(input("Podaj a:"))
	y=float(input("Podaj b:"))
	print("Średnia z {0} i {1} to:".format(x,y),srednia(x,y))

class funkcja(object):
	def __init__(self):
		if input('Chcesz jeszcze raz? ("tak" lub "nie")')=="tak":
			majn()
			funkcja()
		elif input('Chcesz jeszcze raz? ("tak" lub "nie")')=="nie":
			pass
		else:
			input("Nie umiesz pisać, dzbanie")

majn()
funkcja()