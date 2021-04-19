import sys
import os
from mitto_sdk import Mitto
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
JOB_ID = 65

def main():
    """start job"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    response = mitto.start_job(JOB_ID)
    print(response)

if __name__ == "__main__":
    sys.exit(main())
