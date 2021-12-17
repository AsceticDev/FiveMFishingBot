import cv2
import time
import pytesseract
import pyautogui
from consumer.data import *
from pywinauto.application import Application
from winops.winops import focusWindow

app = Application().connect(title_re="FiveM")
win = app.window(title_re = "FiveM")

isHungry = False
isThirsty = False



def isMenuOpen():
    useText='USE'
    pyautogui.screenshot(region=(UseButtonRegion)).save(r'img\usebutton.png')
    img = cv2.imread(r'img\usebutton.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    custom = '--psm 6 --oem 3 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNM-'
    txt = pytesseract.image_to_string(img, config=custom, lang='eng')
    time.sleep(1)

    if useText == txt[:-2]:
        return True
    else:
        return False
        

def useFishingRod(insCls):
    try:
        insCls.setBusy()
    except:
        pass
    if insCls:
        insCls.cancel()
    focusWindow(win)
    time.sleep(2)
    
    if not isMenuOpen():
        winSendKey(openInvKey)
        time.sleep(2)

    pyautogui.click(startScrollLoc)
    time.sleep(1)

    squareObjects = [Square() for i in range(len(textBoxRegions))]

    #find square that has fishing rod
    for i in range(len(textBoxRegions)):
        #set the textbox region equivalent to the position in the textBoxRegions array list
        squareObjects[i].textBoxRegion = textBoxRegions[i]
        #set cursor position for item
        squareObjects[i].itemLoc = [(textBoxRegions[i][0] + 57), (textBoxRegions[i][1] - 30)]
        #set text for square.textBoxContent
        tbr = squareObjects[i].textBoxRegion
        screenFunc(tbr, squareObjects[i])

    #begin operation
    for i in range(len(squareObjects)):
        if fishingRodText in squareObjects[i].textBoxContent:
            print('found fishing rod!')
            consume(squareObjects[i].itemLoc)
            time.sleep(1)

    if isMenuOpen():
        winSendKey(openInvKey)
        time.sleep(2)

    try:
        insCls.setNotBusy()
    except:
        pass



def winSendKey(letter):
    win.send_keystrokes(letter)

def pixelChecker(actionPixelLoc, actionPixelColor):
    # meinPixel = pyautogui.pixel(actionPixelLoc[0], actionPixelLoc[1])
    meinPixel = pyautogui.pixelMatchesColor(actionPixelLoc[0], actionPixelLoc[1], (actionPixelColor), tolerance = 60)
    if meinPixel:
        return False
    else:
        return True

def consume(itemLoc):
    pyautogui.moveTo(itemLoc) 
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(useButtonLoc)  
    time.sleep(1)
    pyautogui.mouseUp(button='left')

def screenFunc(aList, squareObj = {}):
    pyautogui.screenshot(region=(aList)).save(r'img\titties.png')
    img = ()
    try:
        img = cv2.imread(r'img\titties.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    except:
        # print('issue with populating the image!')
        pass
    custom = '--psm 6 --oem 3 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNM-'
    try:
        txt = pytesseract.image_to_string(img, config=custom, lang='eng')
        squareObj.textBoxContent = txt[:-1]
    except:
        # print('pytersseract txt issue')
        pass

    # if squareObj:
        # squareObj.textBoxContent = txt[:-1]
    return squareObj.textBoxContent


def startConsumer(insCls):
    insCls.setBusy()
    # insCls.cancel()
    print('consumer started')
    time.sleep(1)
    focusWindow(win)
    time.sleep(1)
    #Check that menu is open
    print('about to check if menu open')
    if not isMenuOpen():
        print('inside check, menu is not open')
        focusWindow(win)
        time.sleep(1)
        winSendKey(openInvKey)
    time.sleep(1)
    pyautogui.click(startScrollLoc)
    time.sleep(1)

    print('so we check if hungry and thirsty')

    consumables = Consumables()
    squareObjects = [Square() for i in range(len(textBoxRegions))]
    for i in range(len(textBoxRegions)):
        squareObjects[i].textBoxRegion = textBoxRegions[i]
        squareObjects[i].itemLoc = [(textBoxRegions[i][0] + 57), (textBoxRegions[i][1] - 20)]
        tbr = squareObjects[i].textBoxRegion
        loopText = screenFunc(tbr, squareObjects[i])

    isHungry = pixelChecker(eatPixel, eatPixelRGBMenu)
    isThirsty = pixelChecker(drinkPixel, drinkPixelRGBMenu)

    if isHungry:
        print('we hungry')
        for i in range(len(squareObjects)):
            for item in consumables.foodList:
                if item in squareObjects[i].textBoxContent:
                    print(f'Match!!! : {item}')
                    isHungry = pixelChecker(eatPixel, eatPixelRGB)
                    print(isHungry)
                    if isHungry:
                        print('we\'re eating right now')
                        consume(squareObjects[i].itemLoc)

    elif isThirsty:
        print('we thirsty')
        for i in range(len(squareObjects)):
            for item in consumables.drinkList:
                if item in squareObjects[i].textBoxContent:
                    isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)
                    if isThirsty:
                        print('we\'re drinking right now')
                        consume(squareObjects[i].itemLoc)



    if isMenuOpen():
        winSendKey(openInvKey)
        pyautogui.sleep(1)
