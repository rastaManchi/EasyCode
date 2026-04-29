from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
import sys

application = QApplication(sys.argv)
window = QWidget()

media_player = QMediaPlayer()
video_widget = QVideoWidget()

video_widget.resize(800, 600)

audio_output = QAudioOutput()

media_player.setAudioOutput(audio_output)
media_player.setVideoOutput(video_widget)

layout = QVBoxLayout()
layout.addWidget(video_widget)
window.setLayout(layout)

media = QUrl.fromLocalFile('video.mp4')
media_player.setSource(media)

window.show()

media_player.play()
audio_output.setVolume(0.01)

application.exec()
