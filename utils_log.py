from loguru import logger
from sys import stderr 
from functools import wraps

logger.remove()

logger.add(stderr, format="{time} - {level} - {message}", level="INFO")

logger.add("etl.log", format="{time} - {level} - {message}", level="INFO")

def log_decorator(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executando função: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função {func.__name__} executada com sucesso.")
            return result
        except Exception as e:
            logger.error(f"Erro na função {func.__name__}: {e}")
            raise e
    return wrapper