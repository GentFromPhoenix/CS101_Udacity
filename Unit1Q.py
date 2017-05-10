# Tim Chesebrough - Udacity - CS101
# Introduction to Computer Science
# ---------------------------------------------------------
# Lesson 1 - Sessions -------------------------------------
# ---------------------------------------------------------
# print 1 + 2 + 3
# Need to add a decimal to obtain real numbers
# print (799625289 * 100 * (1.0/100000000))

# ----------------------------------------------------------
# Variables  Name = Expression
# ----------------------------------------------------------
#speed_of_light = 299792458                     # meters per second
#cycles_per_second = 2700000000.                # 2.7 Ghz
#billionth = 1.0 / 1000000000
#nanostick = speed_of_light * billionth * 100   # NanoStick length in cm

# distance light travels in one computer cycle for 2.7 Ghz machine
#cycle_distance = speed_of_light / cycles_per_second
#print cycle_distance

# Changing variable assignment
#cycles_per_second = 2800000000.                # 2.8 Ghz
#cycle_distance = speed_of_light / cycles_per_second
#print cycle_distance

# --- The = means assignment, not equal
#hours = 9 + 1
#hours = hours * 2
#print hours

#age = 55
#days_in_year = 365
#print age * days_in_year

# --------------------------------------
# STRINGS
# --------------------------------------
# Can you "" or ''
# Using "" allows you to use ' inside the ""
# Using '' allows you to use "" inside the ''
#print "Hello"
#print 'hello'
#print "Hello it's a boy"
#hello = "Howdy "
#print hello
#name = "Tim"
#print hello + name + " How's it going?"
# ---- multiplying strings ------------
#print name * 12                                  # prints name 12 times
# ---- indexing strings ---------------
# ---- count starts at 0 --------------
# ---- explanation has the count locations ----
# ---- 012345689  etc
name = 'explanation'
print name[0]
#print name[1]
#print name[-1]    # Counts from back of string
#print name[1 + 1 + 1]
#print name[2] + name[4] + name[5]
# ---- Selecting Sub Sequences -----
# ---- variable[start,stop+1]  -----
# ---- variable[:5] No start defined starts at beginning
# ---- variable[5:] No end defined ends at the end
#print name[2:6]    # first number is start, second is (1 after last)
#print name[:6]
#print name[:-1]
#print "ass " + name[2:6] 
#print name + name[0:-1+1]   # -- This will also end on the very last letter
# ---- Find the location in Strings ----------------
# ---- <string>.find(<string>)
# ---- returns starting location, return of -1 is not found ----
#print name.find('plan')
#print 'hey there'.find('there')
# ---- returns the value of location 2 -------------
#print name[2:]
#ohmy_string = 'When all men seek power, then absolutes become relative'
#print ohmy_string.find('then')
#print ohmy_string[ohmy_string.find('then'):]
# ---- Finding distance from specified location ----
#danton = "De l'audace, encore de l'audace, toujours de l'audace,"
#print danton.find('audace')
#print danton.find('audace', 0) 
#print danton.find('audace', 5)
#print danton.find('audace', 6) # -- this is after the first so looks for 2nd
# ---- if completely past it will return -1

# ---------------------------------------------------------------
# ---- FINAL QUIZ Session 1 
# ---------------------------------------------------------------
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')
start_link = page.find('"', start_link)
end_link = page.find('"', start_link+1)
url = page[start_link+1:end_link]
print url
print start_link
print end_link

# ------------------
# ---- EXTRAs - String Function 
# ------------------
# ---- COOL TRICK FOR ROUNDING THEN TEXT CONVERSION ------------
# ---- ADD 0.5 to the Number (or whatever 5 increment needed) --
# ---- To round up then truncate to needed text        ---------
# --------------------------------------------------------------
x = 3.14159
string_convert = str(x)
print string_convert


