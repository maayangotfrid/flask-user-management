import os
from flask import send_from_directory

def download_video(filename):
    # נשתמש בנתיב מלא כדי לשלוח את הקובץ להורדה
    try:
        file_path = os.path.join(os.getcwd(), 'Tiktok_download_files', filename)
        if os.path.exists(file_path):
            return send_from_directory(directory=os.path.dirname(file_path), filename=filename, as_attachment=True)
        else:
            return "File not found, please try again."
    except FileNotFoundError:
        return "File not found, please try again."
