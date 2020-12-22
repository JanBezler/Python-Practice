import tkinter as tk
import math

window = tk.Tk()
window.title("Klakulator")
floattype=bool
floattypetext1 = tk.StringVar()
floattypetext2 = tk.StringVar()
floattypetext3 = tk.StringVar()
floattypetext4 = tk.StringVar()

def Dodawanie():
    ain = tk.Entry(window, width=16)
    ain.pack()

    tk.Label(window, text="+").pack()
    bin = tk.Entry(window, width=16)
    bin.pack()

    lol= tk.Label(window, text="",font=("Garamond",2))
    lol.pack()

    def Function():
        a=ain.get()
        b=bin.get()

        if a=="": a="0"
        if b=="": b="0"

        try:
            a=float(a)
            b=float(b)
            floattypetext1.set("="+str(a+b))
        except ValueError:
            pass


    tk.Label(window, textvariable=floattypetext1, padx=10).pack()
    ok=tk.Button(window, text="Oblicz", width=10, command=Function,).pack()
    tk.Label(window, text="_________________________", pady=5, padx=20).pack()

def Odejmowanie():
    ain = tk.Entry(window, width=16)
    ain.pack()

    tk.Label(window, text="-").pack()
    bin = tk.Entry(window, width=16)
    bin.pack()

    lol= tk.Label(window, text="",font=("Garamond",2))
    lol.pack()

    def Function():
        a=ain.get()
        b=bin.get()

        if a=="": a="0"
        if b=="": b="0"

        try:
            a=float(a)
            b=float(b)
            floattypetext2.set("="+str(a-b))
        except ValueError:
            pass


    tk.Label(window, textvariable=floattypetext2, padx=10).pack()
    ok=tk.Button(window, text="Oblicz", width=10, command=Function,).pack()
    tk.Label(window, text="_________________________", pady=5, padx=20).pack()

def Mnozenie():
    ain = tk.Entry(window, width=16)
    ain.pack()

    tk.Label(window, text="*").pack()
    bin = tk.Entry(window, width=16)
    bin.pack()

    lol= tk.Label(window, text="",font=("Garamond",2))
    lol.pack()

    def Function():
        a=ain.get()
        b=bin.get()

        if a=="": a="0"
        if b=="": b="0"

        try:
            a=float(a)
            b=float(b)
            floattypetext3.set("="+str(a*b))
        except ValueError:
            pass


    tk.Label(window, textvariable=floattypetext3, padx=10).pack()
    ok=tk.Button(window, text="Oblicz", width=10, command=Function,).pack()
    tk.Label(window, text="_________________________", pady=5, padx=20).pack()

def Dzielenie():
    ain = tk.Entry(window, width=16)
    ain.pack()

    tk.Label(window, text="/").pack()
    bin = tk.Entry(window, width=16)
    bin.pack()

    lol= tk.Label(window, text="",font=("Garamond",2))
    lol.pack()

    def Function():
        a=ain.get()
        b=bin.get()

        if a=="": a="0"
        if b=="": b="0"
        if a==0:
            pass
        else:
            try:
                a=float(a)
                b=float(b)
                floattypetext4.set("="+str(a/b))
            except ValueError:
                pass


    tk.Label(window, textvariable=floattypetext4, padx=10).pack()
    ok=tk.Button(window, text="Oblicz", width=10, command=Function,).pack()
    tk.Label(window, text="_________________________", pady=5, padx=20).pack()



tk.Label(window, text="Jakie działanie chcesz wykonywać?",pady=5,padx=20).pack()
tk.Button(window, text="Dodawanie", width=10, command=Dodawanie).pack()
tk.Button(window, text="Odejmowanie", width=10, command=Odejmowanie).pack()
tk.Button(window, text="Mnożenie", width=10, command=Mnozenie).pack()
tk.Button(window, text="Dzielenie", width=10, command=Dzielenie).pack()
tk.Label(window, text="________________________________",pady=5,padx=20).pack()

tk.mainloop()