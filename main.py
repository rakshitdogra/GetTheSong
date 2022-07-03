# © rakshitdogra
# rakshitdogra
# RAKSHIT DOGRA
# SONG DOWNLOADER

import urllib.request
import re
from pytube import YouTube
import os
searchquery=input("Search without space: \n>> ")
search_keyword=searchquery
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
genlink =("https://www.youtube.com/watch?v=" + video_ids[0])
yt=genlink
print("Link:",genlink)
yt = YouTube(genlink)
video = yt.streams.filter(only_audio=True).first()
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")
