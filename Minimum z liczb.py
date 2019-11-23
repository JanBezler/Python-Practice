k = input("Wpisz liczbę: ")
n = len(str(k))
tab = list(str(k))
tab_cyfr = []

for i in range(10):
    x = tab.count(str(i))
    if x > 0:
        for j in range(x):
            tab_cyfr.append(i)

print("n = ",n)
print("tab_cyfr[] = ",tab_cyfr)
