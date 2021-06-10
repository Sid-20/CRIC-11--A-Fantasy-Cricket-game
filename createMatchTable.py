import sqlite3

def createTable():
    MyPlayer=sqlite3.connect('Cric11.db')
    curPlayer=MyPlayer.cursor()
    SQL1='''CREATE TABLE MATCH(
    PLAYER TEXT PRIMARY KEY NOT NULL,
    SCORED INTEGER,
    FACED INTEGER,
    FOURS INTEGER,
    SIXES INTEGER,
    BOWLED INTEGER,
    MAIDEN INTEGER,
    GIVEN INTEGER,
    WKTS INTEGER,
    CATCHES INTEGER,
    STUMPING INTEGER,
    RO INTEGER);'''
    curPlayer.execute(SQL1)
    MyPlayer.commit()
    print("Table Match Created")



        
    
