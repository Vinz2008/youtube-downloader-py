import pytube
from pytube import YouTube
link = input(“Enter the link: “)
yt = YouTube(link)
resolution = input("Enter the resolution")
yt.streams.filter(res=resolution).first().download()
