import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = 'C:\Projects\Personal\youtube-video-downloader\KVP'
ydl_opts = {
    #'format': 'bestvideo+bestaudio',
    'format': 'bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/watch?v=YT1r5_URIXM'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
