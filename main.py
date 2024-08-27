# требуется библиотеки:
# - pip install yt-dlp
# - pip install ffmpeg
# при работе в PyCharm и запуске на ПК треубется установить ffmpeg и настроить пусть к папке.
# Скачиваем видео с ЮТУБ
# ПРОКСИ не нужен, только VPN на компе.


import yt_dlp as youtube_dl
import subprocess
import time

try:
    subprocess.run(['ffmpeg', '-version'], check=True)
    print("FFmpeg доступен и работает.")
except subprocess.CalledProcessError:
    print("FFmpeg не установлен или недоступен.")


# URL видео, которое вы хотите скачать
url = 'https://www.youtube.com/watch?v=1rBjWMJIF20'

# Параметры для youtube_dl
ytdl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=360]',  # Формат видео (720p)
    # 'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # Имя файла, в который будет сохранено видео
    'noplaylist': True,  # Не загружать плейлисты, только одно видео
    'socket_timeout': 30,
    'cookiesfrombrowser': ('chrome',),  # Использовать cookies из браузера Chrome ОЧЕНЬ ВАЖНО!!!!
    # БРАУЗЕР ХРОМ Должен быть ЗАКРЫТ перед запуском скрипта
    # 'cookiesfrombrowser': ('firefox',),  # Или использовать cookies из браузера Firefox
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    },
    # 'proxy': 'http://hWTxZZyr:cwywZYwS@176.113.42.26:63970',  # Укажите ваш прокси здесь
    # Если требуется аутентификация, используйте 'proxy': 'http://username:password@proxyserver:port'
    'postprocessors': [{  # Добавление постпроцессора для преобразования видео в mp4
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'  # Целевой формат
    }],
}

 # Установка секундомера
start_time = time.time()

# Создаем объект youtube_dl
with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
    ydl.download([url])

# Остановка секундомера и вывод времени выполнения
end_time = time.time()
execution_time = (end_time - start_time) / 60
print(f"Время выполнения скрипта: {execution_time:.2f} минут")
