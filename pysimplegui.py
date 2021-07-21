#need PySimpleGui to run
import PySimpleGUI as sg 
sg.theme('SystemDefault') 
layout = [[sg.Text('Welcome in youtube-downloader.py:'),
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Text('Your typed characters appear here:'),
           sg.Text(size=(15,1), key='-OUTPUT-')]
          [sg.Input(key='-IN-')],
          [sg.Button('Download'), sg.Button('Exit')]]
  
