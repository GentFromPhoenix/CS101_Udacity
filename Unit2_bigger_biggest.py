# UNIT 2 - HOW TO REPEAT
# --------------------------------------

# ---- Procedural Abstraction ----------
# ----
# ---- def <name> (<parameters>):
# ---- 
hello = 'hey there partner1'
print hello
def rest_of_string(s):
    return s[1:]
    
print rest_of_string('audacity')
print rest_of_string('pass hat')
print rest_of_string(hello)
# --------------------------------
def sum(a,b):
    a=a+b
    return a

print "a is", sum(3,5)
a = 'Dave '
b = 'is cool'
print  sum(a,b)
# --- Nesting procedures --------
x = 2
print "For x = ", x
def square(n):
    a = n * n
    return a
    
print "and the final output is ",square(square(x))
# ---- quiz --------------------
def sum3(x,y,z):
    return x+y+z
    
print sum3(1,2,3)
# ---- quiz --------------------
def abbaize(text1,text2):
    return text1 + text2 + text2 + text1

print abbaize('a','b')
# ---- quiz --------------------
def find_second(string, target):
    firstspot = string.find(target)
    return string.find(target, firstspot+1)
    
danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace') # answer:25

# --- MAKING COMPARISONS -------
# --- Boolean Outputs ----------
# --- quiz ---------------------
print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21 # double equal needed because would try to assign a value

if 4 < 3:
    print "this is true"

print "did it work?"

# ---- quiz -----------------
def bigger(a,b):
    if a > b: # Don't forget the : even inside the procedure
        return a
    if a < b: # Don't forget the : even inside the procedure
        return b
    if a == b: # Don't forget the : even inside the procedure
        return a
        
print bigger(3,4)  
# ---- another approach to above ---
def bigger(a,b):
    if a > b: # Don't forget the : even inside the procedure
        n = a
    else:
        n = b
    return n
        
print bigger(3,4)  

# --- quiz is_friend ----------------
def is_friend1(name):
    return name[0] == 'D'
   

print is_friend1('Diane')
print is_friend1('Fred')
# --- quiz more is_friend ----------

def is_friend(name):
    if name[0] == 'D':
        return True
    else: 
        return name[0] == 'N'
            
print is_friend('Diane')
 #>>> True

print is_friend('Ned')
 #>>> True

print is_friend('Moe')

# --- OR opporator  --------------
print True or False # prints true
print False or True # prints true
print True or True # prints true
print False or False # print false
print True or this_is_an_error # prints true
#print False or this_is_an_error # prints an error because Falso

# ---- Quiz ---------------------
def biggest(x,y,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

print biggest(3,6,9)
print biggest(6,9,3)
print biggest(9,3,6)
print biggest(3,3,9)
print biggest(9,3,9)
print '------------'
# --- Another approach ---------
# --- use procedure Bigger twice from above --

def biggest2(x,y,z):
     return bigger(bigger(x,y),z)
     
print biggest2(3,6,9)
print biggest2(6,9,3)
print biggest2(9,3,6)
print biggest2(3,3,9)
print biggest2(9,3,9)
print '------------'   

# ---- or using a built in function ---
def biggest3(x,y,z):
    return max(x,y,z)
    
print biggest3(3,6,9)
print biggest3(6,9,3)
print biggest3(9,3,6)
print biggest3(3,3,9)
print biggest3(9,3,9)
print '------------'

# ------------------------------------
# --- WHILE Looping with while construct
# ---------------------------------------
# while <testexpression>:
#    <block>
# ---------------------------------------
i = 0
while i < 10:
    print i
    i = i + 1
