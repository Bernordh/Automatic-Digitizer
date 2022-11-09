# Automatic-Digitizer

<p align="center">
  <img width="500" height="500" src="https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/TypeRacer_logo.svg/1200px-TypeRacer_logo.svg.png">
</p>

<p align="center">
In this repository I will be posting my evolution in the development of a script that can cheat in Type Racer
</p>

# Libraries

:white_check_mark: Keyboard<br/>
:white_check_mark: Cv2<br/>
:white_check_mark: Time<br/>
:white_check_mark: PyTesseract<br/>
:white_check_mark: Pyautogui<br/>
:white_check_mark: Os<br/>
--------------------------------------------------------------
# Keyboard Control

>To control my keyboard I made use of the "keyboard" library. It's a simple library, I didn't find any difficulty using it.<br/>

<b> Example: </b>
```py
keyboard.write("Hello, World!")
```
Is this case the output is:
```py
Hello, World!
```
However, I wanted to write one letter at a time, just like an ordinary human does, so for that, I created a for with delay, to make typing look more "human"
```py
for character in sentense:
  time.sleep(0.02)
  keyboard.write(character)
```
With this my "writing' looks more human
--------------------------------------------------------------
# Take Screenshot

>To take the screenshot, for now I select a specific area of my screen, however it is an imprecise method and it only works if the text appears in the same place<br/>

<b> Example: <b/>
```py
screenshot = pyautogui.screenshot(region=(1226, 384, 407, 129))
screenshot.save("output path here")
```
It works, but as I said, only for a specific region<br/>
But I'll corret this soon
--------------------------------------------------------------
# Load the screenshot
--------------------------------------------------------------
# Using Tesseract
