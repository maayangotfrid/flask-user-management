<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download TikTok Video</title>
</head>
<body>
    <h1>Download TikTok Video</h1>

    <form method="POST">
        <label for="video_url">Enter TikTok Video URL:</label>
        <input type="text" name="video_url" id="video_url" required>
        <button type="submit">Download</button>
    </form>

    {% if result %}
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
