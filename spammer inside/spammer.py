#I DID NOT make the spammer bot, the is some that is original and the rest I moddifed, please watch MaxCodez video on it, it's simple and easy.

import pyautogui, time, os

print('This bot is for spamming people with text from text documents')

#asks for the movie you want. You need the .txt files in the same folder as the Spammer.py file.
movie = input('What movie\n(A)Bee Movie\n(B)Shrek The Third\n(C)schindlers list\nTo Quit Type Quit\n')

#Quit.
if movie == 'Quit':
    os._exit(1)

#input an amount of time you want it to run for, be careful the is no stopping after it starts unless you close this screen with the X icon top right.
count = int(input('Input how long for: '))

#bee movie
if movie == 'A':
    print("Spammer will start in seconds...")
    time.sleep(4)
    pyautogui.typewrite('Hey! <Person> have something to tell you!!')
    pyautogui.press("enter")
    f = open("beemovie.txt", 'r')
    for word in f:
        time.sleep(2)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        #this is the count down till it stops.
        count = count - 1
        print(count)
        if count == 0:
            print('The Bot is finished')
            break

#shrek the third
if movie == 'B':
    print("Spammer will start in seconds...")
    time.sleep(4)
    pyautogui.typewrite('Hey! <Person> have something to tell you!!')
    pyautogui.press("enter")
    f = open("stt.txt", 'r')
    for word in f:
        time.sleep(2)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        #this is the count down till it stops.
        count = count - 1
        print(count)
        if count == 0:
            print('The Bot is finished')
            break

#schindlerslist
if movie == 'C':
    print("Spammer will start in seconds...")
    time.sleep(4)
    pyautogui.typewrite('Hey! <Person> have something to tell you!!')
    pyautogui.press("enter")
    f = open("sl.txt", 'r')
    for word in f:
        time.sleep(2)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        #this is the count down till it stops.
        count = count - 1
        print(count)
        if count == 0:
            print('The Bot is finished')
            break
