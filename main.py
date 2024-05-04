import os
import sys

from PyQt6.QtWidgets import QApplication

from common import consts
from views.login import LoginForm


def main(args):
    app = QApplication(args)  # starts the observation cycle
    # MainController.store_screen_details(app.primaryScreen())

    try:  # safety measure
        form = LoginForm()  # build the entire form or GUI before showing it to the USR
        # lazy instantiation 1- Prepare/Load everything before show, 2- Take the first to load and save, then just load and show
        if not os.path.exists(consts.REMEMBER_ME_FILE_PATH):
            form.show()

    except Exception as e:
        print(e)
        raise e
    finally:
        pass
    code = app.exec()  # 0 means success -- non 0 means error usually 1+ -- less than 0 is human intentional error

    sys.exit(code)  # forcefully closing the program with the execution status/code


if __name__ == '__main__':
    main(sys.argv)
