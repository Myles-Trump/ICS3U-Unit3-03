#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user guess a number between 1-10
#    with a randomized integer and tells them if they are correct or not


import random


def main():
    # this function lets the user pick a number between 1-10
    #   and randomizes said number

    # input
    guess = int(input("Guess an integer between 1-10: "))
    print("")
    randomized_number = random.randint(1, 10)  # a number between 1-10

    # process & output
    if guess == randomized_number:
        print("You are correct")

    else:
        print("You are not correct, the answer was {0}"
              .format(randomized_number))

    print("\nDone")


if __name__ == "__main__":
    main()
