# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    n = 0
    stop = len(product)
    while n < stop:
        if debris.find(product[n]) > 0:
            message = product
            n = n + 1
        else:
            message = "Give me something that's not useless next time."
            n = stop
    return message
    
### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
# daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def daysofmonth(month):
    if month == 1:
        daysofmonth = 31
    if month == 2:
        daysofmonth = 28
    if month == 3:
        daysofmonth = 31
    if month == 4:
        daysofmonth = 30
    if month == 5:
        daysofmonth = 31
    if month == 6:
        daysofmonth = 30
    if month == 7:
        daysofmonth = 31
    if month == 8:
        daysofmonth = 31
    if month == 9:
        daysofmonth = 30
    if month == 10:
        daysofmonth = 31
    if month == 11:
        daysofmonth = 30
    if month == 12:
        daysofmonth = 31
    return daysofmonth

def daystodate(month,day):
    daycount = day
    monthcount = month - 1
    while monthcount > 0:
        daycount = daycount + daysofmonth(monthcount)       
        monthcount = monthcount - 1
    return daycount
    
def isleapyear (year):
    leeproot = 1900
    while leeproot <= year:
        if leeproot == year:
            print year, 'is a leap year'
            return 1
            break
        else:
            leeproot = leeproot + 4
    return 0
    
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    print '----------------------------------------------------'
    ##
    # Your code here.
    ##
#   ----------------------------------
#   determine days to birthday in year
    dayofbirth = daystodate(month1,day1)
    dayofdeath = daystodate(month2,day2)
    lifedays   = 0
    if year1 == year2:
        lifedays = dayofdeath - dayofbirth      
    else:
        # calculate days from end of year back to birthday
        lifedays = daystodate(12,31) - dayofbirth
        # determine leapyear count
        isleapyear(year1)
        # calculate midyear days
        year = year1 + 1
        while year != year2:
            lifedays = lifedays + 365
            # check for leapyear
            lifedays = lifedays + isleapyear(year)
            year = year + 1
        # add last year days
        lifedays = lifedays + dayofdeath + 1
        print 'all days', lifedays
    print 'lifedays is equal to', lifedays
    return lifedays
    
    

#   determine days to death day in year
       

# Test routine

def test():
    test_cases = [((2012,6,29,2013,6,31 ), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()