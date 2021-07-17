import pytube
from pytube import YouTube
link = input(“Enter the link: “)
yt = YouTube(link)
VideoOrAudio = input("Are you downloading  1.an audio or 2.a video (enter 1 or 2)")
resolution = input("Enter the resolution")
if VideoOrAudio == "1";
  yt.streams.filter(res=resolution).first().download()

if VideoOrAudio == "2";
  yt.streams.filter(res=resolution).first().download()
  
