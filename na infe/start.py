# wczytywanie danch
dane = []
with open("dane.txt") as plik:
    for i in plik:
        dane.append(list(map(lambda x: float(x), i.strip().split())))

dane = []
with open("dane.txt") as plik:
    for i in plik:
        dane.append(int(i.strip()))

