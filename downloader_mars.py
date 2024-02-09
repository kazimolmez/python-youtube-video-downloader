import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './Mars/'
ydl_opts = {
    #'format': 'bestvideo+bestaudio',
    'format': 'bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/watch?v=VhI-cMrwVjc',
    'https://www.youtube.com/watch?v=61eBFvUgIQY',
    'https://www.youtube.com/watch?v=qYeW707kLec',
    'https://www.youtube.com/watch?v=TooTjofiJXo',
    'https://www.youtube.com/watch?v=-2PfYuXExv0',
    'https://www.youtube.com/watch?v=yBGSVzWKrpk',
    'https://www.youtube.com/watch?v=VG7l_7pkshc',
    'https://www.youtube.com/watch?v=EJHorR_fSRU',
    'https://www.youtube.com/watch?v=TdyX3wdz5Xo'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
