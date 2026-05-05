from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QFileDialog
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
import sys


tracks = []
audio_output = QAudioOutput()
audio_output.setVolume(0.01)
media_player = QMediaPlayer()
media_player.setAudioOutput(audio_output)


def load_track():
    file, _ = QFileDialog.getOpenFileName(
        window,
        "Загрузить трек",
        "",
        "Audio Files (*.mp3)"
    )
    if file:
        track_name = file.split('/')[-1]
        track_list.addItem(track_name)
        tracks.append(file)
    
    

def play_track():
    selected_track = track_list.currentRow()
    if selected_track >= 0:
        file_path = tracks[selected_track]
        media_player.setSource(QUrl.fromLocalFile(file_path))
        media_player.play()
        
        
def stop_track():
    media_player.stop()



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Аудиоплеер')
window.resize(400, 300)

layout = QVBoxLayout()

load_btn = QPushButton("Загрузить трек")
load_btn.clicked.connect(load_track)

play_btn = QPushButton("Воспроизвести")
play_btn.clicked.connect(play_track)

stop_btn = QPushButton("Остановить")
stop_btn.clicked.connect(stop_track)

track_list = QListWidget()

layout.addWidget(load_btn)
layout.addWidget(track_list)
layout.addWidget(stop_btn)
layout.addWidget(play_btn)

window.setLayout(layout)

window.show()

app.exec()
