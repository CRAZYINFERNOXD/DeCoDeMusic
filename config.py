from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
DB_NAME = getenv("DB_NAME")
DB_URL = getenv("DB_URL")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeeCodeBots")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeeCodesupport")
BOT_USERNAME = getenv("BOT_USERNAME")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/a7c328b3efe86f520523c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/0514728ae86afc870d429.png")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
AUD_IMG = getenv("AUD_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")

admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

OWNER_ID = int(getenv("OWNER_ID"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
