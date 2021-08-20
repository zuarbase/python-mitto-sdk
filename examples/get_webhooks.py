"""
getting all webhooks for jobs in Mitto instance.
"""
import os
import sys

from dotenv import load_dotenv
from create_job_webhook import main as created_webhook
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


def main(BASE_URL, API_KEY):
    """getting webhooks"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    create_job_webhook = created_webhook(WEBHOOK=WEBHOOK)  # noqa: F841, E501# pylint: disable=W0612
    webhooks = mitto.get_webhooks()
    return webhooks


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY))
