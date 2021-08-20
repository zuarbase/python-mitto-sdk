"""
Creating tag for job in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

UUID = str(uuid.uuid4())
NAME = f"tag_{UUID}".replace("-", "_")
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

TAG = {
    "name": NAME
}


def main(TAG):
    """creating tag"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    create_tag = mitto.create_tags(tags=TAG)
    return create_tag


if __name__ == "__main__":
    sys.exit(main(TAG))
