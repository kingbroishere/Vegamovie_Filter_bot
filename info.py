import re
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')


def is_enabled(key, default):
    value = environ.get(key)
    if value is None:
        return default
    value = value.lower()
    return value in ["true", "yes", "1", "enable", "y"]


# Session & Bot Credentials
SESSION = getenv('SESSION', 'Media_search')
API_ID = int(getenv('API_ID', '21694834'))
API_HASH = getenv('API_HASH', '4c8b099a16e43829cf40a9780acd52b1')
BOT_TOKEN = getenv('BOT_TOKEN', '')

# Admins and Channels
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in getenv('ADMINS', '6007179358').split()]
USERNAME = getenv('USERNAME', "https://t.me/GIFT0NTON")  # ADMIN USERNAME
LOG_CHANNEL = int(getenv('LOG_CHANNEL', '-1002894286980'))
MOVIE_GROUP_LINK = getenv('MOVIE_GROUP_LINK', 'https://t.me/+PW_MtYXtAKZkYTU9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in getenv('CHANNELS', '-1003034407154').split()]

# Database Config
DATABASE_URI = getenv('DATABASE_URI', "mongodb+srv://creatingking7_db_user:<db_password>@cluster0.lw5qo5n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = getenv('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = getenv('COLLECTION_NAME', 'lazyfilesx')

MULTIPLE_DATABASE = is_enabled('MULTIPLE_DATABASE', True)
F_DB_URI = getenv('F_DB_URI', "mongodb+srv://prrajputtt148_db_user:XNRIqkksM9BfJFhW@cluster0.0yyy7ln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
S_DB_URI = getenv('S_DB_URI', "mongodb+srv://nrrajputt_db_user:k6EhdmWedoKZ0FFs@cluster0.aqodzad.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Log and Delete Channels
LOG_API_CHANNEL = int(getenv('LOG_API_CHANNEL', '-1002894286980'))
DELETE_CHANNELS = int(getenv('DELETE_CHANNELS', '-1003037072038'))
LOG_VR_CHANNEL = int(getenv('LOG_VR_CHANNEL', '-1002084819782'))
auth_channel = getenv('AUTH_CHANNEL', '-1002564847154')
SUPPORT_GROUP = int(getenv('SUPPORT_GROUP', '-1002987699696'))
request_channel = getenv('REQUEST_CHANNEL', 'LOG_CHANNEL')
MOVIE_UPDATE_CHANNEL = int(getenv('MOVIE_UPDATE_CHANNEL', '-1002943155574'))
SUPPORT_CHAT = getenv('SUPPORT_CHAT', 'https://t.me/+_6ywcJKlLMUyZGM1')

# Verification
IS_VERIFY = is_enabled('IS_VERIFY', True)

# Tutorial Links
TUTORIAL = getenv("TUTORIAL", "https://t.me/c/2437541681/364")
TUTORIAL_2 = getenv("TUTORIAL_2", TUTORIAL)
TUTORIAL_3 = getenv("TUTORIAL_3", TUTORIAL)
VERIFY_IMG = getenv("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

# Shorteners
SHORTENER_API = getenv("SHORTENER_API", "")
SHORTENER_WEBSITE = getenv("SHORTENER_WEBSITE", 'devreview.online')
SHORTENER_API2 = getenv("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = getenv("SHORTENER_WEBSITE2", 'devreview.online')
SHORTENER_API3 = getenv("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = getenv("SHORTENER_WEBSITE3", 'devreview.online')
TWO_VERIFY_GAP = int(getenv('TWO_VERIFY_GAP', "0"))
THREE_VERIFY_GAP = int(getenv('THREE_VERIFY_GAP', "43200"))

# Static Filters
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi", "marathi"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [str(i) for i in range(2025, 2002, -1)]
SEASONS = [f'season {i}' for i in range(1, 23)]

# Referral & Points
REF_PREMIUM = 10
PREMIUM_POINT = 100

# Safe conversions
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# Image Links
START_IMG = getenv('START_IMG', 'https://envs.sh/itN.jpg').split()
FORCESUB_IMG = getenv('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = getenv("REFER_PICS", "https://envs.sh/PSI.jpg").split()
PAYPICS = getenv('PAYPICS', 'https://envs.sh/tYV.jpg').split()
SUBSCRIPTION = getenv('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg')
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]

# Settings
FILE_AUTO_DEL_TIMER = int(getenv('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True)
PORT = getenv('PORT', '5000')
MAX_BTN = int(getenv('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(getenv('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', True)
FILE_CAPTION = getenv('FILE_CAPTION', script.FILE_CAPTION)
IMDB_TEMPLATE = getenv('IMDB_TEMPLATE', script.IMDB_TEMPLATE_TXT)
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', True)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

STREAM_MODE = is_enabled('STREAM_MODE', False)
MULTI_CLIENT = True
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(getenv("PING_INTERVAL", "1200"))

ON_HEROKU = 'DYNO' in environ
URL = getenv("FQDN", "")

# Settings dictionary
SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': IMDB_TEMPLATE,
    'caption': FILE_CAPTION,
    'tutorial': TUTORIAL,
    'tutorial_2': TUTORIAL_2,
    'tutorial_3': TUTORIAL_3,
    'shortner': SHORTENER_WEBSITE,
    'api': SHORTENER_API,
    'shortner_two': SHORTENER_WEBSITE2,
    'api_two': SHORTENER_API2,
    'log': LOG_VR_CHANNEL,
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY,
    'verify_time': TWO_VERIFY_GAP,
    'shortner_three': SHORTENER_WEBSITE3,
    'api_three': SHORTENER_API3,
    'third_verify_time': THREE_VERIFY_GAP
}

# Admin and User Commands
admin_cmds = [
    "/add_premium", "/premium_users", "/remove_premium", "/add_redeem",
    "/refresh", "/set_muc", "/pm_search_on", "/pm_search_off",
    "/set_ads", "/del_ads", "/setlist", "/clearlist",
    "/verify_id", "/index", "/send", "/leave",
    "/ban", "/unban", "/broadcast", "/grp_broadcast",
    "/delreq", "/channel", "/del_file", "/delete",
    "/deletefiles", "/deleteall",
    "All These Commands Can Be Used Only By Admins.",
    "⚡ powered by @vegmoviesnewin"
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "Get Top Trending Button List"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Current Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]

# Assign
