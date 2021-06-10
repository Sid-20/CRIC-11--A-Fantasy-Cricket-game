import sqlite3

def createTable():
    MyPlayer=sqlite3.connect('Cric11.db')
    curPlayer=MyPlayer.cursor()
    SQL1='''CREATE TABLE STATS(
    PLAYER TEXT PRIMARY KEY NOT NULL,
    MATCHES INTEGER NOT NULL,
    RUNS INTEGER NOT NULL,
    Centuries INTEGER NOT NULL,
    Half_Centuries INTEGER NOT NULL,
    VALUE INTEGER NOT NULL,
    CATEGORY TEXT NOT NULL); '''
    curPlayer.execute(SQL1)
    MyPlayer.commit()
    print("Stats Table created")
    MyPlayer.close()

def enterData():
    name=input("Enter player name:")
    m=int(input("Enter the number of matches:"))
    r=int(input("Enter the number of runs:"))
    c=int(input("Enter the number of centuries:"))
    hc=int(input("Enter the number of half-centuries:"))
    v=int(input("Enter player value:"))
    cat=input("Define Category:")
    SQL2='''INSERT INTO STATS(PLAYER,MATCHES,RUNS,CENTURIES,HALF_CENTURIES,VALUE,CATEGORY) VALUES(?,?,?,?,?,?,?);'''
    MyPlayer=sqlite3.connect('Cric11.db')
    curPlayer=MyPlayer.cursor()
    curPlayer.execute(SQL2,(name,m,r,c,hc,v,cat))
    MyPlayer.commit()
    print("Data Updated")
    MyPlayer.close()
   
          

if __name__=="__main__":
    num=int(input("Enter the number of players:"))
    for i in range(num):
        enterData()

    
