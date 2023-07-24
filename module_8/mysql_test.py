#Malachi Roker
#07/23/2023
#CYBR410

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:

    # connect to the pysports database 
    db = mysql.connector.connect(**config) 
    
    # output the connection status 
    print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("Press any key to continue...")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #disconnects from MYSQL
    db.close()