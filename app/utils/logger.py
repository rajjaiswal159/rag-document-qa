import logging

# Configure the application's logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger for the current module
logger = logging.getLogger(__name__)