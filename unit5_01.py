import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time
    
def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
        
print time_execution('1 + 1')
print time_execution('spin_loop(10**4)')[1] # print only the run_time


def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a','a',]
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index