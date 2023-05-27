import time
import pyautogui

def close_current_window():
	time.sleep(0.5)
	pyautogui.hotkey('alt', 'f4')

def go_to_workspace():
	time.sleep(0.5)
	pyautogui.hotkey('win', 'd')

def search(text = ''):
	time.sleep(0.5)
	pyautogui.press('win')

	time.sleep(0.5)
	pyautogui.write(text)

	time.sleep(0.5)
	pyautogui.press('enter')
