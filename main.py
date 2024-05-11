import logging
import os
import sys
from argparse import ArgumentParser

from PyQt6.QtWidgets import QApplication

from common import consts
from controllers.controller import AppController
from models.db import get_db_hook
from models.models import BASE
from utilities.loggings import MultipurposeLogger
from utilities.utils import load_json_file
from views.login import LoginForm


def main(args):
    logger = MultipurposeLogger(name=consts.APP_NAME.replace(" ", ""), path=args.log, create=True)
    logger.initialize_logger_handler(log_level=logging.DEBUG, max_bytes=int(5e+6), backup_count=50)

    AppController.logger = logger

    config = load_json_file(args.config)
    logger.info(f"Loaded config is: {config}")
    conn, fac = get_db_hook(config.get("database", {}), logger=logger, base=BASE)

    AppController.db_conn = conn
    AppController.db_fac = fac

    try:
        fac.create_tables()
    except Exception as e:
        logger.error(f"Unable to build the DB for the Application: {e}")
        raise Exception(f"Unable to build the DB for the Application: {e}")

    app = QApplication([])  # starts the observation cycle # the list can be empty
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


def cli():
    parser = ArgumentParser()
    parser.add_argument('--config', type=str, required=True, help="The path to the main config .json file.")
    parser.add_argument('--log', type=str, default='logs', help="The path to the log directory.")
    return parser.parse_args()


if __name__ == '__main__':
    args = cli()

    main(args)
