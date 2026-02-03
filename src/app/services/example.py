import logging

logger = logging.getLogger("app.services.example")


def string_upper(value: str) -> str:
    logger.info("Transforming string")
    return value.upper()
