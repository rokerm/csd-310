#Malachi Roker
#07/30/2023
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


def show_players(cursor, title):
    
    #inner join statement
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #results from query
    players = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterates over players and shows results
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:

    #connect to the pysports database 
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #insert new player
    new_player = ("INSERT INTO player(first_name, last_name, team_id)" "VALUES (%s, %s, %s)")

    #player information
    player_info = ("Smeagol", "Shire Folk", 1)

    #insert new record
    cursor.execute(new_player, player_info)

    #commit new record in database
    db.commit()

    #shows all players in player table after insert query
    show_players(cursor, " Displaying Players After Insert ")

    #update new inserted record
    update_player = ("UPDATE player SET team_id =2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    #shows all players after update query
    show_players(cursor, " Displaying Players After UPDATE ")

    #delete query
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    #shows all players after delete query
    show_players(cursor, " Displaying Players After Delete ")

    input ("\n Press any key to continue...")

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





