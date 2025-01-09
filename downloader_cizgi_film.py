#!./venv/bin/python

import subprocess
import os

from yt_dlp import YoutubeDL

if __name__ == "__main__":
    separator = '-'
    download_path = './CigziFilm/'

    ydl_opts = {
        'quiet': True, #bilgi mesajlarını kapatmak için
        'format': 'bestvideo+bestaudio',
        'outtmpl': f'{download_path}%(uploader)s{separator}%(title)s.%(ext)s',
        'restrictfilenames': True,
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
        'postprocessor_args': [
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-ar', '44100',
            '-b:a', '192k',
            '-ac', '2'
        ],
    }

    urls = [
        'https://www.youtube.com/watch?v=JhSWWNITd6Y',
        'https://www.youtube.com/watch?v=QC6nmPnJaY0',
        'https://www.youtube.com/watch?v=FzYMgMkZNks',
        'https://www.youtube.com/watch?v=2BMSFa6JR7U',
        'https://www.youtube.com/watch?v=NloEEHoUptM',
        'https://www.youtube.com/watch?v=slcpxzHJYBQ',
        'https://www.youtube.com/watch?v=S9jvxkegPLU',
        'https://www.youtube.com/watch?v=LwB7OSqOHkA',
        'https://www.youtube.com/watch?v=Qmfq2aexY2M',
        'https://www.youtube.com/watch?v=lmM8G6ROTx4',
        'https://www.youtube.com/watch?v=SxG_bP-U1D0',
        'https://www.youtube.com/watch?v=naJqQwcu6-s',
        'https://www.youtube.com/watch?v=WiveXRk_FpE',
        'https://www.youtube.com/watch?v=II7Z9D8gPsA',
        'https://www.youtube.com/watch?v=nyI_oq5NbSA',
        'https://www.youtube.com/watch?v=A2IbyjrBarM',
        'https://www.youtube.com/watch?v=bgJ8xFJs96U',
        'https://www.youtube.com/watch?v=wSOF61QSUCI',
        'https://www.youtube.com/watch?v=P0koA9_Zizs',
        'https://www.youtube.com/watch?v=xfVi1HEq7Dk',
        'https://www.youtube.com/watch?v=kxVgj6arTQY',
        'https://www.youtube.com/watch?v=G8e4P8dmuGY',
        'https://www.youtube.com/watch?v=573-UTqACcM',
        'https://www.youtube.com/watch?v=o_Ls-gNQXTg',
        'https://www.youtube.com/watch?v=ds9o32BpFk8',
        'https://www.youtube.com/watch?v=QITJOtDm9TU',
        'https://www.youtube.com/watch?v=7epZBFCuH6I',
        'https://www.youtube.com/watch?v=0UHZZfCGzPo',
        'https://www.youtube.com/watch?v=zKUtDuiAISg',
        'https://www.youtube.com/watch?v=Yd5SkqSLmF8',
        'https://www.youtube.com/watch?v=MxK-hajSj9g',
        'https://www.youtube.com/watch?v=GBpgCTgAjEk',
        'https://www.youtube.com/watch?v=SAz1KJGCfkQ',
        'https://www.youtube.com/watch?v=QCRp8y98-7A',
        'https://www.youtube.com/watch?v=z_09oYZ9xCI'
    ]

    total_items = len(urls)

    start_index = int(input(f"İndirme işlemi hangi indeksten başlasın? (1-{total_items}): ")) - 1

    if not (0 <= start_index < total_items):
        print("Geçersiz başlangıç indeksi! İşlem sonlandırılıyor.")
        exit()

    with YoutubeDL(ydl_opts) as ydl:
        for index, url in enumerate(urls[start_index:], start=start_index + 1):
            try:
                info_dict = ydl.extract_info(url, download=False)
                print(f"[{index}/{total_items}]: {url} - {info_dict['title']}\n")
                ydl.download([url])
            except Exception as e:
                print(f"[{index}/{total_items}] Hata: {url} - {info_dict['title']} ({e})\n")
                exit()