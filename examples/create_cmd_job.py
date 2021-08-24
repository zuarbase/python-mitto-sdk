"""
Creating CMD job in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"cmd_{UUID}".replace("-", "_")
TITLE = f"[CMD]{UUID}"

JOB = {
    "name": NAME,
    "title": TITLE,
    "type": "cmd",
    "tags": [
        "cmd"
    ]
}


def main(job=JOB):
    """creating CMD job"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    job = mitto.create_job(job=job)
    return job


if __name__ == "__main__":
    sys.exit(main(job=JOB))
