import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '21694834'))
API_HASH = environ.get('API_HASH', '4c8b099a16e43829cf40a9780acd52b1')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6007179358').split()]
USERNAME = environ.get('USERNAME', "https://t.me/GIFT0NTON") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002894286980'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+PW_MtYXtAKZkYTU9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003034407154').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://creatingking7_db_user:<db_password>@cluster0.lw5qo5n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'lazyfilesx')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', True)) # Set True or False

# If Multiple Database Is True Then Fill All Three Below Database Uri Else You Will Get Error.
F_DB_URI = environ.get('F_DB_URI', "mongodb+srv://prrajputtt148_db_user:XNRIqkksM9BfJFhW@cluster0.0yyy7ln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # This Db Is For File Data Store
S_DB_URI = environ.get('S_DB_URI', "mongodb+srv://nrrajputt_db_user:k6EhdmWedoKZ0FFs@cluster0.aqodzad.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # This Db is for File Data Store When First Db Is Going To Be Full.


#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '--1002894286980'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1003037072038')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002084819782'))
auth_channel = environ.get('AUTH_CHANNEL', '-1002564847154')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002987699696'))
request_channel = environ.get('REQUEST_CHANNEL', 'LOG_CHANNEL') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002943155574')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+_6ywcJKlLMUyZGM1') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/c/2437541681/364")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/c/2437541681/364")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/c/2437541681/364")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "68cca3768689dc0402b9cbe64fb8ee3eea40acfe")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'devreview.online')
SHORTENER_API2 = environ.get("SHORTENER_API2", "68cca3768689dc0402b9cbe64fb8ee3eea40acfe")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'devreview.online')
SHORTENER_API3 = environ.get("SHORTENER_API3", "68cca3768689dc0402b9cbe64fb8ee3eea40acfe")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'devreview.online')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "0"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "43200"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi", "marathi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2025, 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 10
PREMIUM_POINT = 100
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://envs.sh/itN.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/tYV.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', True)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', True)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = True
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = True
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
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

admin_cmds = [
    "/add_premium", "/premium_users", "/remove_premium", "/add_redeem",
    "/refresh", "/set_muc", "/pm_search_on", "/pm_search_off",
    "/set_ads", "/del_ads", "/setlist", "/clearlist",
    "/verify_id", "/index", "/send", "/leave",
    "/ban", "/unban", "/broadcast", "/grp_broadcast",
    "/delreq", "/channel", "/del_file", "/delete",
    "/deletefiles", "/deleteall", 
    "All These Commands Can Be Used Only By Admins.", 
    "⚡ powered by @𝘃𝗲𝗴𝗮𝗺𝗼𝘃𝗶𝗲𝘀𝗻𝗲𝘄𝗶𝗻"
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]


if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI    # This Db is for User Data Store
    FILE_DB_URI = F_DB_URI        # This Db Is For File Data Store
    SEC_FILE_DB_URI = S_DB_URI    # This Db is for File Data Store When First Db Is Going To Be Full.


