import random

print("well, we met again, today I want you to play a game with me, you need to guess a number that I chose ")
number_choice = input("up to what number can i choose?")

if number_choice.isdigit() :
    number_choice = int(number_choice)

    if number_choice <= 0 :
        print("Choose number larger than 0 next time")
        quit()
else:
    print("I already told you that you need to write a number ")
    quit()

number_generator = random.randint(0,number_choice)
number_guesses = 0
while True:
    number_guesses += 1
    number_choice = input("Make a guess: ")
    if number_choice.isdigit():
        number_choice = int(number_choice)
    else:
        print("I already told you that you need to write a number ")
        continue

    if number_choice == number_generator:
        print("yay my code is working(I mean yay you got it)")
        break
    elif  number_choice > number_generator :
               print("the number that you're looking for is smaller")
    else:
               print("the number that you're looking for is bigger")
print("you got it in " , number_guesses , " times")