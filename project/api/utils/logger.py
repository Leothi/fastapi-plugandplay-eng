from loguru import logger

# Logging with string allignment
time = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>'
level = "<level>{level: ^18}</level>"
function = "<cyan>{name: <30}</cyan>:<cyan>{function: ^30}</cyan>:<cyan>{line: 5}</cyan>"
message = "<bold>{message}</bold>"

DEFAULT_FORMAT = ' | '.join([time, level, function, message])


# Personalized logging
def log_request(level: str, method: str, endpoint: str, time: str = None):
    message = f"{method: ^4} | ENDPOINT: {endpoint: ^20}"
    if time:
        message = ' | '.join([message, f"TIME: {time}"])
    logger.log(level, message)
