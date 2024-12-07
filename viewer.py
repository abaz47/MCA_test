from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget
)


FILENAME = "boltpattern.txt"


class Viewer(QWidget):
    WIDTH = 528
    HEIGHT = 346
    LABEL_WIDTH = 424
    BUTTON_WIDTH = 45
    BUTTON_HEIGHT = LABEL_HEIGHT = 45

    def __init__(self):
        super().__init__()

        self.setWindowTitle(FILENAME)
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        self.label = QLabel(FILENAME)
        self.label.setFixedSize(self.LABEL_WIDTH, self.LABEL_HEIGHT)
        self.driveButton = QPushButton()
        self.driveButton.setFixedSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.filterButton = QPushButton()
        self.filterButton.setFixedSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        self.text.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.text)
        self.load_text(FILENAME)

        mainLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()

        headerLayout.addWidget(self.label)
        headerLayout.addWidget(self.driveButton)
        headerLayout.addWidget(self.filterButton)

        mainLayout.addLayout(headerLayout)
        mainLayout.addWidget(self.scrollArea)

        self.setLayout(mainLayout)

    def load_text(self, file):
        with open(file, 'r') as file:
            self.text.setPlainText(file.read())


if __name__ == "__main__":
    app = QApplication([])
    viewer = Viewer()
    viewer.show()
    app.exec()
