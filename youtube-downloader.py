
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#need PySimpleGui to run
import PySimpleGUI as sg 
import os
sg.theme('SystemDefault') 
layout = [[sg.Text('Welcome in youtube-downloader.py:'),
           sg.Text(size=(15,1))],
          [sg.Text('Enter the url of the file you want to download:'),
           sg.Text(size=(15,1))],
          [sg.Input(key='-URL-')],
          [sg.Button("Download")],
          [sg.Text('Enter if you you want from where to where you want the video to be'),
           sg.Text(size=(15,1))],
          [sg.Text("Start"), sg.Input(key="-START-"), sg.Text("End"), sg.Input(key="-END-")],
          [sg.Text("Enter the name of the file you just downloaded"), sg.Input(key="-TITLE-")],
          [sg.Button("Cut")],
          [sg.Button("Exit")]],

window = sg.Window('Youtube downloader py', layout)
event, values = window.read() #needed for doing events with things in the layout ex: if a button is clicked

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Download":
        link=values["-URL-"]
        os.system('pip3 install youtube-dl')
        command = "youtube-dl -f best {} --verbose".format(link)
        os.system(command)
    elif event == "Cut":        
        title = values['-TITLE-']
        start = values['-START-']
        end = values['-END-']
        start = int(start)                
        end = int(end)
        ffmpeg_extract_subclip("{}.mp4".format(title), start, end, targetname="{}.mp4".format(title))
