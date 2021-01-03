# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
# The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary


seconds = int(input("How many seconds?"))
if seconds < 60:
    s = seconds

s = seconds % 60

mraw = seconds // 60
m = mraw % 60

hraw = mraw // 60
h = hraw % 24

d = hraw // 24
print(d,":",h,":",m,":",s)

