import logging

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter('!!!!!%(asctime)%s - %(levelname)%s - %(message)%s')

logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)%s - %(levelname)%s - %(message)%s',
                    handlers=[
                        logging.StreamHandler(),  # v konsole
                        logging.FileHandler('example.log'),
                        f_handler.setFormatter
                    ])

logger = logging.getLogger(__name__)
logger.debug("DEBUG")
logger.debug("INFO")
logger.debug("ERROR")
