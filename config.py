import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "22182189")) #optional
API_HASH = getenv("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8181241262").split()))
OWNER_ID = int(getenv("OWNER_ID","8181241262"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "8012072801:AAELfiRdBcc768aCG5M23b-7vCdBjxAIIBM")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://ibb.co/wFSS8sJ7')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOKIBu3Jh5-_0ETAZE-TbtkSPIZ2xQBGhIXgc0BVMOEm8K-Okhn4HGMxFhefzBev07vjaPOmW3Sp0AbmvdRbqhmxrR4EPJkAMBtkOZ5Ss1_SoU5_b8RYJb4W4Nc_fUN_fbwDvKdg4mo_KN0o_Yg90xaEPSwEuCmQUeQbRVFdgoI5tOnGeKqbIipR3O5ahd0vykXm5MHPH9jTHyhMjDlakUoGugTUDl5GQlHesj2dKHU2d-g1QgvDduOTWh4gMEo6DrrAbdhmi0k3l4iz1A4PA6Li4OG0ZL-Kkv7a6Ke2TExPY9zHIZ811knfixiwchEbkdBDOvmkSz-FgTBUbnEly1l70LDA=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
