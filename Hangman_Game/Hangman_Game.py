import random
from hangman_art import stages,logo
from hangman_words import word_list

print(logo)
word_guess=random.choice(word_list)
word_length=len(word_guess)
# print(word_guess)
placeholder=""
for i in range(word_length):
    placeholder+="_"
print(placeholder)
correct_letters=[]
lives=6

game_over=False

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess=input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You already guessed this letter. Try a different letter")
        continue
    correct_letters.append(guess)

    if guess not in word_guess:
        lives-=1
        print("You guessed a wrong letter. You lost a life")
        print(f"You have {lives} lives left")
        if lives == 0:
            print(f"The word was {word_guess}")
            print("You lost all your lives. Game Over")
            game_over = True




    display = ""
    for letter in word_guess:
        if letter==guess:
            correct_letters+=letter
            display+=letter
        elif letter in correct_letters:
            display+=letter

        else:
            display+="_"

    if "_" not in display:
        print("Congrats. You win!")
        print("Thanks for playing")
        break

    print(stages[lives])
    print(display)