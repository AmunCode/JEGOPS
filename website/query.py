import sqlite3

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = """select * from result where IMEI = '353240105790591'"""
    cursor.execute(sqlite_select_Query)

    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for record in records:
        print(record)
        print(type(record))

    cursor.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:

        sqliteConnection.close()
        print("The SQLite connection is closed")

