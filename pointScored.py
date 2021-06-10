import sqlite3

MyPlayer=sqlite3.connect('Cric11.db')
    

def enterTeam():
    name=input("Enter player name: ")
    curPlayer=MyPlayer.cursor()
    SQL1='''SELECT SCORED FROM MATCH WHERE PLAYER='"+name+"'; '''
    curPlayer.execute(SQL1)
    print("SQL executed")
    run=curPlayer.fetchall()
    for r in run:
        print(r)
    


if __name__=="__main__":
    enterTeam()
        
        
