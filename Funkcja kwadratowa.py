import tkinter as tk
import math

window = tk.Tk()
window.title("Funkcje")
floattype = bool
floattypetext = tk.StringVar()
FodX = tk.StringVar()
Delta = tk.StringVar()
x1 = tk.StringVar()
x2 = tk.StringVar()

tk.Label(window, text="Narzędzie do obliczania wszystkiego związanego z funkcjami", padx=10).pack()

tk.Label(window, text="a:").pack()
ain = tk.Entry(window, width=16)
ain.pack()

tk.Label(window, text="b:").pack()
bin = tk.Entry(window, width=16)
bin.pack()

tk.Label(window, text="c:").pack()
cin = tk.Entry(window, width=16)
cin.pack()

lol = tk.Label(window, text="", font=("Garamond", 2))
lol.pack()


def Function():
    a = ain.get()
    b = bin.get()
    c = cin.get()

    if a == "":
        a = "0"
    if b == "":
        b = "0"
    if c == "":
        c = "0"

    FodX.set("f(x) = {0}x^2 + {1}x + {2}".format(a, b, c))

    try:
        a = float(a)
        b = float(b)
        c = float(c)
        floattype = True
        floattypetext.set("Zapis funkcji poprawny!")
    except ValueError:
        floattype = False
        floattypetext.set("Funkcje z parametrami tylko w wersji premium!")
        x1.set("")
        x2.set("")
        Delta.set("")

    if floattype:
        d = math.pow(b, 2)-4*(a*c)
        Delta.set("Delta: {0}".format(d))
        if d == 0:
            try:
                x = -b/(2*a)
                x1.set("X0: {0}".format(x))
                x2.set("")
            except ZeroDivisionError:
                floattypetext.set("'a' nie może być zerem")
                Delta.set("Delta: {0}".format("błąd"))
        elif d < 0:
            x1.set("Ta funkcja nie posiada pierwiastków")
            x2.set("")
        elif d > 0:
            x1x = (-b-math.sqrt(d))/(2*a)
            x2x = (-b+math.sqrt(d))/(2*a)
            x1.set("X1: {0}".format(x1x))
            x2.set("X2: {0}".format(x2x))


ok = tk.Button(window, text="OK", width=10, command=Function, )
ok.pack()

tk.Label(window, textvariable=floattypetext, padx=100).pack()
tk.Label(window, text="Tu pojawi się zapis funkcji:", padx=100).pack()


tk.Label(window, textvariable=FodX, padx=100).pack()
tk.Label(window, textvariable=Delta, padx=100).pack()
tk.Label(window, textvariable=x1, padx=100).pack()
tk.Label(window, textvariable=x2, padx=100).pack()


tk.mainloop()
