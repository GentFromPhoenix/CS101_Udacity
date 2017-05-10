 # -----------------------------------------------------------   
 # --- SUBROUTINE - isleapyear 
 # --- INPUT year
 # --- RETURNS True or False                       
 # --- This provides a quick check using an algorithm 
 # --- provide by wikidpedia to determine if a given year
 # --- is a leapyear
 # -----------------
 # --- if (year is not divisible by 4) then (it is a common year)
 # --- else if (year is not divisible by 100) then (it is a leap year)
 # --- else if (year is not divisible by 400) then (it is a common year)
 # --- else (it is a leap year)
 # ----------------------------------------------------------- 

def isleapyear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:       
        return True
        
    
 # -----------------------------------------------------------   
 # --- SUBROUTINE - daysinmonth
 # --- INPUTS month, year
 # --- RETURNS the days in the month for a given month
 # --- CALLS isleapyear for February (month = 2) to determine
 # --- correct days 28 or 29 (leap year)   
 # -----------------------------------------------------------

def daysinmonth(month,year):
    # month 1,3,5,7,8,10,12
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if month == 2:
            if isleapyear(year):
                return 29
            else:
                return 28

 # -----------------------------------------------------------   
 # --- SUBROUTINE - nextDay
 # --- INPUTS year, month, day
 # --- RETURNS the next calendar day from the one input
 # --- CALLS daysinmonth(month, year) to determine the days
 # --- in current month to be indexed by 1, so to determine 
 # --- if last day or month, move to next month.  
 # -----------------------------------------------------------
def nextDay(year, month, day):
    monthdays = daysinmonth(month,year)
    if day != monthdays:
        return year,month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

 # ----------------------------------------------------------- 
 # --- Suggested helper procedure  
 # --- SUBROUTINE - DateIsBefore
 # --- INPUTS year1, month1,day1,year2,month2,day2
 # --- RETURNS True or False
 # --- Purpose to make sure the end date is later than
 # --- the birth date.  
 # -----------------------------------------------------------
def DateIsBefore(year1, month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False
# -----------------------------------------------------------   
# --- MAIN PROGRAM - daysBetweenDates 
# --- INPUTS year1, month1, day1, year2, month2, day2
# --- RETURNS days between birth date and end date
# --- CALLS DateIsBefore - for assertion error check and
# ---       to provide a STOP for the While statement
# --- CALLS nextday - to sequence the current day to the
# ---       the next day.           
# -----------------------------------------------------------
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # this assertion statement makes sure end date is not before birth date
    assert not DateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while DateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
        # print year1, month1, day1        
    #print "the days are", days
    print '---------------------------'
    print "the number of days is", days
    return days 
 
 # -----------------------------------------------------------   
 # --- Test Case procedure provided in problem statement    --
 # ----------------------------------------------------------- 
    
def test():
    test_cases = [((1961,7,3,2017,4,26), 20386), 
                  ((1961,4,11,2017,4,26), 20469),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed it should be", answer
        else:
            print "Test case passed!"

test()

