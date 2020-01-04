#! /usr/bin/python3
'''
Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

GAME_URL = 'https://gabrielecirulli.github.io/2048/'
SPEED = 0.3  # sec

# Open game webpage
browser = webdriver.Chrome()
browser.get(GAME_URL)

containerElem = browser.find_element_by_tag_name("html")
print(f'is enabled: {containerElem.is_enabled()}')
# Issue commands
commands = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
count = 0
while True:
    for cmd in commands:
        try:
            containerElem.send_keys(cmd)
        except Exception as err:
            print(err)
            print(f'count: {count}')
            sys.exit()

        count += 1
        time.sleep(SPEED)
