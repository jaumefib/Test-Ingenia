from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QProgressBar, QVBoxLayout
from PyQt5.QtCore import QTimer


def create_buttons():
    global layout
    l = QHBoxLayout()

    start_button = QPushButton('Start')
    start_button.setMaximumSize(100, 35)
    l.addWidget(start_button)

    stop_button = QPushButton('Stop')
    stop_button.setMaximumSize(100, 35)
    l.addWidget(stop_button)
    l.setSpacing(80)
    layout.setSpacing(30)
    layout.addLayout(l)


# def advance_progress_bar():
#    curVal = p.value()
#    maxVal = p.maximum()
#    p.setValue(curVal + (maxVal - curVal) / 100)


def create_progress_bar():
    global layout
    progress_bar = QProgressBar()
    progress_bar.setRange(0, 5)
    progress_bar.setValue(1)

    # timer = QTimer()
    # timer.timeout.connect(advance_progress_bar(progress_bar))
    # timer.start(1)

    layout.addWidget(progress_bar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    create_progress_bar()
    create_buttons()

    window.setLayout(layout)
    window.resize(500, 300)
    window.setMaximumSize(500, 300)
    window.setMinimumSize(400, 100)
    window.setFixedSize(350, 150)
    window.move(300, 300)
    window.setWindowTitle('Exercise 2: Progress bar')
    window.show()
    app.exec_()
