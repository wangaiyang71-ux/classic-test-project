"""统一日志配置。"""

import logging

LOGGER_NAME = "classic_bank"


def get_logger() -> logging.Logger:
    """获取项目日志器；重复调用时不会重复添加 handler。"""
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
    )
    logger.addHandler(handler)
    logger.propagate = False
    return logger
