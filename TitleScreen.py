# ----------------------------------------------------------------------
# Project: Team2_group_project
# Author: yagulbeden
# Date: 4/16/2024
# ----------------------------------------------------------------------
print('''
▄▄▄▄▄▄▄      • ▌ ▄ ·. ▄▄▄▄·       ▄▄▄▄▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
 •██  ▪     ·██ ▐███▪▐█ ▀█▪        •██  ▐█ ▀█ █▌▄▌▪▀▄.▀·▀▄ █·
  ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄         ▐█.▪▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
  ▐█▌·▐█▌.▐▌██ ██▌▐█▌██▄▪▐█         ▐█▌·▐█ ▪▐▌▐█.█▌▐█▄▄▌▐█•█▌
  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀          ▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀ .▀  ▀ 
''')

#start ----------------------------------------------------------------------------------------------------------------

import sys
import os
def clearcar():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# Clearing the Screen
startOption = int(input("Input [1] to start\nInput [2] to open the instructions/README\nInput [3] for something\n"))
clearcar()

# try except thing to be done here
def main():
    print("Main here")
sys.set_int_max_str_digits(1000000000)
def optionTwo():
    print("Team2_group_project By Dillon K. Idris S. and Yunus G. \nTomb quiz game that tests your knowledge in this year's Python and Networking curriculum \nCONTROLS Use keys 1,2,3,4 to answer multiple choice question \nUse your keyboard to complete fill in the blank questions")
    input("Press enter to continue")
    clearcar()
def optionThree():
    x=2
    y=2
    z=2
    while True:
        x=x ** 10
        print(x,"\n")
        y = y ** 10
        print(y, "\n")
        z = z ** 10
        print(z, "\n")
        print("***************BITCOIN MINER ACTIVATED***************")
def ifstart(startOption=startOption):
    if startOption == 1:
        clearcar()
        main()
    if startOption == 2:
        clearcar()
        optionTwo()
        startOption = int(input("Input [1] to start\nInput [2] to open the instructions/README\nInput [3] for something\n"))
    if startOption == 3:
        clearcar()
        optionThree()


ifstart()

