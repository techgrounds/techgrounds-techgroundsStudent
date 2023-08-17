# Dit is mijn versie van opdracht 9, vooral mogelijk gemaakt door CHATGPT ivm kennisneming van alle materie mijner zijds.
# Toch is hier en daar een persoonlijke touch te zien. s
import random

def JEU():
    # Genereer een willekeurig getal tussen 1 en 100
    target_number = random.randint(1, 100)
    
    # Initialisatie van het aantal pogingen en het spel
    attempts = 0
    guessed = False
    
    print("Raad het nummer tussen 1 en 100!")

    while not guessed:
        # Vraag de speler om een gok
        guess = int(input("Doe een gok: "))
        
        # Verhoog het aantal pogingen
        attempts += 1
        
        # Controleer of de gok juist is
        if guess == target_number:
            guessed = True
            print(f"Goed geraden! Het nummer was {target_number}. Aantal pogingen: {attempts}")
        else:
            # Geef een aanwijzing aan de speler
            if guess < target_number:
                print("Probeer een hoger nummer.")
            else:
                print("Probeer een lager nummer.")

if __name__ == "__main__":
    JEU()
    JEU()
    JEU()
print("Nu is het wel genoeg")
'''
Chat GPT gebruikt om te zien hoe deze opdracht voltooid kan worden.
Hierdoor kennis gemaakt met __name__ == "__main__" leerstuk. 
Verder door peer to peer learning de overweldigende kracht van de F-string ingezien. 
'''
