import sys
from pynput.mouse import Button as MouseButton
from pynput.mouse import Controller as MouseController

from pynput.keyboard  import Key as KbKey
from pynput.keyboard  import Controller as KbController
from pynput.keyboard  import Listener as KbListener

import threading
import time


tup_first_mouse = (0,0)
tup_second_mouse = (0,0)
nr_first_mouse_clicks = 1  # configurable
nr_second_mouse_clicks = 1 # fixed
msec_delay = 0.05		   # configurable, 50 mSec (50/1000)
NR_MAX_CLICKS = 5

mouse = MouseController()
running = False

def thread_start_clicking():
	while(running):
		mouse.position = tup_first_mouse
		mouse.click(MouseButton.left, nr_first_mouse_clicks)
		mouse.position = tup_second_mouse
		mouse.click(MouseButton.left, nr_second_mouse_clicks)
		time.sleep(msec_delay)

def print_position_details():
	print("-"*28)
	print("1st mouse location = ", tup_first_mouse)
	print("2nd mouse location = ", tup_second_mouse)
	print("Multiplier         = ", nr_first_mouse_clicks)
	print("Delay              = ", msec_delay*1000," milli-sec")
	print("-"*28)

def on_kb_release(key):
	global nr_first_mouse_clicks
	global tup_first_mouse
	global tup_second_mouse
	global NR_MAX_CLICKS
	global running
	global msec_delay

	if(key == KbKey.esc):
		# print('Esc pressed')
		# Stop listener
		return False

	if(key == KbKey.f1):
		tup_first_mouse = mouse.position
		print("1st: ", tup_first_mouse)

	if(key == KbKey.f2):
		tup_second_mouse = mouse.position
		print("2nd: ", tup_second_mouse)

	if(key == KbKey.f3):
		nr_first_mouse_clicks = nr_first_mouse_clicks + 1
		if(nr_first_mouse_clicks > NR_MAX_CLICKS):
			nr_first_mouse_clicks = 1	
		print("Multiplier: ", nr_first_mouse_clicks)

	if(key == KbKey.f4):
		print_position_details()

	if(key == KbKey.f6):
		msec_delay = 0.05
		print("Delay: 50 mSec")

	if(key == KbKey.f7):
		s_delay = input("Delay in milli-sec(0-1000): ")
		try:
			msec_delay = int(s_delay)
			print("Delay: ",msec_delay, "mSec")
			msec_delay = float(msec_delay/1000.0)
		except:
			msec_delay = 0.05
			print("Delay: 50 mSec")

	if(key == KbKey.f8):
		if(running):
			running = False
			print("<--STOPPED... ", time.ctime())
		else:
			thread = threading.Thread(target=thread_start_clicking)
			running = True
			print("-->STARTED... ", time.ctime())
			thread.start()

def main():

	print("="*64)
	print("'F1' 	= Pick up 1st mouse location")
	print("'F2' 	= Pick up 2nd mouse location")
	print("'F3' 	= Increment mouse clicks for 1st location")
	print("'F4' 	= Print position details")
	print("'F8' 	= Start/Stop")
	print("'Esc' 	= Exit application")
	print("Advance settings")
	print("'F6' 	= Set delay FIXED to 50 mSec")
	print("'F7' 	= Enter delay value in range 0-1000. 1000=1sec")
	
	print("="*64)
	print("\n")

	print_position_details()

	# Collect events until released
	with KbListener(on_press=None, on_release=on_kb_release) as listener:
		listener.join()

	print('\nExiting application...')

main()


# from pynput.keyboard  import Key, Controller
# keyboard = KbController()
# # Press and release space
# keyboard.press(KbKey.ctrl_l )
# keyboard.release(KbKey.ctrl_l)

# from pynput.mouse import Button, Controller

# mouse = Controller()
# print(mouse.position)

# for i in range(0,10):
# 	mouse.position = (726, 618)
# 	mouse.click(Button.left,1)
# 	mouse.position = (986, 600)
# 	mouse.click(Button.left,1)
