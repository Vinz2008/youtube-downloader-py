from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#need PySimpleGui to run
import PySimpleGUI as sg 
#need to install pytube to use the script : pip3 install pytube
import pytube
from pytube import YouTube

sg.theme('SystemDefault') 
layout = [[sg.Text('Welcome in youtube-downloader.py:'),
           sg.Text(size=(15,1))],
          [sg.Text('Enter the url of the file you want to download:'),
           sg.Text(size=(15,1))],
          [sg.Input(key='-URL-')],
          [sg.Text('Enter if you you want from where to where you want the video to be'),
           sg.Text(size=(15,1))],
          [sg.Text("Start"), sg.Input(key="-START-"), sg.Text("End"), sg.Input(key="-END-")],
          [sg.Button("Download"), sg.Button("Exit")]],

window = sg.Window('Youtube downloader py', layout)
event, values = window.read() #needed for doing events with things in the layout ex: if a button is clicked

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Download":
        link=values["-URL-"]
        yt = YouTube(link)
        title = yt.title
        yt.streams.filter(res="1080p")
        stream = yt.streams.get_by_itag(22)
        stream.download()
        start = values['-START-']
        end = values['-END-']
        if start:
            if end:
                start = int(start)                
                end = int(end)
                ffmpeg_extract_subclip("{}.mp4".format(title), start, end, targetname="{}.mp4".format(title))
