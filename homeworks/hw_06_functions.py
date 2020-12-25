# write your pay computation function with time-and-a-half for overtime and
# create a function called computepay which takes two parameters ( hours and  rate).

# it will ask from user to enter below values.

# Enter Hours: 45
# Enter Rate: 10

# And then it return total amount money to be paid as float
# Pay: 450.0


def computepay():
    pay = 0
    hours = (input('give the hours'))
    while hours == str(hours):

        try:
            hours = int(hours)

        except:
            print ("Please enter a number")
            hours = (input('give the hours'))

        ###### rate ######
    rate = (input('give the rate'))
    while rate == str(rate):

        try:
            rate = int(rate)

        except:
            print ("Please enter a number")
            rate = (input('give the rate'))

    pay = hours * rate
    pay = float(pay)
    # print ("Pay: " + str(pay))
    return pay
    
result = computepay()
print ("Pay: " + str(result))