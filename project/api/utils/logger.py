from loguru import logger

# Logging with string allignment
time = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>'
level = "<level>{level: ^18}</level>"
function = "<cyan>{name: <32}</cyan>:<cyan>{function: ^30}</cyan>:<cyan>{line: 5}</cyan>"
message = "<bold>{message}</bold>"

DEFAULT_FORMAT = ' | '.join([time, level, function, message])


# Personalized logging
def log_request(
        level: str, method: str, id: str, ip: str, endpoint: str,
        tempo: str = None, local: bool = False):
    message = f"{method: ^4} | ENDPOINT: {endpoint: ^20}"
    if not local:
        message = f"{method: ^4} | ID: {id: <36} | IP: {ip: ^16} | ENDPOINT: {endpoint: ^20}"
    if tempo:
        message = ' | '.join([message, f"TIME: {tempo}"])
    logger.log(level, message)