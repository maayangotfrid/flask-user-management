from flask import Flask, render_template, request, redirect, url_for
from functions.db_connection import get_db_connection
from functions.download_tiktok import download_tiktok_video
from functions.add_user import add_user_to_db
from functions.update_user import update_user_in_db
from functions.delete_user import delete_user_from_db
from flask import send_from_directory
import os

app = Flask(__name__)

# דף ראשי - Dashboard
@app.route('/')
def home():
    return render_template('index.html')

# דף טיקטוק
@app.route('/tiktok', methods=["GET", "POST"])
def tiktok():
    if request.method == "POST":
        video_url = request.form["video_url"]
        # הורדת הסרטון
        filename = download_tiktok_video(video_url)
        if filename.startswith("Error"):
            message = filename
            return render_template('tiktok.html', message=message)
        else:
            # אם הסרטון הורד בהצלחה, העבר את שם הקובץ לדף ההורדה
            return redirect(url_for('download_video', filename=filename))
    return render_template('tiktok.html')


@app.route('/users', methods=["GET", "POST"])
def users():
    connection = get_db_connection()
    cursor = connection.cursor()

    # שליפת כל המשתמשים
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()  # כל המשתמשים

    cursor.close()
    connection.close()

    return render_template('users.html', users=users)





# דף להורדה
@app.route('/download_video/<filename>')
def download_video(filename):
    file_path = os.path.join(os.getcwd(), 'Tiktok_download_files', filename)
    if os.path.exists(file_path):
        return send_from_directory(directory=os.path.dirname(file_path), filename=filename, as_attachment=True)
    else:
        return "File not found, please try again."

# דף פייסבוק
@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

# דף אינסטגרם
@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

# דף טלגרם
@app.route('/telegram')
def telegram():
    return render_template('telegram.html')

# דף יוטיוב
@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

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

        return add_user_to_db(name, email, phone, role, password, valid, active, image_url)

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

        return update_user_in_db(user_id, name, email, phone, role, password, valid, active, image_url)

    cursor.close()
    connection.close()

    return render_template('update_user.html', user=user)

# דף למחיקת משתמש
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    return delete_user_from_db(user_id)

if __name__ == '__main__':
    app.run(debug=True)
