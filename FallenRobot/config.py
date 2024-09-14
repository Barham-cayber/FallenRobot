class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27442758
    API_HASH = "8288c5c54f568ee346b3227271700b52"

    CASH_API_KEY = "IUC8TW8F4WXV7KEL"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://avnadmin:AVNS_hl1f0rRGk6UtG16ahxG@test-barhammhamad7726-593f.j.aivencloud.com:17809/defaultdb?sslmode=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002032682720)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://fallen:Barham1234@cluster0.lbti7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "TestsMusic"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7104421875:AAHk0NmGYO3lMZI69CbZwuLDi6NJtCuchWw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "VT36FQYTDRFQ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5576431780  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
