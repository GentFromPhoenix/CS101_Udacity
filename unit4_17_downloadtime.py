# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# 8 bits to 1 byte

#print 'kb', 2 ** 10      # one kilobit, kb
#print 'kB', 2 ** 10 * 8  # one kilobyte, kB

#print 'Mb', 2 ** 20      # one megabit, Mb
#print 'MB', 2 ** 20 * 8  # one megabyte, MB

#print 'Gb', 2 ** 30      # one gigabit, Gb
#print 'GB', 2 ** 30 * 8  # one gigabyte, GB

#print 'Tb', 2 ** 40      # one terabit, Tb
#print 'TB', 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

speeds = [['kb', 2 ** 10],
         ['kB', 2 ** 10 * 8],
         ['Mb', 2 ** 20],
         ['MB', long(2 ** 20 * 8)],
         ['Gb', 2 ** 30],
         ['GB', long(2 ** 30 * 8)],
         ['Tb', 2 ** 40 ],
         ['TB', 2 ** 40 * 8]]

def convert_seconds(seconds_in):
    response = ""
    hours = seconds_in // 3600
    minutes = (seconds_in // 60) - (hours * 60)
    seconds = seconds_in - (minutes * 60) - (hours * 3600)
    #print hours, minutes, int(seconds)
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


def download_time(filesize, fileunit, bandwidth, bandwidthunit):
    for element in speeds:
        if element[0] == fileunit:
            size = filesize * element[1]
            print 'for filesize', filesize, fileunit, 'the size is', size, 'in bits'
        if element[0] == bandwidthunit:
            bandspeed = bandwidth * element[1]
            print 'for bandwidth', bandwidth, bandwidthunit, 'the speed is', bandspeed, 'in bits/s'
    time = size / bandspeed
    print 'time =', time, 'seconds'
    return convert_seconds(time)    
    
print '----------------------------------------------------------------'
print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 0 minutes, 1 secondprint
print '----------------------------------------------------------------'
print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 secondprint
print '----------------------------------------------------------------'
print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable
print '----------------------------------------------------------------'
print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds
print '----------------------------------------------------------------'
print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds
print '----------------------------------------------------------------'
print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable
print '----------------------------------------------------------------'
print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
print '----------------------------------------------------------------'