import time
import pyautogui
import windows

def change_refresh_rate_from_60hz_to_75hz():
	windows.go_to_workspace()
	windows.search('taxa')

	time.sleep(2)
	pyautogui.click(1526, 512)

	time.sleep(0.5)
	pyautogui.click(1526, 474)

	time.sleep(2)
	pyautogui.click(851, 566)

	windows.close_current_window()
	windows.go_to_workspace()

def set_theme(theme):
	windows.go_to_workspace()
	windows.search('tema')

	time.sleep(2)

	if theme == 'shine':
		pyautogui.click(1085, 453)
	
	if theme == 'black':
		pyautogui.click(846, 453)

	windows.close_current_window()
	windows.go_to_workspace()

# def downgrade_graphic_card_driver():
# 	windows.go_to_workspace()

# 	time.sleep(0.5)
# 	pyautogui.hotkey('win', 'i')

# 	time.sleep(2)
# 	pyautogui.write('gerenciador de dispositivos')

# 	time.sleep(2)
# 	pyautogui.press('down')

# 	time.sleep(0.)
# 	pyautogui.press('enter')

# 	pyautogui.click(214, 208)

# 	windows.go_to_workspace()

def enable_night_light_at_20():
	windows.go_to_workspace()
	windows.search('luz')

	time.sleep(2)
	pyautogui.click(1384, 217)

	while True:
		pyautogui.click(1384, 217)

	windows.close_current_window()
	windows.go_to_workspace()
