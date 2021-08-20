"""
Getting status an existing job in Mitto.
"""
import os
import sys

from dotenv import load_dotenv
from start_job import main as started_job
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")


def main(BASE_URL, API_KEY):
    """getting status"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    start_job = started_job(BASE_URL=BASE_URL, API_KEY=API_KEY)
    job_id = start_job["id"]
    single_status = mitto.get_single_job_status(job_id=job_id)
    return single_status


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
