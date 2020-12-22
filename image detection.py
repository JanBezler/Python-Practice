from pyautogui import *
import pyautogui
import time

file_path_splitted = __file__.split("/")[0:-1]
file_path = ""
for item in file_path_splitted:
    file_path += item+"/"


while 1:
    located = pyautogui.locateOnScreen(
        file_path+'Nurse.png', grayscale=False, confidence=0.60)
    if located != None:
        print(f"Located at: {located[0]+located[2]/2,located[1]+located[3]/2}")

    else:
        print("I am unable to see it")
    time.sleep(1)
