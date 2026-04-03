import string
import pymongo
import config
from pymongo.errors import ConnectionFailure

myClient = pymongo.MongoClient(config.connection_string) #create a mongo client object
try:
    myClient.admin.command('ping')
    print("Connected successfully!")
except ConnectionFailure:
    print("Connection failed")
    
mydb = myClient['mydb']
account_collection = mydb['account_collection']

#check if collection is empty, if so then add admin as first account
if account_collection.count_documents({}) == 0: 
    account_collection.insert_one({"username": "admin", "password": "admin"}) #naturally you should not have this in code since anyone with access to the file will now know admin.
    
    
def validate_password(password): 
    allowed_chars = list(string.ascii_letters + string.digits + string.punctuation)
    # print(allowed_chars)
    if len(password) < 8:
        return False
    
    for char in password:
        if char not in string.ascii_letters or char not in string.digits or char not in string.punctuation:
            return False
    return True

def user_exists(username): #return true as well as document of user if it
    query = {"username": username}
    document = account_collection.find_one(query)
    if document == None:
        return False, None
    else:
        return True, document

def createNewUser(username, passwd):
    query = {"username": username, "password" : passwd}
    result = account_collection.insert_one(query) #TODO: check back what is stored in result; howeer, will not be using it
    print("User has been created, try logging in now!!!")
    
def main():
    while True:
        user_input = input("To log in type \"l\", to sign in type \"s\", to exit type \"q\": ")
        if user_input == "q":
            break
        user = input("Enter username: ")
        passwd = input("Enter password: ") #For now password will show in terminal, will change this later
        exists, user_doc = user_exists(user)
        if user_input == "s": #Create an account if username does not exist in database.
            #TODO: check if username exists, if so then exit and prompt user to log in using "l" input instead
            if exists == True:
                print("User already exists, try logging in!!!")    
    
            #NOTE:Following validates password criteria
            else:
                check_passwd = validate_password(passwd)
                while check_passwd is not True:
                    passwd = input("Password not valid, must hold true to following rules: \n" +
                                       "Length of at least 8 characters\n" +
                                       "Must have 1 Upper and Lower case letter\n" +
                                       "Must contain at least 1 numerical value"+
                                       "And at least 1 punctuation symbol.\n\n" +
                                       "Please try again: ")
                    check_passwd = validate_password(passwd)
                print("password is valid")
                #TODO: Should salt password and encrypt/hash it somehow for protection. Not necesary for this but is good practice.

                #NOTE: create account and store in database
                createNewUser(user, passwd)
            
        elif user_input == "l":
            if exists == True:
                if passwd != user_doc["password"]:
                    i = 0
                    while passwd != user_doc["password"] and i < 3: #have 3 tries to get password right
                        passwd = input(f"Wrong password try again ({3-i} tries left): ")
                        i += 1
                    if i == 3:
                        print("No more tries, GOODBYE!!!")
                        break
    
                print(f'Welcome back {user_doc["username"]}!!!')
                print("Hope you have a wonderful day!!!")
                break
        
                        
        
    print("Exiting Program")
    
def test_validate_pw():
    username = "anakin"
    bad_pws = ["skywalker", "Skywalker", "Skywalker1", "skywalker1..", "sky", "Sk2,"]
    pw_good = "Skywalker123."
    for pw in bad_pws:
        assert False == validate_password(pw), f"Something wrong in validate password, using this password: {pw} "
    print("PASSED BAD PASSWORDS!!!")
    
    assert True == validate_password(pw_good), "Not validating good password!!!"
    print("PASSED VALIDATE_PASSWORD TEST")
    
    
        
if __name__ == "__main__":
    # main()
    test_validate_pw()