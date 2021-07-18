#need to install pytube to use the script : pip3 install pytube
import pytube
from pytube import YouTube
link = input('Enter the link: ') #asking the link 
yt = YouTube(link) 
VideoOrAudio = input("Are you downloading  1.a video or 2.an audio (enter 1 or 2)") #asking if you are downloading an audio or a video
resolution = input("Enter the resolution") #asking the resolution
if VideoOrAudio == "1";
  yt.streams.filter(res=resolution , subtype = "mp4").first().download()

if VideoOrAudio == "2";
  yt.streams.filter(res=resolution , subtype = "mp3").first().download()
  
