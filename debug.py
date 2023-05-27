import pyautogui
import time
import actions

def get_mouse_position():
	while True:
		print(pyautogui.position())

def reset_configs():
	actions.set_theme('black')
