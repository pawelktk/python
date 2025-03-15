import math
import random

def rysuj_i_pole(figura, parametr):
    if figura == "kolo":
        r = parametr
        for y in range(-r, r+1):
            wiersz = ""
            for x in range(-r, r+1):
                if x**2 + y**2 <= r**2:
                    wiersz += "*"
                else:
                    wiersz += " "
            print(wiersz)
        return math.pi * r**2
    elif figura == "kwadrat":
        bok = parametr
        for _ in range(bok):
            print("*" * bok)
        return bok * bok
    else:
        return None

def szyfruj_cezara(tekst, klucz):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            baza = ord('A') if znak.isupper() else ord('a')
            wynik += chr((ord(znak) - baza + klucz) % 26 + baza)
        else:
            wynik += znak
    return wynik

def gra_kpn():
    opcje = ["kamień", "papier", "nożyce"]
    gracz = input("Wybierz: kamień, papier, nożyce: ").lower()
    komputer = random.choice(opcje)
    print(f"Komputer wybrał: {komputer}")
    if gracz == komputer:
        return "Remis"
    elif (gracz == "kamień" and komputer == "nożyce") or \
         (gracz == "papier" and komputer == "kamień") or \
         (gracz == "nożyce" and komputer == "papier"):
        return "Wygrałeś!"
    elif gracz in opcje:
        return "Przegrałeś!"
    else:
        return "Nieprawidłowy wybór."

def reverse_string(s):
    return s[::-1]
