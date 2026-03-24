# database_testing
Will use this repo to create, attach, modify, and simply test database usage with Python. Two main databases I will test will be MongoDB and MySQL

# <u>MongoDB</u>
The installation of MoongoDB steps were primarily taken from [W3Schools MongoDB Tutorial](https://www.w3schools.com/mongodb/mongodb_get_started.php) website.
## installing pyMongo
1. Install pymongo using: 
    
    ```python -m pip install pymongo```
2. Check it is installed using: 

    ```pip show pymongo```
3. 

## Using MongoDB Atlas to host a cloud based database
1. Sign up and  make an account on [MongDB Atlas](https://www.mongodb.com/cloud/atlas/register?utm_campaign=w3schools_mdb&utm_source=w3schools&utm_medium=referral).
2. Click on "Create a Cluster"
3. Follow steps on creating a cluster, will need to make a username and password as well for it (keep this somewhere safe)
4. Will also need to add IP Address to list of allowed IP Addresses. You can also do this under "Database & Network Access -> IP Access List".

    (Take note that after creating a cluster you can click "connect" and choose how you wish to connect. Steps will appear on how to move foward with the connection. You must connect to the cluster in order to be able to utilize the database).

## Installing MongoDB Shell (mongosh)
1. Following [official instructions](https://docs.mongodb.com/mongodb-shell/install/?utm_campaign=w3schools_mdb&utm_source=w3schools&utm_medium=referral) for downloading mongosh.
2. Check using the following command in terminal: ```mongosh --version``` (if no version number appears fall back to step 1).
