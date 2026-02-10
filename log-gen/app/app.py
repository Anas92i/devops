import time
import random
import os
from logger import setup_logger

SERVICE_NAME = os.getenv("SERVICE_NAME", "log-generator")
INTERVAL = int(os.getenv("LOG_INTERVAL", "2"))

logger = setup_logger()

MESSAGES = {
    "INFO": [
        "Service running normally",
        "Heartbeat OK",
        "Processing data"
    ],
    "WARNING": [
        "High memory usage detected",
        "Slow response time"
    ],
    "ERROR": [
        "Failed to connect to database",
        "Unexpected exception occurred"
    ]
}

LEVELS = ["INFO", "WARNING", "ERROR"]

def generate_log():
    level = random.choice(LEVELS)
    message = random.choice(MESSAGES[level])

    if level == "INFO":
        logger.info(f"[{SERVICE_NAME}] {message}")
    elif level == "WARNING":
        logger.warning(f"[{SERVICE_NAME}] {message}")
    elif level == "ERROR":
        logger.error(f"[{SERVICE_NAME}] {message}")

if __name__ == "__main__":
    logger.info(f"Starting service: {SERVICE_NAME}")

    while True:
        generate_log()
        time.sleep(INTERVAL)
