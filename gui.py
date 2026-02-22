import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import download

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройка окна
        self.setFixedSize(500, 560)
        self.setWindowTitle("EZtube")

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Кнопатьки
        enter_url_button = QPushButton('Download', self)

        # URL textbox
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("URL")
        self.textbox.returnPressed.connect(self.change_url)

        self.textbox_widget = QWidget()
        textbox_layout = QHBoxLayout()
        self.textbox_widget.setLayout(textbox_layout)

        textbox_layout.addWidget(self.textbox)
        textbox_layout.addWidget(enter_url_button)
        
        # video res list
        self.options_widget = QWidget()
        options_layout = QGridLayout()
        options_layout.setRowStretch(5, 1)
        self.options_widget.setLayout(options_layout)

        self.enter_url_label = QLabel("Enter Video URL:")
        label = QLabel("Resolution")

        self.combobox_res = QComboBox(self)
        self.combobox_res.addItems(["360p", "480p", "720p", "1080", "Highest"])

        only_audio_checkbox = QCheckBox("Only audio")
        only_audio_checkbox.stateChanged.connect(self.change_format)

        self.directory = QPushButton("Select Directory")
        self.directory.clicked.connect(self.set_directory)

        self.about_button = QPushButton("About")
        self.about_button.setFixedWidth(60)
        self.about_button.clicked.connect(self.show_about)

        self.video_title = QLabel("Video Title Here")
        self.video_title.setWordWrap(True)

        self.image = QImage()
        self.video_thumbnail = QLabel()
        pixmap = QPixmap('absolute_cinema.jpg')
        pixmap = pixmap.scaled(360, 360, Qt.KeepAspectRatio)
        self.video_thumbnail.setPixmap(pixmap)

        options_layout.addWidget(self.video_thumbnail)
        options_layout.addWidget(self.video_title)
        options_layout.addWidget(self.directory)
        options_layout.addWidget(label)
        options_layout.addWidget(self.combobox_res)
        options_layout.addWidget(only_audio_checkbox)

        self.addWidgets()

    def show_about(self, checked):
        w = QMessageBox()
        w.setWindowTitle("About")
        w.setFixedWidth(500)
        w.setText('<a href="https://github.com/DIRrinn/eztube">https://github.com/DIRrinn/eztube</a>')
        w.setInformativeText("Created by DIRrinn")
        x = w.exec_()

    def addWidgets(self):
        self.layout.addWidget(self.enter_url_label)
        self.layout.addWidget(self.textbox_widget)
        self.layout.addWidget(self.options_widget)
        self.layout.addWidget(self.about_button)

    def set_directory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.directory.setText(file)

    def change_format(self, state):
        if state == Qt.Checked:
            self.combobox_res.setEnabled(False)
        else:
            self.combobox_res.setEnabled(True)

    def change_url(self):
        url = self.textbox.text()
        if url != "":
            self.video_title.setText(download.get_title(url))
            self.image.loadFromData(requests.get(download.get_thumbnail(url)).content)
            pixmap = QPixmap(self.image)
            pixmap = pixmap.scaled(450, 500, Qt.KeepAspectRatio)
            self.video_thumbnail.setPixmap(pixmap)
        else:
            self.video_title.setText("Invalid URL")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
