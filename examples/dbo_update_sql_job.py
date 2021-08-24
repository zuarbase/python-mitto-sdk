"""
Updating dbo configuration on existing sql job in Mitto instance.
"""
import os
import sys
import uuid
import hjson

from dotenv import load_dotenv
from create_sql_job import main as created_job
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

DBO = "postrgesql://localhost/analytics"
INPUT_DBO = "postgres"

JOB_TYPE = "sql"


def main(base_url=BASE_URL, api_key=API_KEY, dbo=DBO, input_dbo=INPUT_DBO, job_type=JOB_TYPE, job=JOB):  # noqa: E501
    """dbo updating"""
    mitto = Mitto(
         base_url=BASE_URL,
         api_key=API_KEY
    )
    job = created_job(sql_job=job)
    job_id = job["id"]
    conf = hjson.loads(job["conf"])
    conf["dbo"] = dbo
    job["conf"] = conf
    update_conf_dbo = mitto.update_job_conf(job_id=job_id, job_conf=conf)
    return update_conf_dbo


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, dbo=DBO, input_dbo=INPUT_DBO, job_type=JOB_TYPE, job=JOB))  # noqa: E501
