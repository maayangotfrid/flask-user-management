from functions.db_connection import get_db_connection

def update_user_in_db(user_id, name, email, phone, role, password, valid, active, image_url):
    # חיבור למסד הנתונים
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # ביצוע פקודת SQL לעדכון המשתמש
        cursor.execute('''
            UPDATE users 
            SET name = %s, email = %s, phone = %s, role = %s, password = %s, valid = %s, active = %s, image_url = %s 
            WHERE id = %s
        ''', (name, email, phone, role, password, valid, active, image_url, user_id))
        connection.commit()

        return "User updated successfully"
    except Exception as e:
        # אם קרתה שגיאה, נבצע rollback
        connection.rollback()
        return f"Error updating user: {str(e)}"
    finally:
        cursor.close()
        connection.close()
