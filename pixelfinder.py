import pyautogui
import keyboard

print('press x to start')

while True:
    if keyboard.is_pressed("x"):
        pyautogui.displayMousePosition()
        print('press x to start again')
