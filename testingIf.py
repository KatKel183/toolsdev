import random

game_running = True


def secret_numbers():
    three_numbers = random.sample(range(1, 11), 3)

    if user_input == (str(three_numbers[0]) or str(three_numbers[1])
                      or str(three_numbers[2])):
        print("Yes! you guessed " + str(user_input) + " and I was thinking of "
              + str(three_numbers))
    else:
        print("you guessed " + str(user_input))
        print("Sorry, I was thinking of " + str(three_numbers))
    print("--If you're done, press q--")
    print(" ")
    print("I'm choosing three new numbers from 1 to 10! Guess one.")


print("I'm thinking of three numbers between 1 and 10.")

while game_running:
    user_input = input("Guess one of the three to win! ")
    if user_input == 'q':
        print("game over!")
        break
    secret_numbers()
