import pyautogui
import time


class BlueTooth():
    def __init__(self):
        self.run()

    def run(self):
        # pyautogui.keyDown('winleft')
        # pyautogui.keyUp('winleft')
        # pyautogui.typewrite(['b', 'l', 'u', 'e'])
        # pyautogui.keyDown('enter')
        # pyautogui.keyUp('enter')

        pyautogui.press('winleft')
        pyautogui.typewrite(['b', 'l', 'u', 'e'])
        pyautogui.press('enter')
        time.sleep(1)
        button = pyautogui.locateOnScreen('JBL Clip 3.jpg')
        button = pyautogui.center(button)
        pyautogui.click(button)


if __name__ == '__main__':
    BlueTooth().run()
