from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/b016175f5537f279dc84f.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Best_friends_chatting_01")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ABOUT_NOBITA_XD")

STRING_SESSION = getenv("STRING_SESSION", "AQF8l7kATu2m6VL1L40fxOAHp33x0L0ojNXlv8eN-a1RzV3r5VTUC3b0ZJ99VhX6F1SIgZ4iiJvuNo4_Lp2h83GWFmmFZ132ibUifPKVZ7jTOhAQkE3P-lqf-l_oLI4o5qbZxXX6u-AvATMO23vtcG2f69c5f_tDoodzqPG78g3V7OzxPIylSRmPjrS_vMtMl8hvRAEdWIhB1_xeS0bzGmWeFuDkvcVt7f5FyGvSsiuUWUfAx3Wg59_u8KhQqiWgupPmLpkRAljBak2piW8QE2TSDMR6EFObrw0UmBtH24vvRMx2vjtPtJpocTgdG6oa1Fx__efGmCV3i4Rm707fiaHXx0d0zgAAAAExP6UKAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5263125368").split()))
