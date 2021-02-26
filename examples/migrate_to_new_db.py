"""
This example would update all io jobs with an input
of PostgreSQL to use a new input of MariaDB
"""

import sys
import os
from mitto_sdk import Mitto
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_TYPE = "io"
INPUT_DBO_LIKE = "postgresql"
NEW_DBO = "mysql+pymysql://<user>:<password>@<hostname>.us-east-1.rds.amazonaws.com:3306/<dbname>"


def main():
    """change db inputs from postgres to maria"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    jobs = mitto.get_jobs(job_type=JOB_TYPE)
    for job in jobs:
        job_id = job["id"]
        job_conf = mitto.get_job(job_id=job_id)
        conf = job_conf["conf"]
        if "input" in conf and "dbo" in conf["input"]:
            if INPUT_DBO_LIKE in conf["input"]["dbo"]:
                conf["input"]["dbo"] = NEW_DBO
                print(f"Updating job conf: {job_id}, {job['title']}")
                mitto.update_job_conf(job_id=job_id, job_conf=conf)
if __name__ == "__main__":
    sys.exit(main())
