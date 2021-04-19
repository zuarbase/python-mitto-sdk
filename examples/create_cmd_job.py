import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB = {
    "name": "cmd_echo_env",
    "title": "[CMD] echo env",
    "type": "cmd",
    "tags": [
        "cmd"
    ],
    "conf": {
        "cmd": "env > /var/mitto/data/env.txt",
        "cmd_env": {},
        "exec": False,
        "shell": True
    }
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    job = mitto.create_job(job=JOB)
    print(job)


if __name__ == "__main__":
    sys.exit(main())
