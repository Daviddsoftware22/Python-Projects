import random

def creator_de_parola(parola):
    parola_output = []
    cifre_output = []
    numere_curate = []
    incercari_introduse = 0
    incercari_maxime = 3
    toate_numerele_intregi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for ch in parola:
        parola_output.append(ch)
        for numere in parola_output:
            if numere in toate_numerele_intregi:
                cifre_output.append(numere)
            for dubluri in cifre_output:
                numere_curate.append(dubluri)
    nr_cifre = len(numere_curate)
    nr_caractere_parola = len(parola)

    if nr_cifre <= 2:
        print("Parola trebuie sa contina cel putin 3 cifre ")
    if nr_caractere_parola < 10:
        print("Parola trebuie sa contina cel putin 10 caractere, ati introdus o parola prea scurta")
    if nr_caractere_parola > 16:
        print("Parola trebuie sa contina cel mult 15 caractere, ati introdus o parola prea lunga")
    if nr_caractere_parola == 13 and nr_cifre >= 3:
        print("Medium")
        print(f"Parola dvs este {parola}")
        incercari_introduse = 3

    if nr_caractere_parola < 13 and nr_cifre >= 3:
        print("Low")
        print(f"Parola dvs. este {parola}")
        incercari_introduse = 3
    if nr_caractere_parola > 13 and nr_cifre >= 3:
        print("Strong")
        print(f"Parola dvs este {parola}")
        incercari_introduse = 3

    while incercari_introduse < incercari_maxime:
        parola1 = input("Introduceti parola: ")
        parola_output2 = []
        numere_output2 = []
        numere_curate2 = []
        incercari_introduse = incercari_introduse + 1
        toate_numerele_intregi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for ch1 in parola1:
            parola_output2.append(ch1)
            for numere in parola_output2:
                if numere in toate_numerele_intregi:
                    numere_output2.append(numere)
                for dubluri in numere_output2:
                    numere_curate2.append(dubluri)
        nr_caractere_parola = 0 + len(parola1)
        incercari_introduse += 1
        if nr_cifre <= 2:
            print("Parola dvs. trebuie sa contina cel putin 3 cifre ")
        if nr_caractere_parola < 10:
            print("Parola dvs. trebuie sa contina cel putin 10 caractere, ati introdus o parola prea scurta")
        if nr_caractere_parola > 16:
            print("Parola dvs. trebuie sa contina cel mult 15 caractere, ati introdus o parola prea lunga")
        if nr_caractere_parola == 13 and nr_cifre >= 3:
            print("Medium")
            print(f"Parola dvs este {parola1}")
            break
        if nr_caractere_parola < 13 and nr_cifre >= 3:
            print("Low ")
            print(f"Parola dvs. este {parola1}")

            break
        if nr_caractere_parola > 13 and nr_cifre >= 3:
            print("Strong")
            print(f"Parola dvs este {parola1}")
            break
