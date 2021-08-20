"""
Getting all jobs creds in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_credentials import main as created_credentials
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"creds_{UUID}".replace("-", "_")
TYPE = "sql"
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

NEW_CREDS = {
    "name": NAME,
    "type": TYPE,
    "data": {}
}


def main(BASE_URL, API_KEY):
    """getting creds"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    created_creds = created_credentials(NEW_CREDS=NEW_CREDS)  # noqa: F841, E501# pylint: disable=W0612
    creds = mitto.get_credentials()
    return creds


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
