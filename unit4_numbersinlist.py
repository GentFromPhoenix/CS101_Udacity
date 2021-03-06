# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    n = len(string) - 1
    count = 0
    x = [int(string[0])]
    xsub = []
    while count != n:
        # print int(string[count+1]), int(string[count]), 'count = ', count
        if int(string[count+1]) <= int(string[count]):
            xsub = xsub + [int(string[count+1])]
            loop_check = 1
        else:

            if len(xsub) > 0:
                x = x + [xsub] + [int(string[count+1])]
                xsub = []
                loop_check = 0
            else:
                x = x + [int(string[count+1])]
                loop_check = 0
        count = count + 1
    if loop_check == 1:
        x = x + [xsub]
    return x

#testcases
string = '5439879'
result = [5,[4,3],9,[8,7],9]
print result
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result
print '-----------------------------------------------'


string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print result
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result
print '-----------------------------------------------'


string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1], 2, 3, [2], 6, [6]]
print result
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result
print '-----------------------------------------------'

string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print result
print numbers_in_lists(string)
print repr(string), numbers_in_lists(string) == result