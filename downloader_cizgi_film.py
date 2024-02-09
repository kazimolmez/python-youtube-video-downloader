import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './CigziFilm/'
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/playlist?list=PLPys1om7jEih8BqLJgluJihhEBBL96EEw',
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
