import pyautogui, time
time.sleep(5)
file = open("spam.txt", 'r')

for words in file:
    pyautogui.typewrite(words)
    pyautogui.press("enter")