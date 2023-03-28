# Cititor de CNP
# CNP-ul trebuie sa contina 13 cifre
#Cifrele se scriu intre ghilimele

def cititor_cnp(nume,prenume,cnp):
        if cnp[0] == 1 or 5 or 3 or 7:
            print(f"Domnul {nume} {prenume}")
            print("Sex masculin")
        elif cnp[0] == 2 or 6 or 4 or 8:
            print(f"Doamna {nume} {prenume}")
            print("sex feminin")
        # Cifrele 1 si 2 din CNP reprezinta ultimele 2 cifre din anul nasterii:
        if cnp[1] <= str(2):
            print("Anul nasterii : 20" + cnp[1] + cnp[2])
        else:
            print("Anul nasterii : 19" + cnp[1] + cnp[2])
        if cnp[0] == 3:
            print("anul nasterii : 18" + cnp[1] + cnp[2])
        if cnp[0] == 4:
            print("Anul nasterii : 18" + cnp[1] + cnp[2])
        # cifrele 3 si 4 din CNP reprezinta luna nasterii:

        digits_mapping = {
            "0" and "1": "Ianuarie",
            "0" and "2": "Februarie",
            "0" and "3": " Martie ",
            "0" and "4": " Aprilie ",
            "0" and "5": "Mai",
            "0" and "6": "Iunie",
            "0" and "7": "Iulie",
            "0" and "8": "August",
            "0" and "9": "Septembrie",
            "1" and "0": "Octombrie",
            "1" and "1": "Noiembre",
            "1" and "2": "Decembrie"
        }
        output = " "
        for ch in cnp[3] and cnp[4]:
            output += digits_mapping.get(ch) + ""
        print("Nascut in " + cnp[5] + cnp[6] + output)
        # Judetul
        # in functie de CNP ,cifrele 5 si 6.
        if cnp[7] == str(0) and cnp[8] == str(1):
            print("Domiciliat in Judetul Alba")
        if cnp[7] == str(0) and cnp[8] == str(2):
            print("Domiciliat in Judetul Arad")
        if cnp[7] == str(0) and cnp[8] == str(3):
            print("Domiciliat in Judetul Arges")
        if cnp[7] == str(0) and cnp[8] == str(4):
            print("Domiciliat in Judetul Bacau")
        if cnp[7] == str(0) and cnp[8] == str(5):
            print("Domiciliat in Judetul Bihor")
        if cnp[7] == str(0) and cnp[8] == str(6):
            print("Domiciliat in Judetul Bistrita-Nasaud")
        if cnp[7] == str(0) and cnp[8] == str(7):
            print("Domiciliat in Judetul Botosani")
        if cnp[7] == str(0) and cnp[8] == str(8):
            print("Domiciliat in Judetul Brasov")
        if cnp[7] == str(0) and cnp[8] == str(9):
            print("Domiciliat in Judetul Braila")
        if cnp[7] == str(1) and cnp[8] == str(0):
            print("Domiciliat in Judetul Buzau ")
        if cnp[7] == str(1) and cnp[8] == str(1):
            print("Domiciliat in Judetul Caras-Severin")
        if cnp[7] == str(1) and cnp[8] == str(2):
            print("Domiciliat in Judetul Cluj")
        if cnp[7] == str(1) and cnp[8] == str(3):
            print("Domiciliat in Judetul Constanta ")
        if cnp[7] == str(0) and cnp[8] == str(4):
            print("Domiciliat in Judetul Covasna")
        if cnp[7] == str(1) and cnp[8] == str(5):
            print("Domiciliat in Judetul Dambovita ")
        if cnp[7] == str(1) and cnp[8] == str(6):
            print("Domiciliat in Judetul Dolj")
        if cnp[7] == str(1) and cnp[8] == str(7):
            print("Domiciliat in Judetul Galati")
        if cnp[7] == str(1) and cnp[8] == str(8):
            print("Domiciliat in Judetul Gorj")
        if cnp[7] == str(1) and cnp[8] == str(9):
            print("Domiciliat in Judetul Harghita")
        if cnp[7] == str(2) and cnp[8] == str(0):
            print("Domiciliat in Judetul Hunedoara")
        if cnp[7] == str(2) and cnp[8] == str(1):
            print("Domiciliat in Judetul Ialomita")
        if cnp[7] == str(2) and cnp[8] == str(2):
            print("Domiciliat in Judetul Iasi")
        if cnp[7] == str(2) and cnp[8] == str(3):
            print("Domiciliat in Judetul Ilfov")
        if cnp[7] == str(2) and cnp[8] == str(4):
            print("Domiciliat in Judetul Maramures")
        if cnp[7] == str(2) and cnp[8] == str(5):
            print("Domiciliat in Judetul Mehedint")
        if cnp[7] == str(2) and cnp[8] == str(6):
            print("Domiciliat in Judetul Mures")
        if cnp[7] == str(2) and cnp[8] == str(7):
            print("Domiciliat in Judetul Neamt")
        if cnp[7] == str(2) and cnp[8] == str(8):
            print("Domiciliat in Judetul Olt")
        if cnp[7] == str(2) and cnp[8] == str(9):
            print("Domiciliat in Judetul Prahova")
        if cnp[7] == str(3) and cnp[8] == str(0):
            print("Domiciliat in Judetul Satu Mare")
        if cnp[7] == str(3) and cnp[8] == str(1):
            print("Domiciliat in Judetul Salaj")
        if cnp[7] == str(3) and cnp[8] == str(2):
            print("Domiciliat in Judetul Sibiu")
        if cnp[7] == str(3) and cnp[8] == str(3):
            print("Domiciliat in Judetul Suceava ")
        if cnp[7] == str(3) and cnp[8] == str(4):
            print("Domiciliat in Judetul Teleorman")
        if cnp[7] == str(3) and cnp[8] == str(5):
            print("Domiciliat in Judetul Timis")
        if cnp[7] == str(3) and cnp[8] == str(6):
            print("Domiciliat in Judetul Tulcea")
        if cnp[7] == str(3) and cnp[8] == str(7):
            print("Domiciliat in Judetul Vaslui")
        if cnp[7] == str(3) and cnp[8] == str(8):
            print("Domiciliat in Judetul Valcea")
        if cnp[7] == str(3) and cnp[8] == str(9):
            print("Domiciliat in Judetul Vrancea")
        if cnp[7] == str(4) and cnp[8] == str(0):
            print("Domiciliat in Judetul Bucuresti")
        if cnp[7] == str(4) and cnp[8] == str(1):
            print("Domiciliat in Judetul Bucuresti - Sector 1")
        if cnp[7] == str(4) and cnp[8] == str(2):
            print("Domiciliat in Judetul Bucuresti - Sector 2")
        if cnp[7] == str(4) and cnp[8] == str(3):
            print("Domiciliat in Judetul Bucuresti - Sector 3 ")
        if cnp[7] == str(4) and cnp[8] == str(4):
            print("Domiciliat in Judetul Bucuresti - Sector 4 ")
        if cnp[7] == str(4) and cnp[8] == str(5):
            print("Domiciliat in Judetul Bucuresti - Sector 5 ")
        if cnp[7] == str(4) and cnp[8] == str(6):
            print("Domiciliat in Judetul Bucuresti - Sector 6 ")
        if cnp[7] == str(5) and cnp[8] == str(1):
            print("Domiciliat in Judetul Calarasi")
        if cnp[7] == str(5) and cnp[8] == str(2):
            print("Domiciliat in Judetul Giurgiu ")
        pass
