from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel , QVBoxLayout , QHBoxLayout , QPushButton , QListWidget , QWidget , QFileDialog
import glob
import pyglet
import eyed3
player = ''
song = ''

app = QApplication([])

main = QVBoxLayout()
name = QLabel()
button_l = QHBoxLayout()
play = QPushButton('PLAY')
stop = QPushButton('STOP')
button_l.addWidget(play)
button_l.addWidget(stop)
main.addWidget(name)
main.addLayout(button_l)
list = QListWidget()
open = QPushButton('OPEN FOLDER')
main.addWidget(list)
main.addWidget(open)
win = QWidget()
win.resize(300 , 300)
win.setLayout(main)
win.show()

def connect():
    open.clicked.connect(dir)
    list.clicked.connect(click)
    stop.clicked.connect(pause)
    play.clicked.connect(plaay)

def dir():
    temp = QFileDialog.getExistingDirectory()
    data = temp.split('/')
    dir = ''
    for i in data:
        if dir == '':
            dir = i
        else:
            dir = dir + '\\' + i

    print(dir)
    for i in glob.iglob(dir + '\\*.mp3'):
        list.addItem(i)

def click():
    global song , player
    player = pyglet.media.Player()
    song = pyglet.media.load(list.currentItem().text())
    audio = None
    audio = eyed3.load(list.currentItem().text())
    try:
        text = 'NAME: ' + audio.tag.title+ '\nARTIST: ' + audio.tag.artist + '\nALBUM: ' + audio.tag.album
    except:
        text = list.currentItem().text()
    name.setText(text)
    player.queue(song)
    player.play()


def pause():
    global  player
    player.pause()

def plaay():
    global  player
    player.play()

if __name__ == '__main__':
    connect()
    app.exec_()