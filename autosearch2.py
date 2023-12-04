import requests
import pyautogui as pg
import os
import sys
import time
os.startfile("msedge")
time.sleep(2)
round = 0

def search():
    global round
    if(round >= 30):
        with pg.hold('alt'):
            pg.press('f4')
        sys.exit()
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    word = response.json()[0]
    pg.press('f4')
    pg.write(word, interval=0.03)
    pg.press('enter')
    time.sleep(3)
    round+=1
    search()

search()