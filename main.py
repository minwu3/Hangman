import random
import hangman_art
import hangman_words
# make every guess clear
from replit import clear


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)

#Create blanks
answer = []
for _ in range(0, word_length):
    answer += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
   

    #Check guessed letter
    for i in range(0, word_length):
        letter = chosen_word[i]
      
        if letter == guess:
            answer[i] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        print(f"the letter {guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The answer is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(answer)}")

    #Check if user has got all letters.
    if "_" not in answer:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])
