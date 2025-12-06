def check_answer(user_input, actual_answer, turns):
        if user_input < actual_answer:
            print("too low")
            return turns - 1
            print(f"you  have {attempt} attempt left")
        elif guess > number:
            print("too high")
            return turns - 1
            print(f"you  have {attempt} attempt left")
        elif guess == number:
            print(f"you are right, you guessed {number}")
            return
        check_answer(user_input = guess, actual_answer= number, turns = round())
print("welcome to the guessing game number")
print("im thinking of a number between 1, 100")
import random
number = random.choice(range(1, 100))
guess = " "
game_difficulty = input("choose a difficulty.Type 'easy' or 'hard'")
EASY_TURN = 9
HARD_TURN = 5
def round():
    if game_difficulty == 'easy':
        return EASY_TURN
    elif game_difficulty == 'hard':
        return HARD_TURN
    round()
game_over = True
turns = round()
while guess != number:
    print(f"you have {turns} attempt left for this game")
    guess = int(input("make a guess"))
    turns = check_answer(guess, number,turns)
    if guess != number:
        print("guess again")
    elif turns == 0:
        print("you've run out of guesses, you lose ")
        game_over = False






