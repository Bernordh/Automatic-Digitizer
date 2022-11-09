import time
import cv2
import pytesseract
import keyboard
import pyautogui
import os

def type(fixedtext):
    for character in fixedtext:
        time.sleep(0.01)
        keyboard.write(character)
    os.remove("images\image.png")

def fix_issues(result):
    newresult = result.replace(".", ". ")
    newresult = newresult.replace("|", "I ")
    newresult = newresult.replace(",", ", ")
    return(newresult)

    

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

print("The program will take the print in 3 seconds, go to the typeracer screen")
time.sleep(2)

screenshot = pyautogui.screenshot(region=(1226, 384, 407, 129))
screenshot.save("Image output path")
time.sleep(1)

img = cv2.imread("images\image.png")
result = pytesseract.image_to_string(img)
fixedtext = fix_issues(result)
type(fixedtext)