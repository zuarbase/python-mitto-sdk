"""
Getting configuration info of existing job in Mitto instance.
"""
import sys
import os
import uuid

from dotenv import load_dotenv
from create_job import main as created_job
from mitto_sdk import Mitto

load_dotenv()

UUID = str(uuid.uuid4())
NAME = f"sql_{UUID}".replace("-", "_")
TITLE = f"[SQL]{UUID}"
TYPE = "sql"
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB = {
  "name": NAME,
  "title": TITLE,
  "type": TYPE,
  "schedule": {
      "value": "daily",
      "type": "daily",
      "daily": {
          "minute": 0,
          "hour": 12,
          "ampm": "AM"
      },
      "hourly": None,
      "custom": None
  },
  "conf": {
    "dbo": "postgresql://localhost/analytics",
    "credentials": None,
    "sql": "select 1",
    "parameters": {},
    "kwargs": {},
    "transaction": True,
    "split": False
  }
}


def main(base_url=BASE_URL, api_key=API_KEY, job=JOB):
    """show matching jobs"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    create_job = created_job(job=job)
    job_id = create_job['id']
    s_job = mitto.get_job(job_id=job_id)
    conf = s_job['conf']  # noqa: F841
    return conf


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, job=JOB))
