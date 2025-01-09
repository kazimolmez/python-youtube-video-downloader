import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './Damar/'
ydl_opts = {
    #'format': 'bestvideo+bestaudio',
    'format': 'bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/watch?v=1gPbL3Eb628',
    'https://www.youtube.com/watch?v=w58k6UGeSQw'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
