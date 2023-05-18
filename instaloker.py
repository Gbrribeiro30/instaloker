import pyautogui;
import time;
confirmar =  (959, 816)
jett = (1205, 924)
reyna = (881, 1000)
raze = (784, 1012)
#time.sleep(5)
#print(pyautogui.position())
i = 0
seleção = input("selecione seu boneco\n (1)Jett\n (2)Reyna\n (3)Raze\n")
if seleção == "1":
    boneco = jett
elif seleção == "2":
    boneco = reyna
elif seleção == "3":
    boneco = raze

time.sleep(5) 
while i < 30:
    pyautogui.click(boneco) 
    pyautogui.click(confirmar)
    i = i+1