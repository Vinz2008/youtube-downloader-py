#need to install pytube to use the script : pip3 install pytube
import pytube
from pytube import YouTube

def progress_function(self,stream, chunk,file_handle, bytes_remaining):
  size = stream.filesize
  p = 0
  while p <= 100:
    progress = p
    print("%i %%" % progress)
    p = percent(bytes_remaining, size)

def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc
    
link = input('Enter the link: ') #asking the link 
yt = YouTube(link, on_progress_callback=progress_function)
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
 
def progress_function(self,stream, chunk,file_handle, bytes_remaining):
  
  size = stream.filesize
  p = 0
  while p <= 100:
    progress = p
    print("%i %%" % progress)
    h = bytes_remaining/size
    p = h * 100
