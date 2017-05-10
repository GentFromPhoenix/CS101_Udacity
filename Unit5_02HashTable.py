# ---- "ord" command
print ord('a')

# ---- "chr" command
print chr(34)

# ---- modulus operator
# <number> % <modulus> -----> <remainder>

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    for element in bucket:
        if element[0] == key:
             element[1] = value
             return htable
    hashtable_add(htable,key,value)
    return htable     


def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable, key).append([key,value])
    # The above returns with the specific elements of the bucket of interest
    # and since now pointing to that bucket element it can be appended.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))] #bucket contents
    


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
 
def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    for element in bucket:
        if element[0] == key:
            return element[1]
    return None 

#make_hashtable(3)
#print hash_table
#table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
#['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

#print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

#print hashtable_get_bucket(table, "Brick")
#>>> []

#print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
#>>> ['Rochelle', 94]]]

Break

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table,'Coach')
