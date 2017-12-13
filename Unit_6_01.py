# Created by: Khoa Le
# Created on November 28 2017
# Created for ICS3U
# This program

from enum import Enum

Days = Enum('Sunday', 'Monday', 'Tuseday', 'Wedsnday', 'Thursday', 'Friday', 'Saturday')
print ("Enter your favourite day.")

day_input = raw_input('')
if day_input in Days:
	print(day_input + ' is your favourite day.')
else:
	print("Invalid day.")
	day_input = int(input("Enter your favourite day."))
	print(Days[day_input])
