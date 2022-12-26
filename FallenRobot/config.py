class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 18960528
    API_HASH = "cc0fff577b677c9b2b4de5dd5bc5dfd1"

    CASH_API_KEY = "XYZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://dydshiac:VBumDHnxyP2ox5QQjhsm8CcFr6CFGJKk@ella.db.elephantsql.com/dydshiac"  # A sql database url from elephantsql.com

    EVENT_LOGS = (1001839472020)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://2004:2004@cluster0.vugmi1n.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/d0bdb76513e424ecf2347.jpg"

    SUPPORT_CHAT = "@LOVER_MUSIC_SUPPORT_GROUP"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5663648528:AAH-DGSnjOD_IX2XMW-zCDWHgJ2pWy-0ixw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "xyz"  # Get this value from https://timezonedb.com/api

    OWNER_ID =1548904516   # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = [1001839472020]  # List of groups that you want blacklisted.
    DRAGONS = [5778117994]  # User id of sudo users
    DEV_USERS = [5778117994]  # User id of dev users
    DEMONS = [5778117994]  # User id of support users
    TIGERS = [5778117994]  # User id of tiger users
    WOLVES = [5778117994]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
