import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './Pop/'
ydl_opts = {
    #'format': 'bestvideo+bestaudio',
    'format': 'bestaudio',
    'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
    'restrictfilenames': True,
}

url = [
    'https://www.youtube.com/watch?v=JVNbkiWbTGw',
    'https://www.youtube.com/watch?v=PgdNlgfs0bo',
    'https://www.youtube.com/watch?v=skk6_Eh1xf4',
    'https://www.youtube.com/watch?v=LFih56CNk1s',
    'https://www.youtube.com/watch?v=OFWBSpsqYM8',
    'https://www.youtube.com/watch?v=TsYavJnZe8k',
    'https://www.youtube.com/watch?v=eLv-tzJSD0U',
    'https://www.youtube.com/watch?v=lIyqo5iv7Ac',
    'https://www.youtube.com/watch?v=wgsWR2dpPyg',
    'https://www.youtube.com/watch?v=mOd42aZWfKM',
    'https://www.youtube.com/watch?v=LfEK1pDDJew',
    'https://www.youtube.com/watch?v=xY0FShMyHEg',
    'https://www.youtube.com/watch?v=O5tf_tSCqdc',
    'https://www.youtube.com/watch?v=_vyH_yFnVQA',
    'https://www.youtube.com/watch?v=55nxkunwSJI',
    'https://www.youtube.com/watch?v=715bkRI0BBE',
    'https://www.youtube.com/watch?v=R6gSMSYKhKU',
    'https://www.youtube.com/watch?v=CW5dhShyQVA',
    'https://www.youtube.com/watch?v=_GOZDXq7I-I',
    'https://www.youtube.com/watch?v=SCZgGVqVsbY',
    'https://www.youtube.com/watch?v=NAHRpEqgcL4',
    'https://www.youtube.com/watch?v=lvYg-YgJHuY',
    'https://www.youtube.com/watch?v=puD6-Ohozcc',
    'https://www.youtube.com/watch?v=9TSf2k03HPA',
    'https://www.youtube.com/watch?v=BokbpfhV8O8',
    'https://www.youtube.com/watch?v=Qxs7QfAmBrQ',
    'https://www.youtube.com/watch?v=hjLeV_Xc7lw',
    'https://www.youtube.com/watch?v=5anhsjs8rU8',
    'https://www.youtube.com/watch?v=he2jUbWOx9I',
    'https://www.youtube.com/watch?v=0w7AXnFQgDw',
    'https://www.youtube.com/watch?v=Ck63ZX-QO_k',
    'https://www.youtube.com/watch?v=HjVl8a9gR20',
    'https://www.youtube.com/watch?v=BVzsT0Apa5I',
    'https://www.youtube.com/watch?v=XTI8dwNlO0E',
    'https://www.youtube.com/watch?v=_fTE4NFEPI0',
    'https://www.youtube.com/watch?v=K7m9803KWE4',
    'https://www.youtube.com/watch?v=4AWJBMawRZk'
]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
