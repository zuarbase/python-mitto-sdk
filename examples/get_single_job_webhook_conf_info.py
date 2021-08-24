"""
Getting existing single job webhook configuration info in Mitto instance.
"""
import os
import sys

from dotenv import load_dotenv
from create_job_webhook import main as created_job_webhook
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
WEBHOOK = {
    "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
    "method": "POST",
    "event_type": "JOB_COMPLETE",
    "content_type": "application/json",
    "body": '{ "text": "hello world" }',
    "enabled": True
}


def main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK):
    """getting webhook configuration info"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    webhook = created_job_webhook(webhook=webhook)
    job_id = webhook["id"]
    single_webhook = mitto.get_job_webhooks(job_id=job_id)
    return single_webhook


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK))
