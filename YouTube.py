#need to install pytube to use the script : pip3 install pytube
import pytube
from pytube import YouTube

 
link = input('Enter the link: ') #asking the link 
yt = YouTube(link,on_progress_callback=progress_Check)
VideoOrAudio = input("Are you downloading  1.a video or 2.an audio (enter 1 or 2): ") #asking if you are downloading an audio or a video
#resolution = input("Enter the resolution") #asking the resolution
if VideoOrAudio == "1":
  yt.streams.filter(file_extension='mp4') 
  yt.streams.filter(res="1080p")
  stream = yt.streams.get_by_itag(22)
  stream.download()

if VideoOrAudio == "2":
  yt.streams.filter(only_audio=True) 
  stream = yt.streams.get_by_itag(22)
  stream.download()
