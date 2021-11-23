import cv2
import time
import pytesseract
import pyautogui
from pywinauto.application import Application

useButtonLoc = [960, 545]
UseButtomRegion = [930, 530, 60, 30] #x y w h
global isHungry 
global isThirsty
isHungry = False
isThirsty = False
app = Application().connect(title_re="FiveM")
win = app.window(title_re = "FiveM")

drinkPixel = [220, 1056]
drinkPixelRGB = [1, 98, 130]
eatPixel = [208, 1056]
eatPixelRGB = [115 , 126, 1]

class Consumables:
    foodList = [
        'BREAD',
        'CHIPS',
        'CHOCOLATE',
        'HAMBURGER',
        'SANDWICH',
    ]
    drinkList = [
        'COCA-COLA',
        'ICE-TEA',
        'WATER',
    ]

textBoxRegions = [
    [188, 330, 112, 30],
    [308, 330, 112, 30],
    [428, 330, 112, 30],
    [548, 330, 112, 30],
    [668, 330, 112, 30],

    [188, 450, 112, 30],
    [308, 450, 112, 30],
    [428, 450, 112, 30],
    [548, 450, 112, 30],
    [668, 450, 112, 30],

    [188, 570, 112, 30],
    [308, 570, 112, 30],
    [428, 570, 112, 30],
    [548, 570, 112, 30],
    [668, 570, 112, 30],

    [188, 690, 112, 30],
    [308, 690, 112, 30],
    [428, 690, 112, 30],
    [548, 690, 112, 30],
    [668, 690, 112, 30],

    [188, 810, 112, 30],
    [308, 810, 112, 30],
    [428, 810, 112, 30],
    [548, 810, 112, 30],
    [668, 810, 112, 30],
]

class Square:
    textBoxRegion = []
    textBoxContent = ''
    itemLoc = [1, 2]

def pixelChecker(actionPixelLoc, actionPixelColor):
    # meinPixel = pyautogui.pixel(actionPixelLoc[0], actionPixelLoc[1])
    meinPixel = pyautogui.pixelMatchesColor(actionPixelLoc[0], actionPixelLoc[1], (actionPixelColor), tolerance = 30)
    if meinPixel:
        return False
    else:
        return True


def consume(itemLoc):
    pyautogui.moveTo(itemLoc)   # moves mouse to X of 100, Y of 200.
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(useButtonLoc)   # moves mouse to X of 100, Y of 200.
    time.sleep(1)
    pyautogui.mouseUp(button='left')

def screenFunc(aList, squareObj = {}):
    pyautogui.screenshot(region=(aList)).save(r'img\titties.png')
    img = cv2.imread(r'img\titties.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    custom = '--psm 6 --oem 3 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNM-'
    txt = pytesseract.image_to_string(img, config=custom, lang='eng')

    if squareObj:
        squareObj.textBoxContent = txt[:-1]
    return txt

consumables = Consumables()
squareObjects = [Square() for i in range(len(textBoxRegions))]
isHungry = pixelChecker(eatPixel, eatPixelRGB)
isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)

for i in range(len(textBoxRegions)):
    #set the textbox region equivalent to the position in the textBoxRegions array list
    squareObjects[i].textBoxRegion = textBoxRegions[i]
    #set cursor position for item
    squareObjects[i].itemLoc = [(textBoxRegions[i][0] + 57), (textBoxRegions[i][1] - 30)]
    #set text for square.textBoxContent
    tbr = squareObjects[i].textBoxRegion
    loopText = screenFunc(tbr, squareObjects[i])

while isHungry or isThirsty:
        if isHungry:
            for i in range(len(squareObjects)):
                for item in consumables.foodList:
                    if item in squareObjects[i].textBoxContent:
                        isHungry = pixelChecker(eatPixel, eatPixelRGB)
                        consume(squareObjects[i].itemLoc)
                        isHungry = pixelChecker(eatPixel, eatPixelRGB)
        elif isThirsty:
            for i in range(len(squareObjects)):
                for item in consumables.drinkList:
                    if item in squareObjects[i].textBoxContent:
                        isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)
                        consume(squareObjects[i].itemLoc)
                        isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)
        else:
            print('We are fine')
            isThirsty = pixelChecker(eatPixel, eatPixelRGB)

