import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройка окна
        self.setFixedSize(500, 400)
        self.setWindowTitle("EZtube")

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Кнопатьки
        enter_url_button = QPushButton('Download', self)

        # URL textbox
        textbox = QLineEdit(self)
        textbox.setAlignment(Qt.AlignCenter)
        textbox.setPlaceholderText("URL")
        textbox.setFixedSize(350, 20)

        self.textbox_widget = QWidget()
        textbox_layout = QHBoxLayout()
        textbox_layout.setSpacing(5)
        self.textbox_widget.setLayout(textbox_layout)

        textbox_layout.addWidget(textbox)
        textbox_layout.addWidget(enter_url_button)
        
        # video res list
        self.options_widget = QWidget()
        options_layout = QGridLayout()
        options_layout.setRowStretch(4, 1)
        self.options_widget.setLayout(options_layout)

        label = QLabel("Resolution")
        label.setMargin(0)

        self.combobox_res = QComboBox(self)
        self.combobox_res.addItems(["360p", "480p", "720p", "1080", "Highest"])

        only_audio_checkbox = QCheckBox("Only audio")
        only_audio_checkbox.stateChanged.connect(self.change_format)

        self.directory = QPushButton("Select Directory")
        self.directory.clicked.connect(self.set_directory)

        options_layout.addWidget(label, 0, 0)
        options_layout.addWidget(self.combobox_res, 1, 0)
        options_layout.addWidget(only_audio_checkbox, 2, 0)
        options_layout.addWidget(self.directory)

        self.addWidgets()

    def addWidgets(self):
        self.layout.addWidget(self.textbox_widget)
        self.layout.addWidget(self.options_widget)

    def set_directory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.directory.setText(file)

    def change_format(self, state):
        if state == Qt.Checked:
            self.combobox_res.setEnabled(False)
        else:
            self.combobox_res.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
