# validsate a string ,meets the following standards 
# string lenth should be in 12 letters
# should contain one capital letter,one special sympol,one numeric digit

import re

def validate_string (input_string):
    if len(input_string)!=12:
        return False
    if not re.search(r'[A-Z]',input_string):
        return False
    if not re.search(r'[!@#$%^&*()]',input_string):
        return False
    if not re.search(r'/d',input_string):
        return False
    return True
input_string = str(input("Enter the string"))
if validate_string(input_string):
    print("The string meets the all standards:")
else :
    print("The string doesnot meet the all standards")
