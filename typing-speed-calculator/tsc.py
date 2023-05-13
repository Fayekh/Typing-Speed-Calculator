from time import *
import random as r
from texts import lines


text_p = r.choice(lines)

def mistake(qtext, userText):
    error = 0
    len_qtext = qtext.count(" ")+1
    for i in range(len_qtext):
        try:
            if qtext[i] != userText[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_round = round(time_delay, 3)
    len_userinput = userinput.count(" ")+1
    speed = len_userinput/ time_round
    return round(speed,3)



while True:
    print("\n***Typing Speed Calculator by MAF***")
    print()
    readychecker = input("Press 'R/r' if you are ready: ")
    if readychecker == "r" or readychecker == "R":
        print("\n")
        print(text_p)
        print()
        time_1 = time()
        userTextInput = input("Type (Press Enter after finishing): ")
        time_2 = time()
        print()
        speed = speed_time(time_1, time_2, userTextInput)
        mistakes = mistake(text_p, userTextInput)
        no_space_userText = userTextInput.replace(" ","")
        if no_space_userText == '' or mistakes >= 52:
            score = 0
            speed = 0
        elif mistakes != 0:
            score = round(100*(speed/ mistakes), 2)
        else:
            score = speed/ 1 
        print("Speed: ", speed, " word(s)/sec   ||   ", round((speed*60), 2), " word(s)/minute")
        print()
        print("Mistakes: ", mistakes)
        print()
        print("Score: ", score, "\n")
        print("\n")
        again = input("Run again? (y/n) ")

        if 'y' in again:
            continue
        elif 'Y' in again:
            continue
        elif 'n' in again:
            break
        elif 'N' in again:
            break
        else:
            print("Invalid Input. Pogram started again.")


