import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()

cursor.execute(f'UPDATE {TABLE_NAME} SET name = "Nathan", weight = 50.0 WHERE id = 1')
connection.commit()

cursor.close()
connection.close()