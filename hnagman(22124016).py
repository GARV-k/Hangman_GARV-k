import random
from words import word_list

def obtain_word():
    word = random.choice(word_list)
    return word.upper()


def check_current_guess(word2guess, current_guess, guessed_letters, guess_count):
    if current_guess in guessed_letters:
        return -1
    else:
        if current_guess in word2guess:
            return 1
        else:
            return 0


def change_onscreen(onscreen, word2guess, current_guess):
    new_onscreen = "" * len(word2guess)
    for i in range(len(word2guess)):
        if current_guess == word2guess[i]:
            new_onscreen += current_guess
        else:
            new_onscreen += onscreen[i]    
    return new_onscreen     


def check_status(onscreen):
    if "_" in onscreen:
        return 0
    else:
        return 1
    
def action_on_guess(n, guessed_letters, current_guess, word2guess, guess_count, onscreen):
    if n == 1:
        print("You have made a right guess.")
        guessed_letters[current_guess] = 1
        onscreen = change_onscreen(onscreen, word2guess, current_guess)
        print(onscreen)
    elif n == -1:
        print("You have already guessed this letter! Guess another letter.")
        print(onscreen)
        print("Your remaining guesses are", guess_count)
    else:
        print("Your guess is incorrect.")
        guessed_letters[current_guess] = 0
        guess_count -= 1
        print(onscreen)
        print("Your remaining guesses are", guess_count)
    return onscreen


def startgame():
    word2guess = obtain_word()#"HAPPY" #i have made for a genralised word
    onscreen = "_" * len(word2guess)
    status = False
    guessed_letters = {}
    guess_count = 5
    print(onscreen)
    while guess_count > 0 and status != True:
        current_guess = input("Enter your guess letter: ").upper()
        guess_result = check_current_guess(word2guess, current_guess, guessed_letters, guess_count)
        onscreen = action_on_guess(guess_result, guessed_letters, current_guess, word2guess, guess_count, onscreen)

        if guess_result == 0:
            guess_count -= 1
     
        if check_status(onscreen) == 1:
            status = True
            print("You have successfully made it through. GAME OVER!")
        else:
            status = False


    if guess_count == 0 and status != True:
        print("Sorry you did not make it through. GAME OVER!")
        print("The word was:", word2guess)


startgame()