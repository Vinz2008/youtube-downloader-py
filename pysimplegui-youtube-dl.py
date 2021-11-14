from __future__ import unicode_literals
import ffmpy
import youtube_dl
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
          [sg.Text("",key="-CHARG-")],
          [sg.Text('Enter if you you want from where to where you want the video to be'),
           sg.Text(size=(15,1))],
          [sg.Text("Start"), sg.Input(key="-START-"), sg.Text("End"), sg.Input(key="-END-")],
          [sg.Text("Enter the name of the file you just downloaded"), sg.Input(key="-TITLE-")],
          [sg.Button("Cut")],
          [sg.Button("Exit")]],

window = sg.Window('Youtube downloader py', layout)
event, values = window.read() #needed for doing events with things in the layout ex: if a button is clicked
def hook(d):
    global filename
    filename = d['filename']
    if d['status'] == 'finished':
        print('Converting...')
    if d['status'] == 'downloading':
        print(str(d['downloaded_bytes']) + 'bytes ' + '/' + str(d['total_bytes']) + 'bytes' )

ydl_opts = {
    'format': 'bestaudio/best',
    'progress_hooks': [hook],
    'outtmpl': '~/%(extractor)s-%(id)s-%(title)s.%(ext)s',
}

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Download":
        window["-CHARG-"].update("Chargement")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        filename_final = filename.replace('.m4a','.mp4')
        ff = ffmpy.FFmpeg(
            inputs={"~/" filename: None},
            outputs={"~/" + filename_final: None}
        )
        ff.run()
        os.remove(~/filename)
        window["-CHARG-"].update("Finished")
    elif event == "Cut":        
        title = values['-TITLE-']
        start = values['-START-']
        end = values['-END-']
        st = int(start)                
        end = int(end)
        
