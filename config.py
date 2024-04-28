import os

API_ID = API_ID = 24630940

API_HASH = os.environ.get("API_HASH", "df46be1ad6b0027ec1dff6dd3bb703dd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7041642612:AAE-G8Sk-0Dwd-wdFacfbz2OCBjLoUbOCYA:")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "24630940")

LOG = -1001619283960

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "24630940").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


