"""
Arquivo para criar logs.
"""

import logging

FORMAT = "%(levelname)s - %(asctime)s - %(message)s"
logging.basicConfig(filename='log.log', 
                    level=logging.INFO, 
                    format=FORMAT
)

def log(status, user, message, resultado):

    match status:
        case "INFO":
            log_entry = f"{user} - {message} - Resultado: {resultado}"
            logging.info(log_entry)
        case "WARNING":
            log_entry = f"{user} - {message} - Resultado: {resultado}"
            logging.warning(log_entry)
        case "ERROR":
            log_entry = f"{user} - {message}"
            logging.error(log_entry)
