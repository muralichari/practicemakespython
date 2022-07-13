total = 0
attempts = 0

while True:
        try:
                minutes = input('Please enter the time in minutes for your 10 km run or Enter to quit : ')
                if minutes != '':
                        attempts += 1
                        total += float(minutes)
                else:
                        average = total/attempts
                        print(f'The average time for your 10 km run is {average}')
                        break
        except ValueError as e:
                print("Sorry, that's not a valid number. Try again!")

