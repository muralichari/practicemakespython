import random
number = random.randint(0,100)

while 1:
        answer = input('Enter a number between 0 and 100 inclusive > ')
        if int(answer) == number:
                print('You guessed it right!')
                break
        elif int(answer) < number:
                print(f'Your guess {answer} is less than the answer. Try again!')
        else:
                print(f'Your guess {answer} is more than the answer. Try again!')

print(f'The magic number was {number}')
