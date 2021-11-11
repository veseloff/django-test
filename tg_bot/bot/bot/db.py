import psycopg2
from psycopg2 import Error
from datetime import datetime


try:
    connection = psycopg2.connect(user='postgres',
                                  password='business_trips123',
                                  host='localhost',
                                  port=5432,
                                  database='business_trips'
                                  )
    cursor = connection.cursor()
    insert_query = """INSERT INTO user_profile_cheque (amount,  date_time, report, business_trip_id) VALUES (%s, %s, %s, %s)"""
    item_purchase_time = datetime.now()
    item_tuple = (100, item_purchase_time, 'Колбаса 100р', 1)
    cursor.execute(insert_query, item_tuple)
    connection.commit()
    print("1 запись успешно вставлена")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
