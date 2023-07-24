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

    cursor = db.cursor()

    #queries team data
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #results from query
    teams = cursor.fetchall()

    print("-- Displaying Team Records --")

    #iterates over team and shows results
    for team in teams:
        print("Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team [0], team[1], team [2]))

    #queries player data
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #results from query
    players = cursor.fetchall()
    
    print("-- Displaying Player Records --")

    #iterates over players and shows results
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))


    
    # output the connection status 
    #print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("Press any key to continue...")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    #disconnects from MYSQL
    db.close()


