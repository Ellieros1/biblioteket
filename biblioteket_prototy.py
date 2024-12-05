# ------------------------------- Information --------------------------------- #
"""
Titel: Biblioteket
Författare:
Datum:
Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

# ---------------------------- Klassdefinitioner ------------------------------ #

class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    def __init__(self, författare, titel):
        self.titel = titel
        self.författare = författare
        self.utlånad = False

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Boken {self.titel}, skriven av {self.författare}."

class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, boklista=[]): #sätter ett bibliotek ojekt med en lista av böcker som en standard
        self.böcker = boklista

    # Sparar hela bibliotekskatalogen i en fil.
    def spara(self, filename="Programmering/Författare_böckerpy.txt"):
        with open(filename, "w") as f: #öppnar filen med namnet "filename" i skrivläge och tilldelar filobjektet "f"
        for bok in self.böcker: #loppar igenom varje bok i listan "self.böcker"
            f.write(f"{bok.författare},{bok.titel},{bok.utlånad}\n") #Skriver boken författare, titel och om den är utlånad eller inte (alla är återskillda med kommatecken)
        return

    # Söker på en titel.
    def hittaTitel(self, titel):
        return []

    # Söker på en författare.
    def hittaFörfattare(self, författare):
        return

    # Lånar en bok.
    def lånaBok(self, bok):
        return

    # Återlämnar en bok.
    def lämnaTillbaka(self, bok):
        return

    # Lägger till en ny bok:
    def läggTill(self, bok):
        return

    # Tar bort en bok:
    def taBort(self, bok):
        return

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    Bibliotek = open("Programmering/Författare_böckerpy.txt")
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:
            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok
            7. Lista alla böcker                                8. Sortera böcker
                                        q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
           str(titel = input("ange titel: ")) #ber användaren att skriva in titel
           resultat = Bibliotek.hitta_titel(titel) 
           for bok in resultat:
               print(bok) #Skriver ut boken
        elif menyVal == "2":
            str(författare = input("ange författare: ")) #ber användaren att skriva in författaren
            resultat = Bibliotek.hitta_författare(författare)
            for bok in resultat: print(bok) #Skriver ut boken
        elif menyVal == "3":
            str(title = input("ange boken du vill låna: ")) #ber användaren att skriva in  boken som den vill låna
            print(Bibliotek.låna_bok(titel)) 
        elif menyVal == "4":
            str(titel= input("ange titel på boken du vill återlämna: ")) #Sber användaren att skriva in boken den vill återlämna
            print(Bibliotek.lämna_tillbaka(titel)) 
        elif menyVal == "5":
            författare = input("Ange författaren: ") #ber användaren att skriva in skriva in författren
            titel = input("Ange titeln på den nya boken: ")
            print(Bibliotek.lägg_till_bok(författare, titel))
        elif menyVal == "6":
            titel = input("Ange titeln på boken du vill ta bort: ")  #ber användaren att skriva in boken den vill ta bort
            print(Bibliotek.ta_bort_bok(titel))
        elif menyVal == "7":
            böcker = Bibliotek.listaBöcker() #
            for bok in böcker:
                print(bok)
        elif menyVal == "8":
            print("Avslutar programmet") #Skriver ut "Avslutar programet"

print(
"""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

main()