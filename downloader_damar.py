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
    'https://www.youtube.com/watch?v=w58k6UGeSQw',
    'https://www.youtube.com/watch?v=T8visJjF4Sw',
    'https://www.youtube.com/watch?v=MTSgiIgTs5A',
    'https://www.youtube.com/watch?v=o6PZsAitVCc',
    'https://www.youtube.com/watch?v=rzHFwHFBIXY',
    'https://www.youtube.com/watch?v=HleJQbZjy-U',
    'https://www.youtube.com/watch?v=xTjSpIfyu4E',
    'https://www.youtube.com/watch?v=Ck63ZX-QO_k',
    'https://www.youtube.com/watch?v=9KLMYzwUCNQ',
    'https://www.youtube.com/watch?v=V79rn8jjW4k',
    'https://www.youtube.com/watch?v=Hm3S_TZSXuk',
    'https://www.youtube.com/watch?v=QBawDvuWP4k'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
