import random
javab = random.randint(1,99)
x = int(input('Guess a two-digit number: '))
while x!= javab:
    if x > javab:
        print('You guessed a big number')
        x = int(input('Guess the smaller number: '))
    else:
        print('You guessed a small number')
        x = int(input('Guess the bigger number: '))
print('Hooray!')