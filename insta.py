import pyautogui
import time
import webbrowser


pyautogui.moveTo(1245, 10)
pyautogui.click()
pyautogui.moveTo(803, 45)

pyautogui.click()
pyautogui.typewrite("https://www.instagram.com/")
pyautogui.press("enter")

pyautogui.moveTo(66, 286)
time.sleep(7)
pyautogui.click()
pyautogui.moveTo(220, 225)
pyautogui.typewrite("alibehramalbayrak")
time.sleep(1)
pyautogui.moveTo(267, 301)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(865, 148)
time.sleep(0.3)
pyautogui.click()
print("İşlem tamalandı")