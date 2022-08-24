from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", default=12120671, cast=int)
    API_HASH = config("API_HASH", "ecd153928b09383a2d0b4dde1a16c363")
    BOT_TOKEN = config("BOT_TOKEN", "5307675207:AAEse94GiWr7d_lv-_IMV03AWBxM2mzfURg")
    SUDO = list(map (int, getenv("SUDO", "1930954213 1953140355 2085779631 1897103955 1980866589 1287077585 1990503115 2146911138").split()))
