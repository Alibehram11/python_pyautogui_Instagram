import pyautogui
import time
import webbrowser
#we call our libraries

pyautogui.moveTo(1245, 10)
pyautogui.click()
pyautogui.moveTo(803, 45)
#we exit the application

pyautogui.click()
pyautogui.typewrite("https://www.instagram.com/")
pyautogui.press("enter")
#open instagram on google

pyautogui.moveTo(66, 286)
time.sleep(7) #You can adjust the time here according to the speed of your computer
pyautogui.click()
pyautogui.moveTo(220, 225)
pyautogui.typewrite("alibehramalbayrak") #We write the account name in the instagram search section
time.sleep(1.5) #You can adjust the time here according to the speed of your computer
pyautogui.moveTo(267, 301)
pyautogui.click()
time.sleep(1) #You can adjust the time here according to the speed of your computer
pyautogui.moveTo(865, 148)
time.sleep(0.3) #You can adjust the time here according to the speed of your computer
pyautogui.click() #we are following
print("İşlem tamalandı")
