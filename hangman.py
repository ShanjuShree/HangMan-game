#HANGMAN  GAME
#importing random module
import random
words = ['ANT','APPLE','AIEPLANE','BALL','BAT','BUNNY','CAT','CAGE','CUNNING',
          'DEER','DECADE','DEMONSTRATE','FISHING','FINE','FOLLOW','GOOD','GAME',
          'GHJIK','HELLO','HI','ICE','JOKER','KING','KNIGHT','KANGROO','KNIFE','LAVENDER','LEMON',
          'LEGIT','MONEY','MANGO','MESSAGE','NEST','NAVIGATION','NATIVE','ORGANISM','ORANGE','PASSAGE',
          'PARENT','POSSESSIVE','QUEEN','RESISTANCE','RAMBO','RACE','SPECIMEN','SPOTIFY','SPECIAL','TABLET',
          'TRAVELLING','TRANSITIVE','UMBRELLA','ULTIMATE','VERSATILE','VARIABLE','VINTAGE','WELCOME','WATERMELON',
          'WASABI','XEROX','XMAS','XAVIER','YELLOW','YUMMY','YACHT','ZERO','ZOMATO','ZOO']
from wordlist import wordlist

#function to get a secret word from the wordlist

def inputword(wordist):

    length=len(wordlist) - 1
    #random words are generated from the wordlist
    #random index are generated for this list
    word_len= random.randint(0, length) 
    return wordlist[word_len]

#Getting the players guess
def Guess(previously_guessed):
    while True:
        #getting the guess
        guess = input("\nGUESS A LETTER:")
        
        #converting the guess into upper
        
        guess = guess.upper()

        alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #making sure they input a single character
        if len(guess) != 1:
            print("DO ENTER A SINGLE LETTER...TRY AGAIN!!!")
        elif guess not in alphabets:
            print("ENTER A PROPER LETTER....")
        elif guess in previously_guessed:
            print("YOU HAVE GUESSED THE LETTER ALREADY,,,CHOOSE A LETTER AGAIN :)")
        else:
            return guess
hangman_board= ['''
  -----
    |
    |
    |
  *****''', '''
  -----
    O   |
        |
        |
      *****''', '''
  -----
    O   |
    |   |
        |
      *****''', '''
  -----
    O   |
   /|   |
        |
       *****''', '''
  -----
    O   |
   /|\  |
        |
       *****''', '''
  -----
    O   |
   /|\  |
   /    |
       *****''', '''
   -----
    O   |
   /|\  |
   / \  |
       *****''']

#To display to the hangman board
#displays how many correct and incorrect guesses by the player
def hangman_Board(letter_miss, correct, secretword):
    print(hangman_board[len(letter_miss)])

    #displays the missing spaces to be filled
    print("\nLETTERS MISSED ARE:", end=" ")
    for letter in letter_miss:
        print(letter, end=" ")
    print()


    l= len(secretword)
    #blank has the same number of underscores as the secretword has letters
    empty = "_" * l

    #loop goes through each letter in secretword and replace the underscore with the letter if it exits.
    for i in range(l): 
        if secretword[i] in correct:
            empty = empty[:i] + secretword[i] + empty[i+1:]

    #displaying the secret word with spaces in between     
    for letter in empty:
        print(letter, end=' ')
    print()

#Asking the player if they want to replay the game or not       
def replay():
    play=input("Do you want to play the game again? ('Y' for yes or 'N' no)")
    convert_upper=play.upper()
    check=convert_upper.startswith("Y")
    return check

#Game

print("\n                HEYYY THERE!!! WELCOME TO HANGMAN                 \n ")
print("      RULES FOR HANGMAN                 ")
print("\n   1.Start guessing the secret word if you are the player")
print("\n   2.Find the secret word letter by letter")
print("\n   3.For each incorrect guess the man will get slowly hanged :(")
print("\n   4.You win the game if you choose all the letters of the secret word ;) \n")
print("\n         GUESS THE WORD BEFORE YOUR MAN GETS HUNG!!! GOOD LUCK...\n")
print("\n               ...............LETS START PLAYING.............            \n")
print("\n                ***********H   A   N  G  M   A   N*************          \n")       

#blank strings assigned to miss and correct as the user didnt give any guess
letter_miss = " "
correct = " "
#selects random word from the word list
secretword = random.choice(words)
gameover = False

#calling the hangman function
while True:
    hangman_Board(letter_miss, correct, secretword)
    guess = Guess(letter_miss+ correct)

    #check if the letter is in the secret word
    if guess in secretword:
        correct= correct + guess

        #check if the player won
        letter_found = True
        for i in range(len(secretword)):
            if secretword[i] not in correct:
                letter_found = False
                break
        if letter_found:
            print("YAYYYY!!! YES THE SECRET WORD IS " + secretword +"!\n CONGRATS!!! You have won!\n")
            gameover = True
    else:
         letter_miss = letter_miss + guess
         #checking if player has guessed many times and lost
         len_hang=len(hangman_board) - 1
         if len(letter_miss) == len_hang:
             hangman_Board(letter_miss, correct, secretword)
             print("YOU RAN OUT OF GUESSES...!\n ")
             print("YOU HAD "+str(len(letter_miss)) + "  incorrect guess and  " +str(len(correct)) + " correct guesses \n")
             print("THE WORD IS :", secretword)
             gameover = True

#asking the player if the wanted to replay the game(if the game is over)
    if gameover:
        if replay():
            letter_miss = " "
            correct = " "
            gameover = False
            secretword = inputword(words)
        else:
             print("OKAY!!! THANKS FOR PLAYING..")
             break