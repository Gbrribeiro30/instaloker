import pyautogui;
import time;
#confirmar x=959, y=816
#jett x=1205, y=924
#print(pyautogui.position())
time.sleep(5)
i = 0
while i < 30:
    pyautogui.click(x=1205, y=924)
    pyautogui.click(x=959, y=816)
    i = i+1