
import os
os.system('pip3 install youtube-dl')
link = input('Enter the link: ')
command = "youtube-dl {} --verbose".format(link)
os.system(command)
