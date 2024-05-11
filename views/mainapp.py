from PyQt6.QtWidgets import QMainWindow

from common import consts


class MainApp(QMainWindow):

    def __init__(self, user=None):
        super(MainApp, self).__init__()
        self.__init_ui()
        self.user = user

    def __init_ui(self):
        self.setWindowTitle(consts.APP_NAME )
        height = consts.LOGIN_SCREEN_HEIGHT
        width = consts.LOGIN_SCREEN_WIDTH
        self.resize(width, height)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)

        self.setMinimumWidth(width)
        self.setMaximumWidth(width)

        pass