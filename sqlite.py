import  sqlite3
from  flashscore import  returnSostavPage
try:
    sqlite_connect = sqlite3.connect('C:\\fonbet\\fonbet.sqlite')
    
    

    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS FonbetTeam_Lineups_Home (
                                    id INTEGER PRIMARY KEY  ,
                                    StartTeam TEXT ,
                                    SpareTeam TEXT )'''

    sqlite_create_table_query2 = '''CREATE TABLE IF NOT EXISTS FonbetTeam_Lineups_Away (
                                    id INTEGER PRIMARY KEY ,
                                    StartTeam TEXT ,
                                    SpareTeam Text  UNIQUE)'''
    cursor=sqlite_connect.cursor()
    cursor.execute(sqlite_create_table_query)
    cursor.execute(sqlite_create_table_query2)
    sqlite_connect.commit()
    cursor=sqlite_connect.cursor()
    
    cursor.execute("DELETE FROM FonbetTeam_Lineups_Home")
    sqlite_connect.commit()
    #print(dir(player))
    
    playerRext='Denis'
    #print(player.text)
    smtp='INSERT INTO FonbetTeam_Lineups_Home (StartTeam)  VALUES (?)' 
    for player in returnSostavPage:
        
        #print(player.text)
        
        cursor.execute('INSERT INTO FonbetTeam_Lineups_Home (StartTeam)  VALUES (?)' ,(player.text,))
       
    sqlite_connect.commit()
    print("Таблица SQLite создана")
    
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connect):
        cursor.close()
        sqlite_connect.close()
       
        print("Соединение с SQLite закрыто")

