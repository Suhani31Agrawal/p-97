import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances=0
print("Guess a number (between 1 and 9 ): ")

while chances < 5:

    guess=int(input("enter your guess:- "))

    if guess == number:
        print("CONGRATULATIONS YOU WON!")
        break
    
    elif guess < number:
        print("Your guess was too low: Guess a higher number than", guess)

    else:
        print("Your guessa was too high : Guess a number lower than", guess)

    chances +=1

    if not chances < 5:
        print("YOU LOSE!! The number is", number)
