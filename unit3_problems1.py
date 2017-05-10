def print_header(header):
    # 'Problem - ' is 7 character long
    length = 11 + len(header)
    n = 0
    bar_label = ''
    while n < length:
        bar_label = bar_label + '-'
        n = n + 1
    print bar_label
    print 'Problem - ', header
    return bar_label
    



# ----------------------------------------------------------
# --- UNIT 3 Begins
# ----------------------------------------------------------

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.
# REMEMBER LISTS also start at count 0
print print_header('Lists - Return Days in Month')

def how_many_days(month_number):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]
 
print how_many_days(1)
#>>> 31
print how_many_days(9)
#>>> 30
# -----------------------------------------------------
# --- NExt Problem
# -----------------------------------------------------
print print_header('Nested List - Find and Print Sub Elements')
# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]
# -----------------------------------------------------
# --- NExt Problem - Mutation
# -----------------------------------------------------
print print_header('Stooges - replacing elements')

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print stooges[2]

# -----------------------------------------------------
# --- NExt Problem - Mutation - IMPORTANT ON THIS ONE
# -----------------------------------------------------
print print_header('IMPORTANT - IMPORTANT - variable association when =')

p = ['H','e','l','l','o']
q = p    # This links these two lists
print p, q
p[0] = 'Y'
print p, q
print "It changes both lists"
# -----------------------------------------------------
# --- NExt Problem - Mutation - IMPORTANT ON THIS ONE
# -----------------------------------------------------
# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.
# -----------------------------------------------------
# **** IMPORTANT IMPORTANT IMPORTANT *******************
# **** Whatever the variable defined in the 'def' statement
# **** in this case 'p' is now linked to the object in the 
# **** call statement in this case the list 'spy'.   Now changing
# **** p in the procedure also changes spy
print print_header('IMPORTANT-IMPORTANT - more variable association')

spy = [0,0,7]
def replace_spy(p):
    p[2] = p[2] + 1
    
replace_spy(spy)
print spy

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

#replace_spy(spy)
#print spy
#>>> [0,0,8]

# -----------------------------------------------------
# --- INFORMATION - 
# -----------------------------------------------------
# --- APPEND
# --- <list>.append(<element>)
print print_header('APPEND - Adding elements to a list')
print stooges
stooges.append('shemp')
print stooges
# --- +
# --- [0,1] + [2,3] ----> [1,2,3,4]
print print_header('What Happens when you do [0,1] + [2,3]')
print [0,1] + [2,3]
# ------------
# --- len ----
# ------------
print print_header('len() returns the number of elements')
print len(stooges)  # provides the number of elements
# -----------------------------------------------------
# --- NExt Problem - DONT Forget NESTING    
# -----------------------------------------------------
# alist = [1, 2, 3,[10,15,16]]
# This list has for elements 3 number and 1 list

# -----------------------------------------------------
# --- NExt Problem - LOOPS on LISTS   
# -----------------------------------------------------
# alist = [1, 2, 3,[10,15,16]]
# This list has for elements 3 number and 1 list
print print_header('Loops on Lists')

def print_all_elements(p):
    i = 0
    message = ''
    while i <= len(p)-1:
        print p[i]
        message = message + p[i]
        i = i + 1
    return message
    
print print_all_elements(p)
# -----------------------------------------------------
# --- NExt Problem - FOR Loops   
# -----------------------------------------------------
# for <name> in <list>:
#      <block>
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.
print print_header('For Loops and Summing')

def sum_list(elements):
    sum = 0
    for values in elements: # <----------------
        sum = sum + values
    return sum

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134
# -------------------------------------------------
# FIND ELEMENT CONTAINTING STRING
# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
print print_header('Element Containing String')

def measure_udacity(string_list):
    n = 0
    for string in string_list:
        if string[0] == 'U':
            n = n + 1
    return n

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
# -------------------------------------------------
# FIND ELEMENT IN STRING
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
# --------------------------------------------------
print print_header('Find Element')

def find_element(list, search):
    n = 0
    for e in list:
        if e == search:
            return n
        n = n + 1    
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

# -------------------------------------------------
# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
print print_header("Using 'index' 'in' and 'not in'")

def find_element(list, search):
    print 'the list is',list, 'the search string is', search
    if search in list:
        return list.index(search)
    if search not in list:
        return -1
        
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
# -------------------------------------------------
print print_header('Another way for previous - shorter code')
def find_element(list, search):
    print 'the list is',list, 'the search string is', search
    if search not in list:
        return -1
    return list.index(search)
    
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
# -------------------------------------------------
# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.
print print_header('Union - adding string elements but no duplicate strings')

def union(a,b):
    for check in b:
        if check not in a:
            a.append(check)
            




# To test, uncomment all lines 
# below except those beginning with >>>.
a = [1,2,3]
b = [2,4,6]
union(a,b)
print 'a =', a 
print 'b =', b
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]
# -------------------------------------------------
# --- POP Operation -------------------------------
# -------------------------------------------------
# --- <list>.pop() ----> element
# --- mutates the listing by removing and returning
# --- its last element 
# -------------------------------------------------
print print_header('POP - using POP operator')
a = ['first', 'second', 'third', 'forth']
print 'this is a ', a
x = a.pop()
print 'value of "a.pop()"=', x, '--- value of "a"=', a
y = a.pop()
print 'value of another "a.pop()"=', y, '--- value of "a"=', a
a.append(x)
a.append(y)
print '-----------'
print 'Now a.append(value) in "wrong" order'
print 'and "a" is now reordered. a=', a

print print_header('END OF THESE LESSONS')


