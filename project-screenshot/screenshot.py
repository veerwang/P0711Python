import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap, QScreen, QCursor
from PyQt5.QtCore import Qt, QRect

class ScreenshotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Screenshot with Mouse Position')
        self.setGeometry(100, 100, 800, 600)
        self.button = QPushButton('Capture Screenshot', self)
        self.button.clicked.connect(self.captureScreen)
        self.button.resize(self.button.sizeHint())
        self.button.move(350, 300)

    def captureScreen(self):
        cursor = QCursor()
        position = cursor.pos()
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        print(QApplication.desktop().winId())
        
        # Define the size of the screenshot around the cursor
        screenshot_size = 100  # This defines a 100x100 pixel area around the cursor
        left = position.x() - screenshot_size // 2
        top = position.y() - screenshot_size // 2
        right = left + screenshot_size
        bottom = top + screenshot_size

        # Ensure the rectangle is within the screen bounds
        available_geometry = screen.availableGeometry()
        left = max(left, available_geometry.left())
        top = max(top, available_geometry.top())
        right = min(right, available_geometry.right())
        bottom = min(bottom, available_geometry.bottom())

        # Capture the area around the cursor
        area = QRect(left, top, right - left, bottom - top)
        screenshot = screenshot.copy(area)

        # Save the screenshot
        screenshot.save('mouse_position_screenshot.png', 'PNG')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ScreenshotWindow()
    mainWin.show()
    sys.exit(app.exec_())
