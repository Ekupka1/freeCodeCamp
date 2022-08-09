#Time Calculator - 

# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

#Clock function
def time():
    # string= strftime('%H:%M:%S %p') # Military time
    string= strftime('%I:%M:%S:%p') # By 12Hr
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font= ("ds_digital", 80), background= "black", foreground= "cyan")
label.pack(anchor='center')

time()
mainloop()


# def time_calculator():

# def add_time(time, duration, *args):
#     print("Returns: ")

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)

#make inital timer 0-12
# adding time. 
# week day counter 