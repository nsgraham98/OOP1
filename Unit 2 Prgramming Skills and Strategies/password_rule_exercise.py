is_valid = False

while not is_valid:
    password = (input("Enter a password; must be at least 8 characters long, and contain 1 character from each of the following:\nLowercase letter, \nUppercase letter, \nNumber. \nEnter password:  "))
    if len(password) >= 8:
        print("valid")  
        length_eight = True
        if password.isalpha() == False:
            print("valid")
            has_number = True
            if password.islower() == False:
                print("Valid password!")
                has_upper_lower = True
                is_valid = length_eight and has_number and has_upper_lower
            else:
                print("Invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("Valid Password!")  

                
           
# # all alphabet characters -> True
# isalpha(password)

# # all digit characters -> True
# isaldigit(password)

# # all lowercase characters -> True
# islower(password)
