import string

def validate_password(password):
    # alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    #                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    #                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # special_chars = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '_', '=']
    # allowed_chars = alphabet_lower + alphabet_upper + numbers + special_chars
    
    
    allowed_chars = list(string.ascii_letters + string.digits + string.punctuation)
    print(allowed_chars)
    #string.punction: !"#$%&'()*+,-./:;<=>?@[\]^_{|}~` 
    # criteria = {
    #     "lowercase": False,
    #     "uppercase": False,
    #     "number": False,
    #     "special_char": False
    # }
    if len(password) < 8:
        return False
    
    for char in password:
        if char not in allowed_chars:
            return False
        # if char in alphabet_lower:
        #     criteria["lowercase"] = True
        # elif char in alphabet_upper:
        #     criteria["uppercase"] = True
        # elif char in numbers:
        #     criteria["number"] = True
        # elif char in special_chars:
        #     criteria["special_char"] = True
            
    # for key in criteria:
    #     if criteria[key] == False:
    #         return False
    
    return True

def main():
    while True:
        user_input = input("To log in type \"l\", to sign in type \"s\", to exit type \"q\"")
        if user_input == "q":
            break
        user = input("Enter username: ")
        passwd = input("Enter password: ") #For now password will show in terminal, will change this later
        if user_input == "s": #Create an account if username does not exist in database.
            #TODO: check if username exists, if so then exit and prompt user to log in using "l" input instead
            
            #NOTE:Following validates password criteria
            check_passwd = validate_password(passwd)
            while check_passwd is not True:
                new_passwd = input("Password not valid, must hold true to following rules: \n" +
                                   "Length of at least 8 characters\n" +
                                   "Must have 1 Upper and Lower case letter\n" +
                                   "Must contain at least 1 numerical value"+
                                   "And at least 1 punctuation symbol.\n\n" +
                                   "Please try again: ")
                check_passwd = validate_password(new_passwd)
            print("password is valid")
            
            #TODO: make account
            
        elif user_input == "s":
            pass
        
    print("Exiting Program")
        
if __name__ == "__main__":
    main()