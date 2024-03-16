import pymysql
import pymysql.cursors

import dotenv
import os


dotenv.load_dotenv()

TABLE_NAME = 'users'
connection = pymysql.connect(
        host=os.environ['MYSQL_HOST'], 
        user=os.environ['MYSQL_USER'], 
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:    
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY(id)'
            ')'
            )
        #Limpar a tabela isso é igual a DELETE sem WHERE
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

    with connection.cursor() as cursor:    
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) '
            'VALUES(%s, %s)'
        )
        sql2 = (
                f'INSERT INTO {TABLE_NAME} '
                '(name, idade) '
                'VALUES(%(name)s, %(age)s)'
            )
        data = {'name': 'Nathan', 'age': 24}
        
        result = cursor.execute(sql, ('Gabriel', 23))
        result2 = cursor.execute(sql2, data)

        #print(result)
        #print(result2)
    
    
    with connection.cursor() as cursor:
        sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(name, idade) '
                'VALUES(%(name)s, %(age)s)'
            )
        data = ({'name': 'Almeida', 'age': 18},
                {'name': 'Silva', 'age': 26},
                {'name': 'Julia', 'age': 20})
        
        result = cursor.executemany(sql, data)

        #print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
                f'SELECT * FROM {TABLE_NAME} '
            )
        
        cursor.execute(sql)

        dados = cursor.fetchall()       
        
        for i in dados:
            print(i.values())
        
        print()

        for id, name, idade in dados:
            print(id, name, idade)
    
    print()

    with connection.cursor() as cursor:
        sql = (
                f'SELECT * FROM {TABLE_NAME} WHERE id = %s'
            )
        
        cursor.execute(sql, [5])

        dados = cursor.fetchall()       
        
        for i in dados:
            print(i)
        
        print()

        print(cursor.mogrify(sql, [5]))
        
        print()
        
        for id, name, idade in dados:
            print(id, name, idade)

    print()

    with connection.cursor() as cursor:
        sql = (
                f'DELETE FROM {TABLE_NAME} WHERE id = %s'
            )
        
        resultDelete = cursor.execute(sql, [2])

        print(resultDelete)
        
        connection.commit()
        
    print()

    with connection.cursor() as cursor:
        sql = (
                f'UPDATE {TABLE_NAME} SET name=%s, idade=%s WHERE id = %s'
            )
        
        resultUpdate = cursor.execute(sql, ['Rafael', 22, 3])

        print(resultUpdate)
        print()
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for i in cursor.fetchall():
            print(i)
 
        connection.commit()