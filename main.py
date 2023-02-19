import image
from time import sleep
from checkers.game import Game
import pyautogui
from PIL import Image, ImageGrab


def read_board(position):
    # board pixel = 384*384
    # cell = 48*48
    cells =

def search_chekers(screen):
    lighthouse = Image.open("lighthouse.png")
    lighthouse = lighthouse.convert('L')
    screen = screen.convert('L')
    width_screen = screen.size[0]
    heighth_screen = screen.size[1]
    width_lighthouse = lighthouse.size[0]
    heighth_lighthouse = lighthouse.size[1]
    pix_screen = screen.load()
    pix_lighthouse = lighthouse.load()
    print(pix_lighthouse[5, 5])
    print(pix_screen[5, 5])
    for y in range(0, heighth_screen):
        for x in range(0,width_screen):
            if pix_screen[x,y] == pix_lighthouse[0,0]:
                t = screen.crop((x, y, x+width_lighthouse, y+heighth_lighthouse))
                if lighthouse == screen.crop((x, y, x+width_lighthouse, y+heighth_lighthouse)):
                    return (x, y+heighth_lighthouse)


def screenshot():
    my_screeen =  pyautogui.screenshot()
    position = search_chekers(my_screeen)
    print(position)



if __name__=="__main__":
    screenshot()

