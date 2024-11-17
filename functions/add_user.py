from flask import redirect, url_for
from functions.db_connection import get_db_connection

def add_user_to_db(name, email, phone, role, password, valid, active, image_url):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        '''INSERT INTO users (name, email, phone, role, password, valid, active, image_url)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
        (name, email, phone, role, password, valid, active, image_url)
    )
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('home'))
