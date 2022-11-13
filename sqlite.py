import  sqlite3

try:
    sqlite_connect = sqlite3.connect('C:\\fonbet\\fonbet.sqlite')
    sqlite_create_table_query = '''CREATE TABLE FonbetTeam_Lineups_Home (
                                    id INTEGER PRIMARY KEY,
                                    StartTeam TEXT NOT NULL,
                                    SpareTeam text NOT NULL UNIQUE);'''

    sqlite_create_table_query2 = '''CREATE TABLE FonbetTeam_Lineups_Away (
                                    id INTEGER PRIMARY KEY,
                                    StartTeam TEXT NOT NULL,
                                    SpareTeam text NOT NULL UNIQUE);'''

    cursor=sqlite_connect.cursor()
    print("database successfully created and connected to sqlite")

    
    cursor.execute(sqlite_create_table_query)
    cursor.execute(sqlite_create_table_query2)
    sqlite_connect.commit
    print("Таблица SQLite создана")
    
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connect):
        sqlite_connect.close()
        print("Соединение с SQLite закрыто")

