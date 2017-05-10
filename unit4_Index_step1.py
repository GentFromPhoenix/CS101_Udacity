# ------------------------------------------------
# ---- Structured Data - Unit 4 Continued
# ------------------------------------------------
# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    # Defi
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])


print '------------------------------------------------'
add_to_index(index,'udacity','http://udacity.com')
print 'after procedure 1',index
print '------------------------------------------------'
add_to_index(index,'computing','http://acm.org')
print 'after procedure 2',index
print '------------------------------------------------'
add_to_index(index,'udacity','http://npr.org')
print 'final value 3', index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]

# -----------------------------------------------------
# ------------ LOOK UP Procedure  ---------------------
# -----------------------------------------------------
# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return 'No Match Found'

print '------------------------'
print 'The Url(s) for udacity are',lookup(index,'udacity')
print 'The Url(s) for computing are',lookup(index,'computing')
print 'The Url(s) for oink are',lookup(index,'oink')
#>>> ['http://udacity.com','http://npr.org']
