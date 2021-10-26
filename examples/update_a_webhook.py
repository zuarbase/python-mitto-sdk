"""Updating a webhook"""
import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")
OLD_WEBHOOK = "https://oldhook.com"  # noqa: E501
WEBHOOK = "https://newhook.com"  # noqa: E501


def main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK, old_webhook=OLD_WEBHOOK):  # noqa: E501
    """
    Updating all webhooks in Mitto instance to defined webhook
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    update_webhook_list = []
    webhooks = mitto.get_webhooks()
    for n in webhooks:
        s_webhook = n
        webhook_id = s_webhook["id"]
        if s_webhook["url"] == old_webhook:
            webhook_url = s_webhook["url"]
            webhook_url = webhook
            s_webhook["url"] = webhook_url
            update_webhook = mitto.update_a_webhook(webhook_id=webhook_id, webhook=s_webhook)  # noqa: E501
            update_webhook_list.append(update_webhook)
    return update_webhook_list


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY, webhook=WEBHOOK, old_webhook=OLD_WEBHOOK))  # noqa: E501
