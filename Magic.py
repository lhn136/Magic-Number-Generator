# Write code clearer practice

import random

# Generate 2 random number in a list
magic_numbers = [random.randint(0,9),random.randint(0,9)]

def user_input_conditional_check():
    user_number = int(input("Enter a number between 0 and 9: "))
    # print(magic_numbers[0], "  " ,magic_numbers[1]);
    if user_number in magic_numbers:
        print ("You got the number right!")
    if user_number not in magic_numbers:
        print( "You didn't quite get it.")

def run_program_n_times(chances):
    for attempt in range(chances):
        print("This is attempt {}".format(attempt))
        user_input_conditional_check()

if __name__ == '__main__':
    user_attempts = int(input("How many rounds?"))
    print(run_program_n_times(user_attempts))