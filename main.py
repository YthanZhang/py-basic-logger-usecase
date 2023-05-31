import logging
import datetime
import sys
import os


def logger_init(name: str,
                file_level: int | str = logging.DEBUG,
                stream_level: int | str = logging.WARNING,
                ) -> logging.Logger:
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-3.3s]  %(message)s")

    date_str_format = "%Y_%m_%d"
    time_str_format = "%H_%M_%S_%f"

    log_directory = f"{datetime.date.today().strftime(date_str_format)}"
    os.makedirs(log_directory, exist_ok=True)

    file_handler = logging.FileHandler(
        f"{log_directory}/"
        f"{datetime.datetime.now().time().strftime(time_str_format)}.log")
    file_handler.setLevel(file_level)
    file_handler.setFormatter(log_formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(stream_level)
    stream_handler.setFormatter(log_formatter)

    logger_base = logging.getLogger(name)
    logger_base.setLevel(logging.DEBUG)
    logger_base.addHandler(stream_handler)
    logger_base.addHandler(file_handler)

    return logger_base


if __name__ == '__main__':
    logger = logger_init("Logger", logging.DEBUG, logging.WARNING)

    logger.info("This is info")
    logger.warning("This is warning")
    logger.debug("This is debug")
    logger.error("This is error")
