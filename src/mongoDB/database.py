import pymongo #need in order to use mongodb
from pymongo.errors import ConnectionFailure
import config #holds sensitive information in string that is used for connection

# Simple connection
# myClient = pymongo.MongoClient('mongodb://localhost:27017/') #create a mongo client object

myClient = pymongo.MongoClient(config.connection_string) #create a mongo client object
#connection_string is in following format:
#   'mongodb+srv://<username>:<passwd>@<cluster name and stuff taken from MongoAtlasDB>'

try:
    myClient.admin.command('ping')
    print("Connected successfully!")
except ConnectionFailure:
    print("Connection failed")

# print(myClient)

mydb = myClient['mydatabase'] #creating a database from the client established earlier
# the database above will still not be ceeated UNTIL content is put inside it

#we will not add content to the database created above
#a collection is the same as a Table in SQL databases
collection = mydb['collection']
# same as database, collection is created after filling it with content (via documents)

#Now we will add content to collection
#documents are same as records in SQL
#Will comment following 3 lines out so they don't keep getting added everytime I run to test file
# mydict = {"name": "Matt", "age": 16}
# x = collection.insert_one(mydict)
# print(x.inserted_id) #inserted_id will return the unique _id of a document inserted by insert_one()



print(myClient.list_database_names())
print(mydb.list_collection_names())
content = collection.find() #collection.find() returns a cursor, must loop through to get data
print(list(content))

single_content = collection.find_one({"name":"Matt"})
print(type(single_content)) #returns data as a dict
print(single_content)
print(single_content["age"]) #how to get back a certain thing from the content if found.

