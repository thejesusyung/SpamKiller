import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("API_KEY_SPAM_KILLER") # Get token from environment variable
ADMIN_IDS = (
    os.getenv("ADMIN_IDS").split(",") if os.getenv("ADMIN_IDS") else []
)  # Get admin id from environment variable (in .env file)
TARGET_GROUP_ID = (
    os.getenv("TARGET_GROUP_ID") if os.getenv("TARGET_GROUP_ID") else []
)  # Get tar  # Get target group id from environment variable (in .env file)
TARGET_SPAM_ID = (
    os.getenv("TARGET_SPAM_ID") if os.getenv("TARGET_SPAM_ID") else []
)  # Get target notid from environment variable (in .env file)
WHITELIST_ADMINS = (
    [int(i) for i in os.getenv("WHITELIST_ADMINS").split(",")]
    if os.getenv("WHITELIST_ADMINS")
    else []
)
TARGET_NOT_SPAM_ID = (
    os.getenv("TARGET_NOT_SPAM_ID") if os.getenv("TARGET_NOT_SPAM_ID") else []
)  # Get target not spam group id from environment variable (in .env file)
AUTHORIZED_USER_IDS = (
    os.getenv("AUTHORIZED_USER_IDS").split(",")
    if os.getenv("AUTHORIZED_USER_IDS")
    else []
)
AUTHORIZED_GROUP_IDS = (
    os.getenv("AUTHORIZED_GROUP_IDS").split(",")
    if os.getenv("AUTHORIZED_GROUP_IDS")
    else []
)  # Get admin id from environment variable (in .env file)