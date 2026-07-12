import logging


# Configure application logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# Application logger
logger = logging.getLogger(__name__)


# Suppress Google Gemini SDK logs
logging.getLogger("google").setLevel(logging.ERROR)

# Suppress HTTP request logs from Gemini SDK
logging.getLogger("httpx").setLevel(logging.ERROR)

# Suppress lower-level transport logs
logging.getLogger("google.genai").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)