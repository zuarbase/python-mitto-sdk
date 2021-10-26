"""
Get info about packages in Mitto instances.
"""
import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")


def main(base_url=BASE_URL, api_key=API_KEY):
    """getting pkg"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    pkg = mitto.get_pkg()
    return pkg


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY))
