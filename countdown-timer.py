import time 

unit = input("do you want set time in (seconds / minutes / hours):").lower()
time1 = int(input("Enter countdown time: "))

if unit == "minutes":
    time1 = time1 * 60
elif unit == "hours":
    time1 = time1 * 3600



for remaining_time in range(time1, -1 , -1):
    hours = int(remaining_time / 3600)
    minutes = int((remaining_time % 3600) / 60)
    seconds = remaining_time % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r" , flush=True)
    time.sleep(1)

print("\nTime's up! ⏰")
