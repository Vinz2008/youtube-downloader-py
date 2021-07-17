#need pyqt : pip3 install pyqt5

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv) #create an instance of QApplication

#Create an instance of the app gui
window = QWidget()
window.setWindowTitle('Youtube Downloader Py')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Welcome in Youtube Downloader Py!</h1>', parent=window)
helloMsg.move(60, 15)

window.show() #Show the gui
sys.exit(app.exec_()) #run the event loop (allows to cleanly exit and release memory ressource when the app terminates)
