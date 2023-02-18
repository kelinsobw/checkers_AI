from time import sleep

import pyautogui


def search_chekers(image):
    print(image)

def screenshot():
    myScreenshot = pyautogui.screenshot()
    search_chekers(myScreenshot)
    #myScreenshot.save(r'file name.png')


if __name__=="__main__":
    while True:
        sleep(2)
        screenshot()

