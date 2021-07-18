from PyQt5.QtWidgets import QApplication, QWidget
import sys

#Subclass QMainWindow to customize the main window
class MainWindow(QMainWindow):
  def _init_(self):
    super()._init_()
    
    self.setWindowTitle("Youtube Downloader Py") #assign a name to the window
    button = QPushButton("Download") #create a button
    
    self.setCentralWidget(button)
    
app = QApplication(sys.argv) # Pass in sys.argv to allow command line arguments


window = QMainWindow() #create a window and say what there is in it
window.show() #show the window


app.exec() #start the event loop
