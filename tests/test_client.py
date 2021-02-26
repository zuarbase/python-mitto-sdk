import requests
from addict import Dict

from src.mitto_sdk import Mitto


def test_init(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.session.params["API_KEY"] == "FAKE_API_KEY"


def test_base_url_ends_with_slash(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net/",
        api_key="FAKE_API_KEY"
    )
    assert mitto.base_url == "https://fake.zuarbase.net"


ABOUT_RESPONSE = Dict()
ABOUT_RESPONSE.version = "2.8.8"
ABOUT_RESPONSE.system.fqdn = "fake.zuarbase.net"


def test_get_about(mocker):
    def _request_get(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: ABOUT_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_about() == ABOUT_RESPONSE
    assert mitto.get_about()["system"]["fqdn"] == "fake.zuarbase.net"


GET_JOB_RESPONSE = Dict()
GET_JOB_RESPONSE.id = 1
GET_JOB_RESPONSE.name = "job_name"
GET_JOB_RESPONSE.title = "job name"
GET_JOB_RESPONSE.type = "io"


def test_get_job(mocker):
    def _request_get(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_job(1) == GET_JOB_RESPONSE


GET_JOB_SCHEDULE_RESPONSE = Dict()
GET_JOB_SCHEDULE_RESPONSE.value = "daily"
GET_JOB_SCHEDULE_RESPONSE.type = "daily"
GET_JOB_SCHEDULE_RESPONSE.daily = {
    'hour': 1,
    'minute': 0,
    'ampm': 'AM'
}


def test_get_job_schedule(mocker):
    def _request_get(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_SCHEDULE_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_job_schedule(1) == GET_JOB_SCHEDULE_RESPONSE


def test_update_schedule(mocker):
    def _request_post(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.update_job_schedule(
        job_id=1,
        job_schedule={
            'value': 'never',
            'type': 'never',
            'daily': None,
            'hourly': None,
            'custom': None
        }
    ) == GET_JOB_RESPONSE


def test_update_job_conf(mocker):
    def _request_post(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    new_conf = Dict()
    new_conf.id = 1
    new_conf.name = "fake_job"
    new_conf.title = "fake job"
    assert mitto.update_job_conf(
        job_id=1,
        job_conf=new_conf
    ) == GET_JOB_RESPONSE


def test_create_job(mocker):
    def _request_post(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    job = {
        "name": "sql_select_1_from_api",
        "title": "[SQL] Select 1 from API",
        "type": "sql",
        "tags": [
            "sql"
        ],
        "conf": {
            "dbo": "postgresql://localhost/analytics",
            "sql": "select 1;",
            "parameters": {},
            "kwargs": {},
            "transaction": True,
            "split": False
        }
    }
    assert mitto.create_job(job=job) == GET_JOB_RESPONSE


WEBHOOK_RESPONSE = Dict()
WEBHOOK_RESPONSE.url = "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314"  # noqa: E501
WEBHOOK_RESPONSE.method = "POST"
WEBHOOK_RESPONSE.event_type = "JOB_COMPLETE"


def test_create_job_webhook(mocker):
    def _request_post(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: WEBHOOK_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    webhook = {
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
        "method": "POST",
        "event_type": "JOB_COMPLETE",
        "content_type": "application/json",
        "body": '{ "text": "hello world" }',
        "enabled": True
    }
    assert mitto.create_job_webhook(
        job_id=1,
        job_hook=webhook
    ) == WEBHOOK_RESPONSE


GET_JOBS_RESPONSE = Dict()
GET_JOBS_RESPONSE.jobs = []
GET_JOBS_RESPONSE.jobs.append(GET_JOB_RESPONSE)
GET_JOBS_RESPONSE.pagination = {
    'count': 82,
    'limit': 50,
    'more_pages': False,
    'offset': 50
}


def test_get_jobs(mocker):
    def _request_get(*args, params=None, **kwargs):
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOBS_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert list(mitto.get_jobs()) == GET_JOBS_RESPONSE["jobs"]
