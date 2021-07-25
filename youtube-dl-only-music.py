import os
os.system('pip3 install youtube-dl')
link = input('Enter the link: ')
command = "youtube-dl -x --audio-format mp3 -f bestaudio {} --verbose".format(link)
os.system(command)
