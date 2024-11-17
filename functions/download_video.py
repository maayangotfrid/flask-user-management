import os
from flask import send_from_directory

def download_video(filename):
    # ניצור את הנתיב המלא של הקובץ
    try:
        file_path = os.path.join(os.getcwd(), 'Tiktok_download_files', filename)
        
        # אם הקובץ קיים, נשלח אותו להורדה
        if os.path.exists(file_path):
            return send_from_directory(directory=os.path.dirname(file_path), filename=filename, as_attachment=True)
        else:
            return "File not found, please try again."
    except Exception as e:
        return f"An error occurred: {str(e)}"
