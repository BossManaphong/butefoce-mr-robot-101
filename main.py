import random
import pyautogui
import time


password = pyautogui.password("Enter a password: ", "Password")
name = pyautogui.prompt("NAME : ", "Social Engineering ")
year = pyautogui.prompt("YEAR : ", "Social Engineering ")

name_UP = name.upper()
name_LOW = name.lower()

data = year+name_UP+name_LOW
data_list = list(data)

bruteforce = ""
count = 0

start_time = time.time()
while bruteforce != password:
    bruteforce = random.choices(data_list, k=len(password))
    print(str(bruteforce))
    count += 1

    if bruteforce == list(password):
        end_time = time.time()
        print("Password : {0} ".format(bruteforce))
        print("Amount : {0} times" .format(count))
        print("Time : {:.2f} seconds" .format(end_time - start_time))
        break
