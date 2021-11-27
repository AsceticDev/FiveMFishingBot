from consumer.consumer import startConsumer, useFishingRod
from menu import menu
from fisher.fisher import startFishing
from pywinauto.application import Application
import keyboard

app = Application().connect(title_re="FiveM")
win = app.window(title_re = "FiveM")
setafk = False
hungerStatus = False
thirstStatus = False


while True:
    menu.print_menu()
    setafk = int(input('Please select if you want AFK Mode Enabled: '))
    break

print('Press ALT + x to start')
print('press ALT + q to exit')
while True:
    if keyboard.is_pressed("alt+x"):
        print('Bot Activated')
        if setafk == True:
            print('AFK MODE ACTIVE')
        else:
            print('Non AFK')

        while True:
            if keyboard.is_pressed("alt+q"):
                print("Exiting bot mode")
                print("Press CTRL + c to fully kill program")
                print("press ALT + x to start again")
                break

            startFishing(win, setafk)