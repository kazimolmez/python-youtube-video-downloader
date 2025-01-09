import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './Slow/'
    ydl_opts = {
        #'format': 'bestvideo+bestaudio',
        'format': 'bestaudio/best',
        'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
        'restrictfilenames': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                #'preferredquality': '192',
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
        'postprocessor_args': [
            '-c:a', 'mp3',
            '-ar', '44100',
            '-b:a', '192k',
            '-ac', '2'
        ],
        'extractaudio': True,
    }

    url = [
        'https://youtu.be/I0nkE0gAUag',
    ]

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
