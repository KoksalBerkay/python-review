# write your pay computation function with time-and-a-half for overtime and
# create a function called computepay which takes two parameters ( hours and  rate).

# it will ask from user to enter below values.

# Enter Hours: 45
# Enter Rate: 10

# And then it return total amount money to be paid as float
# Pay: 450.0

def computepay():
    hours = int (input ("How many hours?"))
    rate = int (input ("Give the rate"))
    pay = hours * rate
    print(pay)
    
    
computepay()
