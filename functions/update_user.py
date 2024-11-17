from flask import request
import psycopg2
from psycopg2 import sql

def update_user_in_db(user_id):
    # קבלת הנתונים מהטופס
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    role = request.form.get('role')
    password = request.form.get('password')
    valid = request.form.get('valid')
    active = request.form.get('active')
    image_url = request.form.get('image_url')

    # חיבור למסד נתונים
    connection = psycopg2.connect(
        host='dpg-css42c1u0jms73e5mel0-a.frankfurt-postgres.render.com',
        port=5432,
        database='mgproject',
        user='maayan',
        password='BowLYRTI3H9xpayZixjVTFWM0malIzzj'
    )
    cursor = connection.cursor()

    try:
        # יצירת פקודת SQL לעדכון המידע
        update_query = sql.SQL("""
            UPDATE users
            SET name = %s, email = %s, phone = %s, role = %s, password = %s, 
                valid = %s, active = %s, image_url = %s
            WHERE id = %s
        """)

        # הרצת הפקודה עם הערכים החדשים
        cursor.execute(update_query, (name, email, phone, role, password, valid, active, image_url, user_id))
        connection.commit()

        return "User updated successfully"
    except Exception as e:
        connection.rollback()  # אם יש שגיאה, נעשה rollback של השינויים
        return f"Error updating user: {str(e)}"
    finally:
        cursor.close()
        connection.close()
