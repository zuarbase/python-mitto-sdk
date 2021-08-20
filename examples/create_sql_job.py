"""
Creating a new sql job in Mitto instance.
"""
import os
import sys
import uuid

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

UUID = str(uuid.uuid4())
NAME = f"sql_{UUID}".replace("-", "_")
TITLE = f"[SQL]{UUID}"
BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
SQL_JOB = {
  "name": NAME,
  "title": TITLE,
  "type": "sql",
  "conf": {
    "input": {},
    "output": {
      "dbo": "postgresql://localhost/analytics",
      "schema": "",
      "tablename": "cogs",
      "use": "call:mitto.iov2.db#todb"
    }
  }
}


def main(SQL_JOB):
    """
    Request to API with current configurations.
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    created_job = mitto.create_job(job=SQL_JOB)
    return created_job


if __name__ == "__main__":
    sys.exit(main(SQL_JOB))
