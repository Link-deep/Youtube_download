# python "download/down.py"
# требуется библиотеки:
# - pip install yt-dlp
# - pip install ffmpeg
# Скачиваем видео с ЮТУБ
# следующие доработки, передавать видео куда-либо на сервер.!
# в приложение на телевизор?


import yt_dlp as youtube_dl

    # URL видео, которое вы хотите скачать
url = 'https://www.youtube.com/watch?v=0tZ0SAcZtco'

    # Параметры для youtube_dl
ytdl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Формат видео (720p)
        'outtmpl': '%(title)s.%(ext)s',  # Имя файла, в который будет сохранено видео
        'noplaylist': True,  # Не загружать плейлисты, только одно видео
        'socket_timeout': 30,
    }

    # Создаем объект youtube_dl
with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        ydl.download([url])