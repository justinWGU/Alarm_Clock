# Justin Ortiz Alarm Clock Program

# two modules needed to play sound and to get current time
from playsound import *
from datetime import *

# user's desired alarm time
alarm_time = input('Please enter desired alarm time using format \'HH MM AM/PM\' (Ex: 12 00 PM): ')

# slicing user input
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_period = alarm_time[6:].upper()

while True:
    # getting current time
    now = datetime.now()

    # divide current time into hours, secs, and pm/am
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    period = now.strftime("%p")

    # compare current time to user's desire alarm time
    if hour == alarm_hour:
        if minute == alarm_min:
            if period == alarm_period: # if all cases match, send notification to terminal and sound alarm
                print("WAKE UP !")
                alarm_counter = 0
                while alarm_counter < 10: # alarm will sound for about 20 secs unless program is manually ended
                    playsound("C:/Users/Justi/OneDrive/Desktop/Pojects/Alarm_Clock/sounds/bmw_warning_chime.wav")
                    alarm_counter += 1





