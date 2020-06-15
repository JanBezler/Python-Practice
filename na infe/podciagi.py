text = []
podciagi = []

for i in open("lol.txt", mode="r"):
    text.append(int(i.strip()))

for i in range(len(text)):
    try:
        r = 0
        podciagi.append([])
        podciagi[i].append(text[i])
        while text[i+r+1] < text[i+r]:  # >rosn | <mal
            podciagi[i].append(text[i+r+1])
            r += 1
    except IndexError:
        print("IndexError")


podciagi.sort(reverse=False, key=lambda e: len(e))

for i in podciagi:
    print(i)
