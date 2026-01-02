import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Кнопатьки
        self.config_button = QPushButton('Config', self)
        self.set_url = QPushButton('Set Url', self)
        self.download = QPushButton('Download', self)
        self.exit = QPushButton('Exit', self)

        self.config_button.clicked.connect(self.on_config_clicked)
        self.set_url.clicked.connect(self.on_config_clicked)
        self.download.clicked.connect(self.on_config_clicked)
        self.exit.clicked.connect(self.on_config_clicked)

        # Картинка
        self.image = QLabel(self)
        pixmap = QPixmap('/home/dirrinn/Images/Works/eztubelogo.png')
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
        self.image.setFixedSize(350, 250)
        self.image.setAlignment(Qt.AlignCenter)

        # Добавляем виджеты и настраиваем
        menu_widget = QListWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(2)

        layout.addWidget(self.image)
        layout.addWidget(self.config_button)
        layout.addWidget(self.set_url)
        layout.addWidget(self.download)
        layout.addWidget(self.exit)
        layout.addStretch(1)

        # Настройка окна
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("EZtube")

    def on_config_clicked(self):
        QMessageBox.information(self, 'Лолкек', 'Ты крутой, но тут ничего нет :(')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
