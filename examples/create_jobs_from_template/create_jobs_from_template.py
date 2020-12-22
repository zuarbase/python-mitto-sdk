import os
import sys
import json

from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

INPUT_DIRECTORY = "templates"
TEMPLATE_FILE = "sql.json"

MITTO_JOBS = [
    {
        "name": "sql_select_1_from_api",
        "title": "[SQL] Select 1 from API",
        "sql": "select 1;"
    },
    {
        "name": "sql_select_2_from_api",
        "title": "[SQL] Select 2 from API",
        "sql": "select 2;"
    },
    {
        "name": "sql_select_3_from_api",
        "title": "[SQL] Select 3 from API",
        "sql": "select 3;"
    }
]


def main():
    # set up Jinja
    template_env = Environment(loader=FileSystemLoader(INPUT_DIRECTORY))
    template = template_env.get_template(TEMPLATE_FILE)

    # set up Mitto
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    # create a Mitto job for each Jinja job template
    for job in MITTO_JOBS:
        jinja_template = template.render(
            job_name=job["name"],
            job_title=job["title"],
            sql=job["sql"]
        )
        job_template = json.loads(jinja_template)
        job = mitto.create_job(job=job_template)
        print(job)


if __name__ == "__main__":
    sys.exit(main())
