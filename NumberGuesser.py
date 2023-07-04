import random
difficulty = input("Do you want to play on hard or easy mode?: ")
if difficulty == "easy":
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    print(letter)
    answer = input("""Guess a random letter and i will tell you if you are right
But you only get one try so choose wisely: """)
    if answer == letter:
        print("\033[33m", "Whoa you guessed it right", "\033[31m", "I BET YOU CHEATED", "\033[0m")
    else:
        while answer != letter:
            print("\033[31m", "Nope this wasn't it try again", "\033[0m")
            answer = input("""Guess a random letter and i will tell you if you are right
But you only get one try so choose wisely: """)
            if answer == letter:
                print("\033[33m", "Whoa you guessed it right", "\033[31m", "I BET YOU CHEATED!!!", "\033[0m")
    input()
if difficulty == "hard":
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    print(letter)
    answer = input("""Guess a random letter and i will tell you if you are right
But you only get one try so choose wisely: """)
    if answer == letter:
        print("\033[33m", "Whoa you guessed it right", "\033[31m", "I BET YOU CHEATED", "\033[0m")
    else:
        while answer != letter:
            print("\033[31m", "Nope this wasn't it try again", "\033[0m")
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            print(letter)
            answer = input("""Guess a random letter and i will tell you if you are right
But you only get one try so choose wisely: """)

            if answer == letter:
                print("\033[33m", "Whoa you guessed it right", "\033[31m", "I BET YOU CHEATED!!!", "\033[0m")
    input()