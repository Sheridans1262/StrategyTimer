import datetime
import subprocess
import threading
import time
from datetime import datetime, timedelta

from playsound import playsound

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, QSize
import sys

import vlc


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(230, 80)
        self.setWindowTitle("GameTimer")

        mainLayout = QVBoxLayout()

        topGroup = QHBoxLayout()

        leftLabel = QLabel("Set timer for:")
        rightLabel = QLabel("min")

        self.input = QLineEdit(self)
        self.input.setFixedSize(QSize(100, 20))


        topGroup.addWidget(leftLabel)
        topGroup.addWidget(self.input)
        topGroup.addWidget(rightLabel)

        mainLayout.addLayout(topGroup)

        self.startButton = QPushButton("Start timer")
        self.startButton.clicked.connect(self.startLocalTimer)
        self.startButton.setDefault(True)
        mainLayout.addWidget(self.startButton)

        self.setLayout(mainLayout)

    def startLocalTimer(self):
        minutesToMidnight = self.input.text()
        try:
            minutesToMidnightInt = int(minutesToMidnight)

            if minutesToMidnightInt < 1:
                minutesToMidnightInt = 1

            timerThread = threading.Thread(target=self.workingTimer, args=(minutesToMidnightInt * 60,))
            timerThread.start()

            self.input.setEnabled(False)
            self.startButton.setEnabled(False)
        except ValueError:
            dialog = QMessageBox(parent=self, text="Wrong input")
            dialog.show()
            self.input.clear()

    def workingTimer(self, timeInSeconds):
        subprocess.call(f"schtasks /Delete /TN \"killCK3\" /F")
        subprocess.call(f"schtasks /Delete /TN \"killStellaris\" /F")
        subprocess.call(f"schtasks /Delete /TN \"killRimworld\" /F")

        currentTime = datetime.now()
        print(currentTime)
        taskkillDateTime = currentTime + timedelta(seconds=60)
        taskkillTime = f'{taskkillDateTime:%H:%M}'
        print(taskkillTime)

        subprocess.call(f"schtasks /Create /SC ONCE /ST {taskkillTime} /TN killCK3 /TR \"taskkill /f /im chrome.exe\"")
        subprocess.call(f"schtasks /Create /SC ONCE /ST {taskkillTime} /TN killCK3 /TR \"taskkill /f /im chrome.exe\"")
        subprocess.call(f"schtasks /Create /SC ONCE /ST {taskkillTime} /TN killCK3 /TR \"taskkill /f /im chrome.exe\"")
        # subprocess.call(f"schtasks /Create /SC ONCE /ST {taskkillTime} /TN killCK3 /TR \"taskkill /f /im chrome.exe & schtasks /Delete /TN killCK3 /F\"")


        # time.sleep(timeInSeconds - 60)
        #
        # player = vlc.MediaPlayer("NavalInvasionSound.mp3")
        # player.audio_set_volume(100)
        # player.play()
        #
        # time.sleep(60)
        # subprocess.call("TASKKILL /F /IM ck3.exe")
        # subprocess.call("TASKKILL /F /IM stellaris.exe")
        # subprocess.call("TASKKILL /F /IM rimworld.exe")


        self.input.setEnabled(True)
        self.startButton.setEnabled(True)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())