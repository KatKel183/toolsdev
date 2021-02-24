import random

game_running = True


def secret_numbers():
    three_numbers = random.sample(range(1, 11), 3)
    if user_input == str(three_numbers[0]):
        print("Yes! You guessed " + user_input + " and it was " +
              str(three_numbers))
    elif user_input == str(three_numbers[1]):
        print("Yes! You guessed " + user_input + " and it was " +
              str(three_numbers))
    elif user_input == str(three_numbers[2]):
        print("Yes! You guessed " + user_input + " and it was " +
              str(three_numbers))
    else:
        print("Sorry, you guessed " + user_input + " but I was thinking of "
              + str(three_numbers))


print("I'm thinking of three numbers between 1 and 10.")

while game_running:
    user_input = input("Guess one of the three to win! ")
    if user_input == 'q':
        print("game over!")
        break
    secret_numbers()
    print("--If you're done, press q--")
    print(" ")
    print("I'm choosing three new numbers from 1 to 10! Guess one.")
