from loguru import logger


def string_upper(string: str) -> str:
    """Transforms the input string to upper case.

    :param string: input string.
    :type string: str
    :return: upper case string.
    :rtype: str
    """
    logger.info("Transforming string.")
    return string.upper()
