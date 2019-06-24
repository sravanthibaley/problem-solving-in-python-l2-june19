#function to validate a phone number

import re
def phonenumbervalidator(num):
    pattern = '^[6-9][0-9]{9}'
    if re.match(pattern,str(num)):
        print("valid number")
    else:
        print("Invalid")
    return
phonenumbervalidator(9177086399)


def emailvalidator(email):
    pattern= '[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][2-4a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailvalidator("sravanthi@gmail.com")