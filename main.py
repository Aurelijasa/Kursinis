import tkinter.ttk
from tkinter import *

langas = Tk()

langas.title("Drabužių dydžių konvertavimas")
langas.geometry("400x300")
langas.config(bg='#F2B90C')

sarasas1 = ["JAV", "JK", "Vokietija", "Prancūzija", "Italija", "Korėja"]
jav = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
jk = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
vokietija = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54]
prancuzija = [32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]
italija = [36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
koreja = [44, 44, 55, 55, 66, 66, 77, 77, 88, 88, "Nėra dydžio", "Nėra dydžio", "Nėra dydžio"]

uzrasas1 = Label(langas, text="Drabužių dydžių konvertavimas")
uzrasas2 = Label(langas, text="Pasirinkite drabužių dydžio šalį")

def pasirinkti_meniu(e):
    if meniu1.get() == "JAV":
        meniu2.config(value=jav)
        meniu2.set("Pasirinkti")
    if meniu1.get() == "JK":
        meniu2.config(value=jk)
        meniu2.set("Pasirinkti")
    if meniu1.get() == "Vokietija":
        meniu2.config(value=vokietija)
        meniu2.set("Pasirinkti")
    if meniu1.get() == "Prancūzija":
        meniu2.config(value=prancuzija)
        meniu2.set("Pasirinkti")
    if meniu1.get() == "Italija":
        meniu2.config(value=italija)
        meniu2.set("Pasirinkti")
    if meniu1.get() == "Korėja":
        meniu2.config(value=koreja)
        meniu2.set("Pasirinkti")

meniu1 = tkinter.ttk.Combobox(langas, value=sarasas1)
meniu1.set("Pasirinkti")
meniu1.bind("<<ComboboxSelected>>", pasirinkti_meniu)

uzrasas3 = Label(langas, text="Pasirinkite drabužio dydį")

meniu2 = tkinter.ttk.Combobox(langas, value=[" "])

uzrasas4 = Label(langas, text="Pasirinkite kitą šalį")

kintamasis = StringVar()
rezultatas = Label(langas, text=" ")

def nustatyti():
    if meniu1.get() == "JAV":
        i = jav.index(int(meniu2.get()))
        return i
    if meniu1.get() == "JK":
        i = jk.index(int(meniu2.get()))
        return i
    if meniu1.get() == "Vokietija":
        i = vokietija.index(int(meniu2.get()))
        return i
    if meniu1.get() == "Prancūzija":
        i = prancuzija.index(int(meniu2.get()))
        return i
    if meniu1.get() == "Italija":
        i = italija.index(int(meniu2.get()))
        return i
    if meniu1.get() == "Korėja":
        i = koreja.index(int(meniu2.get()))
        return i

def pakeisti(e):
    if meniu3.get() == "JAV":
        n = nustatyti()
        dydis = jav[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])
    if meniu3.get() == "JK":
        n = nustatyti()
        dydis = jk[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])
    if meniu3.get() == "Vokietija":
        n = nustatyti()
        dydis = vokietija[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])
    if meniu3.get() == "Prancūzija":
        n = nustatyti()
        dydis = prancuzija[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])
    if meniu3.get() == "Italija":
        n = nustatyti()
        dydis = italija[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])
    if meniu3.get() == "Korėja":
        n = nustatyti()
        dydis = koreja[n]
        rezultatas["text"] = (f"Jūsų dydis: {dydis}")
        kintamasis.set(rezultatas["text"])

meniu3 = tkinter.ttk.Combobox(langas, value=sarasas1)
meniu3.set("Pasirinkti")
meniu3.bind("<<ComboboxSelected>>", pakeisti)

def isvalyti():
    rezultatas["text"] = ""

def iseiti():
    langas.destroy()

mygtukas1 = Button(langas, text="Išvalyti", command=isvalyti)
mygtukas2 = Button(langas, text="Užverti", command=iseiti)

uzrasas1.grid(row=0, column=1, sticky=E)
uzrasas2.grid(row=1, column=0)
meniu1.grid(row=2, column=0)
uzrasas3.grid(row=3, column=0)
meniu2.grid(row=4, column=0)
uzrasas4.grid(row=5, column=0)
meniu3.grid(row=6, column=0)
rezultatas.grid(row=7, column=0)
mygtukas1.grid(row=8, column=0)
mygtukas2.grid(row=9, column=0)

langas.mainloop()

#kaip isvalyti boxus?