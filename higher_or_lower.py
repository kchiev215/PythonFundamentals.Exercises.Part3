from random import randrange
print(randrange(10))
print(randrange(10))
#Randomly generates a number from 0-10

randomNumber = randrange(1, 11)
print("Guess a number I am thinking of between 0-10")
userGuess = 0
while randomNumber != userGuess:
    userGuess = int(input())
    if userGuess > randomNumber:
        print("too high")
    elif userGuess < randomNumber:
        print("too low")
    elif userGuess == randomNumber:
        print("ding "*3)
        print("Thanks for playing")
        break;
