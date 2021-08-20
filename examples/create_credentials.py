"""
Creating credentials for Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from mitto_sdk import Mitto


load_dotenv()

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


def main(NEW_CREDS):
    """creating credentials"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    create_creds = mitto.create_credentials(creds=NEW_CREDS)
    return create_creds


if __name__ == "__main__":
    sys.exit(main(NEW_CREDS))
