import random
import time
while True:
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
    print("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n4. Exit")
    game = input("\nEnter your choice: ")
    if game == "1":
        random_number = random.randint(1,100)
        print(f"Great! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        for i in range(10):
            choice = int(input("Enter your guess:"))
            if choice == random_number:
                print(f"You guessed correctly in {i + 1} attempts.")
                time.sleep(0.5)
                break
            elif choice < random_number:
                print(f"Incorrect! The number is greater than {choice}.")
            elif choice > random_number:
                print(f"Incorrect! The number is less than {choice}.")
        else:
            print("You have used up all your attempts.")
            time.sleep(1)
    elif game == "2":
        random_number = random.randint(1, 100)
        print(f"Great! You have selected the Medium difficulty level.")
        print("Let's start the game!")
        for i in range(5):
            choice = int(input("Enter your guess:"))
            if choice == random_number:
                print(f"You guessed correctly in {i + 1} attempts.")
                time.sleep(0.5)
                break
            elif choice < random_number:
                print(f"Incorrect! The number is greater than {choice}.")
            elif choice > random_number:
                print(f"Incorrect! The number is less than {choice}.")
        else:
            print("You have used up all your attempts.}")
            time.sleep(1)
    elif game == "3":
        random_number = random.randint(1, 100)
        print(f"Great! You have selected the Hard difficulty level.")
        print("Let's start the game!")
        for i in range(3):
            choice = int(input("Enter your guess:"))
            if choice == random_number:
                print(f"You guessed correctly in {i + 1} attempts.")
                time.sleep(1)
                break
            elif choice < random_number:
                print(f"Incorrect! The number is greater than {choice}.")
            elif choice > random_number:
                print(f"Incorrect! The number is less than {choice}.")
        else:
            print("You have used up all your attempts.")
            time.sleep(1)
    elif game == "4":
        print("Thanks for playing!")
        break


