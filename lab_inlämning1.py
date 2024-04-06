

# hang man med färger
import random


# funktion som randomiserar ett ord från en lista
def choose_word():
    spelord = ["röd", "blå", "grön", "gul", "lila", "orange", "rosa", "brun", "cyan", "magenta", "vinröd", "guld", "svart", "vit"]
    return random.choice(spelord)


# funktion som avgör hur ordet ska visas.
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


# funktion som avgör om alla bokstäver i ordet finns bland de bokstäver spelaren gissat.
def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


# huvudfunktionen som samlar funktionerna skapade ovan till "spelfunktionen".
def hangman():
    word = choose_word() # tillskriver variabeln word det slumpmässigt valda ordet via funktionen.
    guessed_letters = [] # initialt en tom lista, som kommer fyllas på vid varje försök i spelet.
    attempts = 6 # välj antal försök spelaren ska ha

    print("\n\nÄr du redo för Hänga gubben?")
    print("Ordet vi söker är en färg, det är", len(word), "bokstäver långt.")  # Utskrift av antalet bokstäver i ordet

    while attempts > 0:
        print("\n:", display_word(word, guessed_letters)) # använder funktionen för att visa ordet.
        print("\n Antal försök kvar:", attempts) # 
        guess = input("Gissa en bokstav som finns i ordet: ").lower() # input som tar emot gissning, och formaterar till gemener.

        if len(guess) != 1 or not guess.isalpha(): # kontroll om input är längd 1
            print("Du kan bara gissa en bokstav i taget.")
            continue

        if guess in guessed_letters:
            print("Du har redan gissat den bokstaven.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Den bokstaven finns inte tyvärr.")
            attempts -= 1 # här räknas försöken ned, om bokstaven inte finns med i ordet.
        else:
            print("Yippie! - jackpot!")

        if is_word_guessed(word, guessed_letters): # så länge antal försök är större än 0, kolla om det lyckats gissa rätt ord via funktion.
            print("\nGrattis! du lyckades gissa rätt ord!", word)
            break

    if attempts == 0: # om försök = 0, game over!
        print("\nSorry mate, spelet är över! - ordet vi sökte var:", word)

if __name__ == "__main__":
    hangman()
