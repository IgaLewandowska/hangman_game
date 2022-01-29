import getpass
import sys
haslo = getpass.getpass("Wprowadź hasło do odgadnięcia: ").upper()
kategoria = input("Kategoria: ")
odpowiedz = list(haslo)
puste = ["_"]*len(haslo)
zycie = 5
dobre_strzaly = []
zle_strzaly = []

n = 0
while n < len(odpowiedz):
    if odpowiedz[n] == " ":
        puste[n] = " "
    n += 1
print(puste)
while True:
    literka = input("Podaj literkę: ").upper()
    sys.stdout.write("\033[K")

    if len(literka) != 1:
        print("Podaj jedną literkę")
        continue
    if literka in odpowiedz:
        i = 0
        while i < len(odpowiedz):
            if literka == odpowiedz[i]:
                puste[i] = literka
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                if literka in dobre_strzaly:
                    print("ta literka została już użyta, wprowadź inną")
                else:
                    dobre_strzaly.append(literka)
            i += 1
        print(puste)
        if puste == odpowiedz:
            print("Brawo! Zgadłeś")
            break
        continue
    elif zycie >= 2:
        zycie -= 1
        if literka in zle_strzaly:
            pass
        else:
            zle_strzaly.append(literka)
            zle_strzaly.sort()
        print(f"Próbuj dalej masz {zycie} prób, użyte litery: {zle_strzaly}")
        sys.stdout.write("\033[K")
        continue
    else:
        print("Straciłeś wszystkie życia, koniec gry")
        break



