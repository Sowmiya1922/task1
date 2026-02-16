
import random
num =random.randint(1,10)
no_attempts =0
print("Guess a number between 1 and 10")

while True:
    guess = int (input("Enter your guess number :  "))
    no_attempts += 1

    if guess > num:
        print ("your guessing number is higher than the number !!")

    elif guess < num:
        print("your guessing number is lower than the number !!")

    else:
        print(f"Correct !! You guessed the number in {no_attempts} attempts .")
        break
