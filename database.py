import sqlite3

def insert_varible_into_table(name, number, email, address):
    try:
        sqlite_connection = sqlite3.connect('main.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = """INSERT INTO users
                              (name, number, email, address)
                              VALUES (?, ?, ?, ?);"""

        data_tuple = (name, number, email, address)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
