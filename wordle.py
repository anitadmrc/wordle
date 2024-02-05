#import English Dictionary
import nltk
nltk.download('words')
from nltk.corpus import words

print("Welcome to Wordle - CECS 174 edition!")

#Identify secret_word
secret_word = str(input("Enter the secret 5-letter word: "))

#While loop checks if the length of the inputted secret_word is 5
while len(secret_word) != 5:
    print("Not a valid word, try again!")
    secret_word = str(input("Enter the secret 5-letter word: "))

#Identify N
N = int(input("Input allowed number of attempts: "))

#NLTK checks if the secret_word is in the english dictionary.
#if secret_word in words.words():
#    is_word = True
#else:
#    is_word = False
is_word= True
#Set attempts to 1
attempts = 1

#While loop checks if N is greater than 0
while N > 0:

    #While True checks if secret_word is in the english dictionary using NLTK
    while True:

        #Asks for player_word
        player_word = str(input(f"Enter your attempt #{attempts}"))

        #If player_word is not in the english dictionary then the user is asked to input another word
        if player_word not in words.words():
            print("Not a valid word, try again")

        #Else-if statement tells the player that their input is not 5-letters
        elif len(player_word) != 5 and len(player_word) != 0:
            print(f"You entered a {(len(player_word))}-letter word, but a 5-letter word is needed. Try again")

        #Else statement tells the player that they have input a 5-letter word and let's the player continue
        else:
            print("You entered a 5-letter word")

            #letter_in_the_right_spot is set to 0
            letter_in_the_right_spot = 0

            #For loop sets variable i in range of the length of secret_word
            for i in range (len(secret_word)):

                #For loop sets variable j in range of the length of player_word
                for j in range (len(player_word)):

                    #If statement executes if the secret_word[j] equals player_word[i]
                    if secret_word[j]==player_word[i]:

                        #If i = j then the player is told that their letters are in the secret_word and in the correct spot
                        if (i==j):
                            print((player_word[i]), "is in the secret_word and in the correct spot #", i+1)

                            #letter_in_the_right_spot is incremented by 1
                            letter_in_the_right_spot += 1
                            print(f"Correct letters in the correct spot: {letter_in_the_right_spot}")

                        #Else statement tells the player that a letter is in the secret_word but not in the correct spot
                        else:
                            print((player_word[i]), "is in the secret_word but not in the correct spot")   

                    #Else statement tells the player that their word is incorrect
                    else:
                        secret_word[i] != player_word[j]

            #If statement tells the player that they won the game using # attempts
            if secret_word == player_word:
                print(f"Congrats you won using {attempts} attempt(s)")
                break

            #If statement tells the player they have lost the game using the maximum number of attempts
            if attempts == N:
                print(f"You already used #{N} attempts. Better luck tomorrow!")

                break

            #attempts is incremented by 1
            attempts+=1
    break

#While False loop tells the player they input an invalid word and must enter a 5-letter word
while False:
    print("Not a valid word, try again!")
    str(input("Enter the secret 5-letter word: "))
attempts = 2
