import os
import sys

from dotenv import load_dotenv
from build.lib.mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_ID = 26402

# the existing job conf has "sql": "select 1"
JOB_CONF = {
    "dbo": "postgresql://localhost/analytics",
    "sql": "select 3;",
    "parameters": {},
    "kwargs": {},
    "transaction": True,
    "split": False
}


def main():
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    updated_job = mitto.update_job_conf(job_id=JOB_ID, job_conf=JOB_CONF)
    print(updated_job)


if __name__ == "__main__":
    sys.exit(main())
