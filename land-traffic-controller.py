
import time
import datetime

#Check the signal first Stop when it is Red and Go when it is Green.
#When it is Green, before proceeding further check for predestines if you see predestines stop and wait or Go if no predestines.
#Whenever you see orange (Amber) slow down.

def countdown(total_seconds):
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
 
traffic_lights_signal_dictionary = {
	"Red": "Stop",
	"Green": "Go",
	"Orange": "Slow-down"
}

def traffic_status(status):
	print(f'Traffic light is: {status}')
    
print('Traffic light is in operation')

i = 0
max_iterations = 3

while i < max_iterations:
	pedestrian_signal = "Stop"
	traffic_signal = list(traffic_lights_signal_dictionary)[i]
	message = "Traffic light is: " + pedestrian_signal
	
	countdown(5)
	if traffic_signal == 'Red':
		traffic_status(traffic_signal)
		if pedestrian_signal == "Stop":
			print("- Pedestrian is stop - don't cross the road yet.")
			pedestrian_signal = "Go"
			countdown(10)
		print('- Pedestrian you may now cross the road.')
	elif traffic_signal == 'Green':
		traffic_status(traffic_signal)
		print("- Pedestrian don't cross the road.")
		countdown(10)
	else:
		traffic_status(traffic_signal)
		print('- Vehicle slow down...')
		print('- Pedestrian standby..')
		countdown(5)
	i += 1
	countdown(5)

