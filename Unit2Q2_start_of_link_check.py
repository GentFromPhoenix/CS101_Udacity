# ------------------------------------
# --- WHILE Looping with while construct
# ---------------------------------------
# while <testexpression>:
#    <block>
# ---- Quiz 24 - Print Numbers ----------------------
def print_numbers(i):
    n = 1
    while n <= i:
        print n
        n = n + 1
        
print_numbers(5)

# --- Quiz 25 - Factorial --------------------------
def factorial(n):
    total = 1
    while n > 0:
        total = total * n
        n = n - 1
    return total
    
print factorial(5)

# --- Quiz 26 - Break ------------------------------
# --- break ----------------------------------------
# --- while True - this shows a continuous true ----

# --- Quiz 27 -  
first, second = 3 , 4

# -------------------------------------------------
# THIS WAS A SPECIAL CASE ADDITION ----------------
# TO PROVIDE AN ACTUAL PAGE FROM THE WEB ----------
# THAT COULD BE USED IN THE FINAL QUIZ FOR --------
# UNIT 2.           -------------------------------
# This function reads the source content of a given
# web page and input to our variable 'page' to be 
# used in our get_next_target procedure.
# -------------------------------------------------
import urllib
page = urllib.urlopen('http://xkcd.com/353').read()
# -------------------------------------------------

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        url, end_quote = None, 0
        return url, end_quote 
    else:       
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]    
        return url, end_quote

url, endpos = get_next_target('this is a <a href="http://udacity.com">link')
#print get_next_target('this is a <a href="http://udacity.com">link')
#url, endpos = get_next_target('this is not a string')
#print get_next_target('this is not a string')
# -------------------------------------------------------------
# --- example of when 'None' is returned it's a null string ---
# --- and as such 'False' in the below if statement -----------
# -------------------------------------------------------------
if url:
    print "There was text!"
else:
    print "There was no text here!"
# ------------------------------------------------------------    
# --- Quiz 30 - Print All Links ------------------------------
# --- Final quiz to write a while loop that calls 
# --- get_next_target.   When get_next_target returns a 
# --- a value of None for variable url, url is now False
# --- and the procedure print_all_links breaks.
# -------------------------------------------------------------
def print_all_links(page):
   
    while True:
        url, endpos = get_next_target(page) # calling previous procedure
        if url:
            print url
            page = page[endpos:]   
        else: 
            print " "
            print "**** That is the end of the links ****" 
            break     
       
# --- RUN the procedure print_all_links ---------------------
print_all_links(page)


# -----------------------------------------------------------
# --- END OF UNIT 2 -----------------------------------------
# -----------------------------------------------------------
