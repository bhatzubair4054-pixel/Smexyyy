import os

API_ID = int(os.getenv("API_ID", "38641461"))
API_HASH = os.getenv("API_HASH", "5fa11f53519d40359344a7e01f85229d")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("ASSISTANT_SESSION") or os.getenv("STRING_SESSION")
MAIN_OWNER = int(os.getenv("OWNER_ID", "8690336358"))
DEPLOYED_OWNER_ID = int(os.getenv("OWNER_ID", "8690336358"))
SEARCH_API_URL = os.getenv("SEARCH_API_URL", "https://search-api.kustbotsweb.workers.dev")
DOWNLOAD_API_BASE = os.getenv("DOWNLOAD_API_BASE", "").rstrip("/")
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")
YOUTUBE_COOKIES = os.getenv("YOUTUBE_COOKIES", "")
RATE_LIMIT_COUNT = 4
RATE_LIMIT_WINDOW = 6
MAX_TITLE_LEN = 30
PORT = int(os.getenv("PORT", "8080"))
