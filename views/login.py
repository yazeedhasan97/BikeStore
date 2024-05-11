import re

from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtGui import QIcon, QAction
# from cryptography.fernet import Fernet
from sqlalchemy import func

from common import consts
from controllers.controller import AppController
from models.models import User
from utilities.utils import RememberMe
from views.customes import QClickableLabel
from views.mainapp import MainApp


# this code has the minimum memory usage and the highest performance
class ForgetPasswordForm(QWidget):
    """ This "window" is a QWidget. If it has no parent, it will appear as a free-floating window as we want.
    """

    def __init__(self, ):
        super(ForgetPasswordForm, self).__init__()
        self.__init_ui()

        layout = QGridLayout()

        label_name = QLabel('Email')
        label_name.setStyleSheet(consts.GENERAL_QLabel_STYLESHEET)
        layout.addWidget(label_name, 0, 0)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(consts.GENERAL_QLineEdit_STYLESHEET)
        self.lineEdit_username.setPlaceholderText('Please enter your email...')
        layout.addWidget(self.lineEdit_username, 0, 1, )

        button_check = QPushButton('Check')
        button_check.adjustSize()
        button_check.setStyleSheet(consts.GENERAL_QPushButton_STYLESHEET)

        button_check.clicked.connect(self.check_password)
        layout.addWidget(button_check, 1, 1, )

        button_back = QPushButton('Back')
        button_back.adjustSize()
        button_back.setStyleSheet(consts.GENERAL_QPushButton_STYLESHEET)
        button_back.clicked.connect(self.return_to_login_page)
        layout.addWidget(button_back, 1, 0, 1, 1)

        # layout.setRowMinimumHeight(10, 75)
        layout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(layout)

    def __init_ui(self):
        self.setWindowTitle(consts.APP_NAME + ' -- Forget Password Form')
        height = consts.FORGET_PASSWORD_SCREEN_HEIGHT
        width = consts.FORGET_PASSWORD_WIDTH
        self.resize(width, height)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)

        self.setMinimumWidth(width)
        self.setMaximumWidth(width)

        pass

    def check_password(self):
        msg = QMessageBox()
        email = self.lineEdit_username.text().lower()
        if email is None or email == '':
            msg.setText('Please enter an email to validate.')
            msg.exec()
            return

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            msg.setText('Text must be in an email format.')
            msg.exec()
            return

        user = AppController.db_fac.session.query(User).filter(
            func.lower(User.email) == email.lower(),  # PK
        ).first()

        if user:
            msg.setText('You will receive an email with the details.')
            msg.exec()
            # TODO: call the email API here to send email.
            AppController.emailer.send_email(
                "Forget Password Remembered",
                f"Your current password for the email '{user.email}' is: {user.password}",
                receivers=[user.email],
                # receivers=["osama2003issa@gmail.com", 'Ammarkden@outlook.com', 'M.abuzaineh@harmonysaudi.com'],
            )
        else:
            msg.setText("Could not find this user in the system.")
            msg.exec()
            return

    def return_to_login_page(self):
        LoginForm(state='reverse').show()
        self.hide()
        self.destroy()
        self.close()
        pass


class LoginForm(QWidget):
    def __init__(self, state=None):
        super(LoginForm, self).__init__()
        self.__init_ui()
        self.screen = None
        AppController.logger.info('Starting the loging success')
        self._remember_object = RememberMe(
            path=consts.REMEMBER_ME_FILE_PATH,
            # key=Fernet.generate_key()
        )
        AppController.logger.info('Created the remember me object success')
        layout = QGridLayout()

        label_name = QLabel('Email')
        label_name.setStyleSheet(consts.GENERAL_QLabel_STYLESHEET)
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(consts.GENERAL_QLineEdit_STYLESHEET)
        self.lineEdit_username.setPlaceholderText('Please enter your email...')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1, 1, 3, )

        label_password = QLabel('Password')
        label_password.setStyleSheet(consts.GENERAL_QLabel_STYLESHEET)
        self.lineEdit_password = QLineEdit()

        self.lineEdit_password.setStyleSheet(consts.GENERAL_QLineEdit_STYLESHEET)
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password...')

        self.__show_pass_action = QAction(QIcon(consts.UNHIDDEN_EYE_ICON_PATH), 'Show password', self)
        self.__show_pass_action.setCheckable(True)
        self.__show_pass_action.toggled.connect(self.show_password)  # connect to the event observer and execution
        self.lineEdit_password.addAction(self.__show_pass_action, QLineEdit.ActionPosition.TrailingPosition)

        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1, 1, 3, )

        self.remember_me = QCheckBox('Remember me')
        self.remember_me.setStyleSheet(consts.SMALLER_QLabel_STYLESHEET)
        layout.addWidget(self.remember_me, 2, 0)

        label_forget_password = QClickableLabel('Forget Password?', self.forget_password, )
        label_forget_password.setStyleSheet(consts.SMALLER_QLabel_STYLESHEET)
        layout.addWidget(label_forget_password, 2, 3)

        button_login = QPushButton('Login')
        button_login.setStyleSheet(consts.GENERAL_QPushButton_STYLESHEET)
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 3, 0, 1, 4, )

        layout.setRowMinimumHeight(2, 150)
        layout.setContentsMargins(15, 25, 15, 25)
        self.setLayout(layout)

        if state is None:
            self.__try_remember_me_login()

    def show_password(self, ):
        if self.lineEdit_password.echoMode() == QLineEdit.EchoMode.Normal:
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.__show_pass_action.setIcon(QIcon(consts.UNHIDDEN_EYE_ICON_PATH))
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.__show_pass_action.setIcon(QIcon(consts.HIDDEN_EYE_ICON_PATH))

    def __init_ui(self):
        self.setWindowTitle(consts.APP_NAME + ' -- Login')
        height = consts.LOGIN_SCREEN_HEIGHT
        width = consts.LOGIN_SCREEN_WIDTH
        self.resize(width, height)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)

        self.setMinimumWidth(width)
        self.setMaximumWidth(width)

        pass

    def check_password(self):

        msg = QMessageBox()
        email = self.lineEdit_username.text().lower()
        password = self.lineEdit_password.text()
        if email is None or not email:
            msg.setText('Please enter an email.')
            msg.exec()
            return

        if password is None or not password:
            msg.setText('Please enter a password.')
            msg.exec()
            return

        # REGEX [regular expression]: do the basic text processing, check if the email format is valid
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            msg.setText('Email must be in an email format.')
            msg.exec()
            return

        user = self.__load_user_data(email, password)

        # Serialization: Communication/Storage formate between API and different programs
        #  = STRING
        #  - JSON
        #  - XML
        #  - YAML
        #  = Binary
        #      - h5
        #      - pkl - differ per language - local to the application
        #      - feather

        # binary serialization -- Python
        #  - Doesn't support composition serialization
        #  - Nested function/method

        #  Why we use serialization string formatted configuration ?
        #   - because it can serve as centralized config for all the APIs and tool contributes to the project

        if self.remember_me.isChecked():
            # we can do it in two ways
            # 1- db
            # 2- serialization binary

            self._remember_object.remember_user({
                'email': user.email,
                'password': user.password,
            })

            pass

        print('done checking')
        self.next_screen(user)

    def forget_password(self, event):
        self.screen = ForgetPasswordForm()
        self.screen.show()
        self.hide()
        self.destroy()
        self.close()

    def __load_user_data(self, email, password, remember_me=False):
        user = AppController.db_fac.session.query(User).filter(
            User.email == email,  # PK
        ).first()

        msg = QMessageBox()
        if user:
            AppController.logger.info(f"user found is {user}")

            if password != user.password:
                if not remember_me:
                    AppController.logger.warning("Password is incorrect.")
                    msg.setText("Password is incorrect.")
                else:
                    AppController.logger.warning("Password was changed for the remember_me behavior")
                    msg.setText("Password was changed since last remember me.")
                msg.exec()
                return False
            return user
        else:
            AppController.logger.warning(f"User not found in the database.")

            msg.setText(f"User {email} not found in the database.")
            msg.exec()
            return False

    def __try_remember_me_login(self, ):
        msg = QMessageBox()
        data = self._remember_object.get_user()

        if data:
            user = self.__load_user_data(
                email=data['email'],
                password=data['password'],
                remember_me=True,
            )
        else:
            msg.setText("Could not load pre-saved user.")
            msg.exec()
            return

        self._remember_object.remember_user({
            'email': user.email,
            'password': user.password,
        }, )
        self.next_screen(user)
        return True

    def next_screen(self, user):
        self.screen = MainApp(
            user=user,
        )
        self.screen.show()

        self.hide()
        self.destroy()
        self.close()
        pass
