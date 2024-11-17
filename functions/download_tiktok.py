import os
import yt_dlp

def download_tiktok_video(video_url, save_path='Tiktok_download_files'):
    # ודא שהתיקייה קיימת, אם לא צור אותה
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # הגדרות ל-yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
        'noplaylist': True,  # מוודא שלא יבחרו פלייליסטים
        'quiet': False,  # מאפשר לראות את כל הלוגים
    }

    try:
        # הורדת הסרטון
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            return filename  # מחזיר את שם הקובץ שנשמר
    except Exception as e:
        return f"Error downloading video: {str(e)}"
