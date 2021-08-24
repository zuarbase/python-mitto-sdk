"""
Deleting defined webhook by id in Mitto instanse.
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


def main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK):
    """
    Request to API with current configurations.
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    webhook = created_webhook(webhook=webhook)
    webhook_id = webhook["id"]
    deleted_webhook = mitto.delete_webhook(webhook_id=webhook_id)
    print(f'{webhook}\n If you see Response[204]',
          f'message webhook {webhook_id} succesfuly deleted')
    return deleted_webhook


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK))
