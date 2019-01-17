from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, \
    QProgressBar, QVBoxLayout
from PyQt5.QtCore import QTimer


class LoadingScreen(QWidget):
    def __init__(self, parent=None):
        super(LoadingScreen, self).__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        self.create_timer()
        self.create_progress_bar()
        self.create_buttons()

        self.setLayout(self.layout)
        self.resize(500, 300)
        self.setFixedSize(350, 150)
        self.move(300, 300)
        self.setWindowTitle('Exercise 2: Loading Screen')

    def create_timer(self):
        """
        Creates the timer and initializes the counter.
        """
        self.counter = 0
        self.timer = QTimer()

    def create_buttons(self):
        """
        Creates the two buttons (Start & Stop) and connects it with
        their corresponent action when clicked.
        """
        layout = QHBoxLayout()

        start_button = QPushButton('Start')

        def start_clicked():
            if self.counter == 0 or self.counter >= 5:
                self.counter = 0
                self.progress_bar.setValue(0)
                self.start_timer(self.timer_func)

        start_button.clicked.connect(start_clicked)
        start_button.setMaximumSize(100, 35)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop')

        def stop_clicked():
            self.counter = 0
            self.timer.stop()

        stop_button.clicked.connect(stop_clicked)
        stop_button.setMaximumSize(100, 35)
        layout.addWidget(stop_button)

        layout.setSpacing(80)
        self.layout.setSpacing(30)
        self.layout.addLayout(layout)

    def timer_func(self):
        """
        Updates the value of the progress bar.
        """
        cur_val = self.progress_bar.value()
        max_val = self.progress_bar.maximum()
        # The progress bar increments 1/5 every time timer_func is called
        self.progress_bar.setValue(cur_val + max_val/5)

    def start_timer(self, slot, count=5, interval=1000):
        """
        Starts the timer for the progress bar.
        :param slot: the function that is called  when the timer arrives
        at the end of the interval.
        :param count: number of calls to the function slot.
        :param interval: For starting the timer with a timeout interval
        of msec milliseconds.
        """
        self.counter = 0

        def handler():
            """
            Function that works as a counter.
            """
            self.counter
            self.counter += 1
            slot()
            if self.counter >= count:
                self.timer.stop()

        self.timer = QTimer()
        self.timer.timeout.connect(handler)
        self.timer.start(interval)

    def create_progress_bar(self):
        """
        Creates the progress bar
        """
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    app.exec_()
