import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        host='dpg-css42c1u0jms73e5mel0-a.frankfurt-postgres.render.com',
        port=5432,
        database='mgproject',
        user='maayan',
        password='BowLYRTI3H9xpayZixjVTFWM0malIzzj'
    )
    return connection
