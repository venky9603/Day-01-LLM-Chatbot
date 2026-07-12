import os
from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


TEMPERATURE = float(
    os.getenv("TEMPERATURE", 0.3)
)

MAX_OUTPUT_TOKENS = int(
    os.getenv("MAX_OUTPUT_TOKENS", 512)
)

TOP_P = float(
    os.getenv("TOP_P", 0.9)
)

TOP_K = int(
    os.getenv("TOP_K", 40)
)


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY missing in .env file"
    )