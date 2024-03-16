import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent
DB_NAME = 'DATABASE.sqlite3'
DB_FILE = ROOT_DIR/DB_NAME

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()

cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
               )

connection.commit()

#cursor.execute(f"INSERT INTO {TABLE_NAME} (name, weight) VALUES ('Gabriel Nathan Almeida Silva', 60.8) , ('Rafael Silva', 86.1)")
#connection.commit()

#cursor.execute(f'DELETE FROM {TABLE_NAME}')
#connection.commit()

#cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"')
#connection.commit()

sql = (f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)")
#cursor.execute(sql, ['Gabriel', 99])
#cursor.executemany(sql, [['Nathan', 99], ['Almeida', 99]])

cursor.executemany(sql, [{'name':'Silva', 'weight':99},{'name':'Sem nome', 'weight':99}])

#connection.commit()


#cursor.execute(f'DELETE FROM {TABLE_NAME}')
#connection.commit()

cursor.close()
connection.close()

if __name__ =='__main__':
    print(sql)
