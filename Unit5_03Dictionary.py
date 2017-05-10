elements = {'hydrogent': 1, 'helium': 2, 'carbon': 6}
print elements
print elements['hydrogent']
print 'lithium' in elements # prints false because not in elements yet
# Adding Elements
elements['lithium'] = 3  # this adds elements
elements['nitrogen'] = 8
print elements
elements['lithium'] = 100 # this changes the value associated lithium since now exists
print elements
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai':17.8,'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5}
print population['Mumbai']

# Dictionaries within dictionaries

elements = {}
elements['H'] = {'name': 'Hyrdogen', 'number': 1, 'weight': 1.00794}
elements['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602, 'nobel gas': True}
print elements['H']
print elements['H']['name']
print elements['H']['weight']