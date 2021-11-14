from __future__ import unicode_literals
import os
import ffmpy
import youtube_dl
link = input('Enter the link: ')
'''
class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print("There was an error")
        print(msg)
'''
def hook(d):
    global filename
    filename = d['filename']
    if d['status'] == 'finished':
        print('Converting...')
    if d['status'] == 'downloading':
        print(str(d['downloaded_bytes']) + 'bytes ' + '/' + str(d['total_bytes']) + 'bytes' )


ydl_opts = {
    'format': 'bestaudio/best',
   # 'logger': Logger(),
    'progress_hooks': [hook],
   # 'outtmpl': '~/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

filename_final = filename.replace('.m4a','.mp4')
ff = ffmpy.FFmpeg(
    inputs={filename: None},
    outputs={filename_final: None}
)
ff.run()
os.remove(filename)


