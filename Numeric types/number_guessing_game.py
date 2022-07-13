import random
answer = random.randint(0, 100)
while True:
    user_guess = int(raw_input("What is your guess? "))
    if user_guess == answer:
        print("Right!  The answer is {0}".format(user_guess))
        break
    elif user_guess < answer:
        print("Your guess of {0} is too low!".format(user_guess))
    elif user_guess > answer:
        print("Your guess of {0} is too high!".format(user_guess))
