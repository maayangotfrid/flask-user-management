from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# פונקציה להתחברות למסד הנתונים
def get_db_connection():
    connection = psycopg2.connect(
        host='dpg-css42c1u0jms73e5mel0-a.frankfurt-postgres.render.com',
        port=5432,
        database='mgproject',
        user='maayan',
        password='BowLYRTI3H9xpayZixjVTFWM0malIzzj'
    )
    return connection

# דף הבית שמציג את כל המשתמשים
@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()

    # שליפת כל המשתמשים
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()  # כל המשתמשים

    cursor.close()
    connection.close()

    return render_template('index.html', users=users)

# דף להוספת משתמש חדש
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        role = request.form['role']
        password = request.form['password']
        valid = request.form['valid']
        active = request.form['active']
        image_url = request.form['image_url']

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

    return render_template('add_user.html')

# דף לעדכון פרטי משתמש
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # שליפת המידע על המשתמש
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()

    if request.method == 'POST':
        name = request.form.get('name', user[1])  # אם השדה לא מעודכן, נשאיר את הערך הקיים
        email = request.form.get('email', user[2])
        phone = request.form.get('phone', user[3])
        role = request.form.get('role', user[4])
        password = request.form.get('password', user[5])
        valid = request.form.get('valid', user[6])
        active = request.form.get('active', user[7])
        image_url = request.form.get('image_url', user[8])

        cursor.execute(
            '''UPDATE users SET name = %s, email = %s, phone = %s, role = %s, password = %s, 
            valid = %s, active = %s, image_url = %s WHERE id = %s''',
            (name, email, phone, role, password, valid, active, image_url, user_id)
        )
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    cursor.close()
    connection.close()

    return render_template('update_user.html', user=user)

# דף למחיקת משתמש
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # מחיקת המשתמש
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
