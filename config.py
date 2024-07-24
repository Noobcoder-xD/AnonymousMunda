from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")

BOT_TOKEN = getenv("BOT_TOKEN", "7346998885:AAGcGS_rGpALTZWDNa6aEJCz5e7ZTKMf_Gk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7159128525"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")
SESSION = getenv("SESSION", "BADNvmIAK1ezQsqTUYqRfzfO3I_lIm_W8UDKAkoS2lH4jp3GQNPW1DUVODwUDMVjfO0IHhMNnV40imPOUKwUEQ7IZT4Nl0ZzGqmVuubKkebFg66ZfJiC2uhwbxgubfr_tGiZ1W1X93zAb8pxkXjXfDsPwH4g-ICt9KFzi-jjlB2REhOR8E4xpXT_IBVDqoL1-I1hUXJeUJs9nRpE6t5R0ITZ63WWeGQBxgZmrsLWqW7tsHW941HvEzBnGyOGF6NFTg38KR0qquPai0hYIQAugApKPCknrRNKJ2ukNG7aeFhlpt25nQhyZybgt1zLe7dzVDGFoiCiCmIk9M3PxHQlXXunw7Mc-gAAAAF60z7MAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CU_Music_Project")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CU_Music_Project")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5825339458").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
