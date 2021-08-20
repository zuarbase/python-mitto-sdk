"""
Updating an existing job in Mitto instance.
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


UPDATE_JOB = {
  "title": "sql",
  "type": "sql",
  "markdown": "string",
  "schedule": {
    "type": "daily",
    "daily": {
      "minute": 0,
      "hour": 6,
      "ampm": "AM"
    },
  },
  "timeout": 0,
  "notify": 0,
  "delay": 0,
  "continue_on_error": True,
  "concurrency": 0,
  "conf": {
    "input": {},
    "output": {
      "dbo": "postgresql://localhost/analytics",
      "schema": "test",
      "tablename": "account",
      "use": "call:mitto.iov2.db#todb"
    },
    "steps": [
       {
         "column": "system_modstamp",
         "use": "mitto.iov2.steps#MaxTimestamp"
       },
       {
         "use": "mitto.iov2.steps.upsert#SetUpdatedAt"
       },
       {
         "transforms": [
            {
              "use": "mitto.iov2.transform#ExtraColumnsTransform",
              "rename_columns": False
            },
            {
              "use": "mitto.iov2.transform#ColumnsTransform"
            }
         ],
         "use": "mitto.iov2.steps#Input"
       },
       {
         "use": "mitto.iov2.steps#CreateTable"
       },
       {
         "use": "mitto.iov2.steps.upsert#CreateTempTable"
       },
       {
         "transforms": [
            {
              "use": "mitto.iov2.transform#FlattenTransform"
            }
         ],
         "use": "mitto.iov2.steps#Output"
       },
       {
         "key": "id",
         "use": "mitto.iov2.steps.upsert#SyncTempTable"
       },
       {
         "use": "mitto.iov2.steps#CollectMeta"
       }
    ],
    "store": {
      "key": "Id",
      "updated_at": "SystemModstamp"
    }
  },
  "tags": [
    "string"
  ],
  "input": {},
  "output": {},
  "sdl": {},
  "steps": [
    "string"
  ]
}


def main(BASE_URL, API_KEY, UPDATE_JOB):
    """updating job"""
    job = created_job(JOB=JOB)
    print(job)
    job_id = job["id"]

    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    update_job = mitto.update_job(job_id=job_id, update_job_body=UPDATE_JOB)
    return update_job


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY, UPDATE_JOB))
