import pytube
from pytube import YouTube
link = input(“Enter the link: “)
yt = YouTube(link)
yt.streams.filter(res="1080p").first().download()
