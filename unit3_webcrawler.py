

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
page = urllib.urlopen('http://www.udacity.com/cs101x/index.html').read()
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
        print url   
        return url, end_quote

# ------------------------------------------------------------    
# --- Quiz 30 - Print All Links ------------------------------
# --- Final quiz to write a while loop that calls 
# --- get_next_target.   When get_next_target returns a 
# --- a value of None for variable url, url is now False
# --- and the procedure print_all_links breaks.
# -------------------------------------------------------------
links = []
def get_all_links(page):
    while True:
        url, endpos = get_next_target(page) # calling previous procedure
        if url:
            print "link found and added"
            links.append(url)
            page = page[endpos:]  
        else: 
            print " "
            print "**** That is the end of the links ****" 
            break 
    return links    
# --- RUN the procedure print_all_links ---------------------
print get_all_links(page)



# -----------------------------------------------------------
# --- END OF UNIT 2 -----------------------------------------
# -----------------------------------------------------------
