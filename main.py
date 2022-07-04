#Copyright (c) © 2022 rakshitdogra

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import urllib.request
import re
from pytube import YouTube
import os
import time
import sys
import pyfiglet

print(pyfiglet.figlet_format("Get The Song"))
print("\n")  

while True:  
    print("Search")
    print("1. Using Search")
    print("2. Using Url")  
    choice = int(input("Enter the Choice (1 or 2): "))

    if choice == 1:
       withspace=input("Search >> ")
       searchquery = withspace.replace(" ", "+")
       search_keyword=searchquery
       html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
       video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
       genlink =("https://www.youtube.com/watch?v=" + video_ids[0])
       yt=genlink
       print("\nLink:",genlink)
       yt = YouTube(genlink)
       video = yt.streams.filter(only_audio=True).first()
       print("\nEnter the destination (leave blank for current directory)")
       destination = str(input(">> ")) or '.'
       out_file = video.download(output_path=destination)
       base, ext = os.path.splitext(out_file)
       new_file = base + '.mp3'
       os.rename(out_file, new_file)
       print("\nDownloading:")
       animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]
       for i in range(len(animation)):
        time.sleep(0.05)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
       print("\n")
       print(yt.title + " has been successfully downloaded.")


    if choice == 2:
       urllink=input("\nEnter the url link of the video: \n>> ")
       yt = YouTube(urllink)
       video = yt.streams.filter(only_audio=True).first()
       print("\nEnter the destination (leave blank for current directory)")
       destination = str(input(">> ")) or '.'
       out_file = video.download(output_path=destination)
       base, ext = os.path.splitext(out_file)
       new_file = base + '.mp3'
       os.rename(out_file, new_file)
       print("Downloading:")
       animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]
       for i in range(len(animation)):
        time.sleep(0.05)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
       print("\n")
       print(yt.title + " has been successfully downloaded.")

    next_request = input("\nDo you want to use this script again? (yes/no): \n>> ")
    if next_request == "no":
        break
