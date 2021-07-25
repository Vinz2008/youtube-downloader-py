import os
os.system('pip3 install youtube-dl')
link = input('Enter the link: ')
command = "youtube-dl -f bestaudio {} --verbose".format(link)
os.system(command)
