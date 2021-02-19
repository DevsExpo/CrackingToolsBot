import os


class Config(object):
    DL_LOCATION = os.environ.get("DL_LOCATION", "./starkgang/")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DEVS_EXPO = os.environ.get("DONTKANGTHISPLS", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None
    API_ID = int(os.environ.get("APP_ID", 6))
    LOG_CHAT = int(os.environ.get("LOG_CHAT", -111111)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    JTU_ENABLE = os.environ.get("JTU_ENABLE", False)
    JTU_ID = int(os.environ.get("JTU_ID", False))
    JTU_LINK = os.environ.get("JTU_LINK", "t.me/PutLinkHereNIbbaElseHowPeopleWillKnow")
