from flask import redirect, url_for
from functions.db_connection import get_db_connection

def delete_user_from_db(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('home'))
