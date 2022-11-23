import  sqlite3
from  flashscore import  sostavPage
try:
    sqlite_connect = sqlite3.connect('C:\\fonbet\\fonbet.sqlite')
    
    
    if """create table  FonbetTeam_Lineups_Home""":
        print(" table  FonbetTeam_Lineups_Home creating")
    else:
        sqlite_create_table_query = '''CREATE TABLE FonbetTeam_Lineups_Home (
                                    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
                                    StartTeam TEXT NOT NULL,
                                    SpareTeam text NOT NULL UNIQUE);'''

        sqlite_create_table_query2 = '''CREATE TABLE FonbetTeam_Lineups_Away (
                                    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
                                    StartTeam TEXT NOT NULL,
                                    SpareTeam text NOT NULL UNIQUE);'''
        cursor=sqlite_connect.cursor()
        cursor.execute(sqlite_create_table_query)
        cursor.execute(sqlite_create_table_query2)

    cursor=sqlite_connect.cursor()
    for player in sostavPage:
        print(player.text)
        sqlite_insert_query = """INSERT INTO FonbetTeam_Lineups_Home
                            (StartTeam)  VALUES (?) """ 
        cursor.execute(sqlite_insert_query,player)
    
    
    


    
    

    

    cursor.execute(sqlite_insert_query,(player))
    sqlite_connect.commit
    print("Таблица SQLite создана")
    
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connect):
        sqlite_connect.close()
        print("Соединение с SQLite закрыто")

