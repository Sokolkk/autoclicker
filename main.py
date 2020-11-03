import pyautogui
import time
def click():
  i=1
  while i<=60:
    pyautogui.click(100,100)
    time.sleep(60)
    i+=1
click()
