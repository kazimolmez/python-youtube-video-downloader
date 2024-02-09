import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './Turku/'
ydl_opts = {
    #'format': 'bestvideo+bestaudio',
    'format': 'bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/watch?v=snHsHdx0S7k',
    'https://www.youtube.com/watch?v=P9jEknDlPyY',
    'https://www.youtube.com/watch?v=BKrqBbK7Ixo',
    'https://www.youtube.com/watch?v=LGWjLBtgSIc',
    'https://www.youtube.com/watch?v=NNqjiGDfQqc',
    'https://www.youtube.com/watch?v=G9tXKqIc774',
    'https://www.youtube.com/watch?v=U2g9VvGqdNc',
    'https://www.youtube.com/watch?v=qVDAqN96o1w',
    'https://www.youtube.com/watch?v=deHPTjklpMw',
    'https://www.youtube.com/watch?v=NgW6VmWxPNA',
    'https://www.youtube.com/watch?v=SaVHsbx18OY',
    'https://www.youtube.com/watch?v=deHPTjklpMw',
    'https://www.youtube.com/watch?v=OCFZN5HeGkc',
    'https://www.youtube.com/watch?v=dpDch6l1M44',
    'https://www.youtube.com/watch?v=cqsGUkWhz2M',
    'https://www.youtube.com/watch?v=w0DTBlCB9ko',
    'https://www.youtube.com/watch?v=JXibjgvfZLw',
    'https://www.youtube.com/watch?v=vxJbHBPc7wI',
    'https://www.youtube.com/watch?v=T5Z2CaoaRhc',
    'https://www.youtube.com/watch?v=h7B-Afj_vAQ',
    'https://www.youtube.com/watch?v=cvaL1OM_Okg',
    'https://www.youtube.com/watch?v=ph3SoDtg_Ec',
    'https://www.youtube.com/watch?v=PK-EB2dhl00',
    'https://www.youtube.com/watch?v=dC18MxLKVC8',
    'https://www.youtube.com/watch?v=O6mrzmw5YuA',
    'https://www.youtube.com/watch?v=mF5PsNZFjvU',
    'https://www.youtube.com/watch?v=dLyx4PmiMRM',
    'https://www.youtube.com/watch?v=QuYxUd1qQc0',
    'https://www.youtube.com/watch?v=V_7dxixoiyY',
    'https://www.youtube.com/watch?v=HKrZQrZGI0g',
    'https://www.youtube.com/watch?v=v72Z7weB9aA',
    'https://www.youtube.com/watch?v=p6zaEzMzKAc',
    'https://www.youtube.com/watch?v=L2Y9y40wt5U',
    'https://www.youtube.com/watch?v=j2tVhs9-8QY',
    'https://www.youtube.com/watch?v=-7nkDmTcNbw',
    'https://www.youtube.com/watch?v=hVfRtuheMxE',
    'https://www.youtube.com/watch?v=wzjmzmLDRaM',
    'https://www.youtube.com/watch?v=v9QUPfBE5P4'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
