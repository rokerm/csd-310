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

    # connect to the pysports database 
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #insert new player
    add_player = ("INSERT INTO player(first_name, last_name )")
