# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(passage):
    count = 1
    for char in passage:
        if char == " ":
            count = count + 1
    return count
# Another way
def count_words2(passage):
    count = passage.split()
    return len(count)

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
print count_words2(passage)
#>>>56
# ---------------------------------------------------------------------
# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(time, distance):
    # remember total distance is x2 because round trip
    return ((2 * distance) / (time / 1000.)) / speed_of_light 
    # last is ms to s converstion
    
print speed_fraction(50,5000)
#>>> 0.666666666667
print speed_fraction(50,10000)
#>>> 1.33333333333  
# Any thoughts about this answer, or these inputs?
# ---------------------------------------------------------------------

# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#


def convert_seconds(seconds_in):
    response = ""
    hours = seconds_in // 3600
    minutes = (seconds_in // 60) - (hours * 60)
    seconds = seconds_in - (minutes * 60) - (hours * 3600)
    print hours, minutes, int(seconds)
    # Hours
    if hours == 1:
        response = response + str(int(hours)) + ' hour, '
    else: 
         response = response + str(int(hours)) + ' hours, '
    # Minutes
    if minutes == 1:
        response = response + str(int(minutes)) + ' minute, '
    else: 
         response = response + str(int(minutes)) + ' minutes, '
    # Seconds
    if seconds == 1:
        response = response + str(seconds) + ' second'
    else:
        if seconds_in > int(seconds_in):
            response = response + str(seconds) + ' seconds'
        else:
            response = response + str(seconds) + ' seconds'
    return response
    
print convert_seconds(1)

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

