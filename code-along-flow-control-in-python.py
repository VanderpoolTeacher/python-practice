# declare and assign our variables
our_number = 42
guess = None
quit = False

# main while loop
while quit == False:

# while loop for guessing and comparing numbers
    while guess != our_number:

        guess = int(input('Enter an interger: '))

        if guess == our_number:
            print('Yeah! First try :)')
        elif guess > our_number:
            print('Too high!')
        elif guess < our_number:
            print('Too low!')

# if statement - do you want to play again
    play_again = input("Do you want to play again? Y/N")

    if play_again == "Y" or play_again == "y":
        print("Let's play again!")
        guess = None
    elif play_again != "Y":
        quit = True
        print("Thank you for playing! See you again soon!")