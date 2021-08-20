"""
Creating webhook for job in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from create_job import main as created_job
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
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


WEBHOOK = {
    "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
    "method": "POST",
    "event_type": "JOB_COMPLETE",
    "content_type": "application/json",
    "body": '{ "text": "hello world" }',
    "enabled": True
}


def main(WEBHOOK):
    """creating webhook"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    job = created_job(JOB=JOB)
    job_id = job["id"]
    job_webhook = mitto.create_job_webhook(job_id=job_id, job_hook=WEBHOOK)
    return job_webhook


if __name__ == "__main__":
    sys.exit(main(WEBHOOK))
