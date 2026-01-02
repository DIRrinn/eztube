import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # buttons_names = ["Config", "Set Url", "Download", "Exit"]
        # Кнопатьки
        self.config_button = QPushButton('Config', self)
        self.set_url = QPushButton('Set Url', self)
        self.download = QPushButton('Download', self)
        self.exit = QPushButton('Exit', self)

        self.config_button.clicked.connect(self.on_config_clicked)
        self.set_url.clicked.connect(self.on_config_clicked)
        self.download.clicked.connect(self.on_config_clicked)
        self.exit.clicked.connect(self.on_config_clicked)

        # Создаем вертикальный layout и добавляем кнопку
        menu_widget = QListWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.config_button)
        layout.addWidget(self.set_url)
        layout.addWidget(self.download)
        layout.addWidget(self.exit)

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
