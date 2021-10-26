"""
Getting job by existing name.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_bulk_job import main as created_bulk_job  # noqa: E501# pylint: disable;E0401
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
UUID = str(uuid.uuid4())
NAME = f"bulk_{UUID}".replace("-", "_")
TITLE = f"[BULK]{UUID}"
TYPE = "bulk"

BULK_JOB = [
  {
    "name": NAME,
    "title": TITLE,
    "type": TYPE,
    "markdown": "string",
    "schedule": {
      "type": "daily",
      "daily": {
        "minute": 0,
        "hour": 12,
        "ampm": "AM"
      },
      "hourly": None,
      "custom": None
    },
    "timeout": 0,
    "notify": 0,
    "delay": 0,
    "continue_on_error": True,
    "concurrency": 0
  }
]


def main(base_url=BASE_URL, api_key=API_KEY, bulk_job=BULK_JOB):  # noqa: E501
    """
    Request to API with current configurations.
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    create_bulk_job = created_bulk_job(bulk_job_s=bulk_job)
    jobs = mitto.get_bulk_jobs(create_bulk_job)
    return jobs


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
