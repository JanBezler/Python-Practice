class Wyjatek(Exception):

    def __init__(self, numer, opis):
        print('Jestem w konstruktorze klasy wyjątek!')
        self.numer = numer
        self.opis = opis

    def getNum(self):
        print(f'Numer błędu: {self.numer}')

    def getOpis(self):
        print(f'Numer błędu: {self.opis}')

    def __del__(self):
        print('Jestem w destruktorze klasy wyjątek!')


class Stos():

    def __init__(self):
        self.tablica = []
        print('Jestem w konstruktorze klasy stos!')

    def push(self, arg, i):
        if i > 9:
            raise(Wyjatek(1, 'BŁĄD METODY PUSH'))
        else:
            self.tablica.append(arg)

    def pop(self, i):
        if i > 9:
            raise(Wyjatek(2, 'BŁĄD METODY POP'))
        else:
            return self.tablica[i]

    def __del__(self):
        del(self.tablica)
        print('Jestem w destruktorze klasy stos!')


class Symulacja:
    def __init__(self):
        self.stos = Stos()
        print('Jestem w konstruktorze klasy symulacja!')

    def symulacja(self):
        for i in range(11):
            try:
                self.stos.push(i, i)

            except Wyjatek as w:
                print(w.numer, w.opis)
                del(w)

        for i in range(11):
            try:
                print(self.stos.pop(i))

            except Wyjatek as w:
                print(w.numer, w.opis)
                del(w)

    def __del__(self):
        print('Jestem w destruktorze klasy symulacja!')


sym = Symulacja().symulacja()
