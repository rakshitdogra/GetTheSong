#Copyright (c) © 2023 rakshitdogra

import urllib.request
import re
from pytube import YouTube
import os
import pyfiglet

print(pyfiglet.figlet_format("Get The Song"))
print("Copyright (c) © 2023 rakshitdogra")
print("\n")  

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    def audio():
        print(color.YELLOW + "\nTitle of the Video:",yt.title + color.END)
        print(color.BOLD + "\nEnter the destination (leave blank for current directory)" + color.END)
        destination = str(input(">> ")) or '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        rchoice= input("Do you want to rename file? (y/n)")
        if rchoice.lower() == "y":
            new_file_name = input(color.BOLD + "Enter the new file name: " + color.END)
            new_file = os.path.join(destination, new_file_name + ext)
            os.rename(out_file, new_file)
        elif rchoice.lower() == "n":
            os.rename(out_file, new_file)
        else:
            print("invalid input")
        print("\n")
        title=str(yt.title)
        print(color.CYAN + title + " has been successfully downloaded." + color.END)

    def video():
        print(color.YELLOW + "\nTitle of the Video:",yt.title + color.END)
        print(color.BOLD + "\nEnter the destination (leave blank for current directory)" + color.END)
        destination = str(input(">> ")) or '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        print("\n")
        title=str(yt.title)
        print(color.CYAN + yt.title + " has been successfully downloaded." + color.END)

    while True:  
        print("\n1. Using Search \n2. Using Url")
        choice = int(input("Enter the Choice (1 or 2): "))
        if choice == 1:
            withspace=input(color.CYAN +"\nSearch >> " + color.END)
            print(color.GREEN + "\nSearching........" + color.END)
            searchquery = withspace.replace(" ", "+")
            search_keyword=searchquery
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            genlink =("https://www.youtube.com/watch?v=" + video_ids[0])
            yt=genlink
            s=str(genlink)
            print(color.BLUE+"\nLink:"+ s +color.END)
            print("\n")

            print("1. Audio \n2. Video")
            select = int(input("Enter the Choice (1 or 2): "))
            if select == 1:
                yt = YouTube(genlink)
                video = yt.streams.filter(only_audio=True).first()
                audio()           
            elif select == 2:
                yt = YouTube(genlink)
                video = yt.streams.filter(only_video=True).first()
                video()
            else:
                print("\nInvaild input!") 
    
        elif choice == 2:  
            print("1. Audio \n2. Video")
            select2 = int(input("Enter the Choice (1 or 2): "))  
            if select2 == 1:
                urllink=input("\nEnter the url link of the video: \n>> ")
                yt = YouTube(urllink)
                video = yt.streams.filter(only_audio=True).first()
                audio()
            elif select2 == 2:
                urllink=input("\nEnter the url link of the video: \n>> ")
                yt = YouTube(urllink)
                video = yt.streams.filter(only_video=True).first()
                video()
            else:
                print("\nInvaild input!")
        else:
            print("\nInvaild input!")

        next_request = input("\nDo you want to use this script again? (yes/no): \n>> ")
        if next_request == "no":
            break

if __name__ == "__main__":
    main()
