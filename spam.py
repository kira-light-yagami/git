import pyautogui
print("step#1: make sure to open the application where you wanted to spam and be sure to select were and click on the writing box ")
print("caution : Only the program and the app where you wanted to spam should be open close all unnessery apps the program may do something else")
y=int(input("how many times do you want to spam your msg:"))
d=input("tell me what you want to spam :")
pyautogui.hotkey("alt","tab")
for x in range(y):
    pyautogui.typewrite(d,interval = 0.1),pyautogui.hotkey("enter")














































