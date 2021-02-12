# FROM CS50
'''
(es)? possible no es or es
ummmm.......yes also work
^y(es)? - first char need to be y
no$ - end of the word
'''
import re
s = input("Do you agree?\n")
if re.search("y(es)?", s, re.IGNORECASE):
    print("Agreed.")
elif re.search("n(o)?", s, re.IGNORECASE):
    print("Not agreed.")
