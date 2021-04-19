import sys
import os
from mitto_sdk import Mitto
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_TYPE = "io"
INPUT_DBO_LIKE = "postgresql"

def main():
    """show matching jobs"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    jobs = mitto.get_jobs(job_type=JOB_TYPE)
    print(f"found jobs that input into {INPUT_DBO_LIKE}:")
    for job in jobs:
        job_id = job["id"]
        job_conf = mitto.get_job(job_id=job_id)
        conf = job_conf["conf"]
        if "input" in conf and "dbo" in conf["input"]:
            if INPUT_DBO_LIKE in conf["input"]["dbo"]:
                print(f"JOB ID: {job_id} - JOB TITLE: {job['title']}")

if __name__ == "__main__":
    sys.exit(main())
