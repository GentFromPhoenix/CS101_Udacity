# --- Find the Median
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))
# --- My solution
def median(a,b,c):
    if a == biggest(a,b,c):
        a = 0
        return biggest(a,b,c)
    if b == biggest(a,b,c):
        b = 0
        return biggest(a,b,c)
    if c == biggest(a,b,c):
        c = 0
        return biggest(a,b,c)

# --- There solution - cleaner way to elimninate variables
def median1(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
print(median1(1,2,3))
#>>> 2

print(median1(9,3,6))
#>>> 6

print(median1(7,8,7))
#>>> 7
# ---- BLASTOFF -- While Loops 
def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print 'Blastoff'
        
countdown(9)

# --- Problem - Find Last
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(string,target):
    location = string.find(target,0)
    last_found = location
    while location != -1:
        last_found = location
        location = string.find(target, location+1)
    return last_found
        



print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False
            
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(change):
    fivep  = 0
    twop   = 0
    onep   = 0
    while change > 0:
        if change > 4:
            change = change - 5
            fivep = fivep + 1
        else:
            if change > 1:
                change = change - 2
                twop = twop + 1
            else:
                if change > 0:
                    change = change -1
                    onep = onep + 1
    return (fivep, twop, onep)
    
    # Your code here


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps


# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a, b, c):
    max_value = max(a,b,c)
    min_value = min(a,b,c)
    range = max_value - min_value
    return range
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6