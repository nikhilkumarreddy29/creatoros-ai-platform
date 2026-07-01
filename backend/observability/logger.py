import structlog
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = structlog.get_logger()