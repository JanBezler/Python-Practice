# sortowanie listy list po indexie
key1 = 0  # index1
indiv = []
nowatabela = []
tabela = [
    [21, 33],
    [23, 37],
    [6, 28],
    [4, 1],
    [94, 66],
    [5, 33],
    [94, 37],
    [94, 66],
    [44, 14]
]

for i in tabela:
    if i[key1] in indiv:
        pass
    else:
        indiv.append(i[key1])

indiv.sort()
indiv.reverse()

for j in indiv:
    for i in tabela:
        if i[key1] == j:
            nowatabela.append(i)

# print(indiv)
print(nowatabela)

########################################

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=lambda e: len(e))
print(cars)


########################################
# palindrom
slowo = list([5, 3, 8, 5, 4, 5,  8, 3, 5])

if list(slowo[:int((len(slowo)+len(slowo) % 2)/2)]) == list(reversed(slowo[int(len(slowo)/2):])):
    print("palindrom")


########################################
# quicksort
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)

print(arr[::-1])
