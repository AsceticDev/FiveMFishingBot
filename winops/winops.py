from pywinauto import win32defines 


def sendkey(window, letter):
    window.send_keystrokes(letter)
    print("sending : {}".format(letter))

def setFocus(window, letter):
    if window.has_style(win32defines.WA_INACTIVE): # if minimized
        window.set_focus()
        sendkey(window, letter)
    else:
        sendkey(window, letter)

def isWindowInFocus(window):
    if window.has_style(win32defines.WA_INACTIVE): # if minimized
        return False
    else:
        return True

def focusWindow(window):
    window.set_focus()