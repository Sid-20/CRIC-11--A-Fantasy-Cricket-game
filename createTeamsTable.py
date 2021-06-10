import sqlite3

def createTable():
    MyPlayer=sqlite3.connect('Cric11.db')
    curPlayer=MyPlayer.cursor()
    MyPlayer=sqlite3.connect('Cric11.db')
    curPlayer=MyPlayer.cursor()
    SQL1='''CREATE TABLE TEAMS(Team_Name TEXT(25) NOT NULL,PLAYERS TEXT NOT NULL,POINTS INTEGER NOT NULL);'''
    curPlayer.execute(SQL1)
    MyPlayer.commit()
    MyPlayer.close()

if __name__=='__main__':
    createTable()
    
