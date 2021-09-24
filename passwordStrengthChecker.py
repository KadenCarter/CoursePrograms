# This program will return the time in which it would take for a computer to crack a 4 character password
# It does this by taking an input from the user and then checking to make sure that the user only
# entered 4 characters that are only letters and numbers. It then compares the password with a guess and
# if the password and the guess match the password is printed back to them along with the time it took to crack it.

import time

# used for calculating time.
def current_milli_time():
    return round(time.time() * 1000)

# main method
def main():
    
    # takes an input from the user and stores it in the "password" variable.
    password = input(">>Input a 4-pin password. Only numbers and letters (case-sensitive) are allowed.:")

    # checks to see if "password" has a length of 4 or not.
    if len(password) != 4:
        print("Your password must be 4 characters long.")
    else:

        #checks if "password" is only using letters and numbers or not.
        if password.isalnum() == False:
            print("You must only use letters and numbers.")
        else:
            # string with all alphanumerical values case sensitive.
            charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

            # starts the timer
            start = current_milli_time()

            # loops through the "charSet" string and makes a guess at each iteration.
            for i in charSet:
                for j in charSet:
                    for k in charSet:
                        for l in charSet:
                            passGuess = i + j + k + l
                            if passGuess == password:
                                print(passGuess)
                                end = current_milli_time()
                                print("Your password can be cracked in: " + str(end - start) + "ms")
                                break

main()

