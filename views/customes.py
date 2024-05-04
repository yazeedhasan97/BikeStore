from PyQt6.QtWidgets import QLabel


class QClickableLabel(QLabel):
    def __init__(self, msg, when_clicked, parent=None):
        # QLabel.__init__(
        #     self,
        #     msg,
        #     parent=parent
        # )
        super().__init__(msg, parent=parent)
        self._when_clicked = when_clicked

    def mouseReleaseEvent(self, event):
        self._when_clicked(event)
