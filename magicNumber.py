import random

def selectDifficult():
    print('MAGIC NUMBER \n\nThe player must guess the number to win with 5 tries\n\n')
    difficult = 0
    error = 0
    while error < 3:
        try:
            difficult = int(input('Choose a difficult: 1.Easy, 2.Hard, 3.Insane\n'))
            if difficult == 1:
                print('Try a number between 1 to 10')
                return 10
            elif difficult == 2:
                print('Try a number between 1 to 50')
                return 50
            elif difficult == 3:
                print('Try a number between 1 to 100')
                return 100
            else:
                difficult = 0
                error += 1
        except (NameError, SyntaxError):
            print('Please, choose a valid difficult')
            error +=1
    if error == 3:
        exit()

def start(maxRange):
    error = 5
    foundNumber = False

    number = random.randint(1,max)
    while error != 0 | foundNumber == False:
        try:
            n = int(input('\nPick number: '))
            if n == number:
                foundNumber = True
            elif n < number:
                print('Try a higher number')
            elif n > number:
                print('Try a lower number')
            error -= 1
        except (NameError, SyntaxError):
            error -= 1
            print('Invalid number :/')
        
    if foundNumber:
        print('\nYou win :D')
    else:
        print('\nYou fail, the number was '+ str(number) +' :(')

if __name__ == "__main__":
    max = selectDifficult()
    start(max)


