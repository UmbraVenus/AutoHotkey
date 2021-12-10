import pyautogui

def autohotkey():
    while True:
        print("Hello!")
        pyautogui.PAUSE = 1
        pyautogui.moveTo(100, 150)
        pyautogui.click()
        pyautogui.PAUSE = 10
        pyautogui.press('space', presses=3)
        pyautogui.press('w', presses=3)
        pyautogui.press('a', presses=3)
        pyautogui.press('d', presses=3)
        pyautogui.press('w', presses=3)
        pyautogui.press('d', presses=3)
        pyautogui.press('s', presses=3)
        pyautogui.PAUSE = 10
        pyautogui.press('space', presses=3)
        pyautogui.press('w', presses=3)
        pyautogui.press('d', presses=3)
        pyautogui.press('s', presses=3)
        pyautogui.press('w', presses=3)
        pyautogui.PAUSE = 10
        pyautogui.press('space', presses=3)
        pyautogui.press('a', presses=3)
        pyautogui.PAUSE = 15
        pyautogui.press('space', presses=3)
        pyautogui.press('s', presses=3)
        pyautogui.press('a', presses=3)
        print("World")

autohotkey()