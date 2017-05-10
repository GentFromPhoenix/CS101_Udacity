# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.


def freq_analysis(message):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    alpha_location = 0
    alpha_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    message_length = len(message)
    for check in alpha:
        n=0                            # Reset the message length loop to '0'
        while n <= message_length - 1: # Loop on the message length
            if message[n] == check:    # check to see if letter in message matches current letter
                alpha_count[alpha_location] = alpha_count[alpha_location] + 1 # if yes at a count of +1 to letter
            n = n + 1                  # next letter in message
        alpha_count[alpha_location] = alpha_count[alpha_location] * 1.0            
        alpha_count[alpha_location] = alpha_count[alpha_location] / message_length # convert to fractional value
        alpha_location = alpha_location + 1   # go to next letter
        
    return alpha_count
    

#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

#print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]