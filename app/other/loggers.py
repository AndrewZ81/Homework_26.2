# Подключаем инструменты логирования
import logging

info_logger = logging.getLogger("info_logger")  # для успешного логирования
info_logger.setLevel(logging.INFO)
error_logger = logging.getLogger("error_logger")  # для логирования с ошибками
error_logger.setLevel(logging.ERROR)
post_handler = logging.FileHandler("logs/api.log", encoding="utf-8")
post_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
post_handler.setFormatter(post_formatter)
info_logger.addHandler(post_handler)
error_logger.addHandler(post_handler)
