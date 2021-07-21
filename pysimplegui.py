#need PySimpleGui to run
import PySimpleGUI as sg 
#need to install pytube to use the script : pip3 install pytube
import pytube
from pytube import YouTube

sg.theme('SystemDefault') 
layout = [[sg.Text('Welcome in youtube-downloader.py:'),
           sg.Text(size=(15,1))],
          [sg.Text('Enter the url of the file you want to download:'),
           sg.Text(size=(15,1))]
          [sg.Input(key='url')],
          [sg.Button('Download'), sg.Button('Exit')]]

window = sg.Window('Youtube downloader py', layout)
event, values = window.read() #needed for doing events with things in the layout ex: if a button is clicked

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == download
        link=value["url"]
        yt = YouTube(link)
