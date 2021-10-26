"""Test of all scripts at examples directory"""  # noqa: E901
import json  # noqa: F401# pylint: disable=W0611, C0411

from addict import Dict  # noqa: E402
from collections import OrderedDict  # noqa: F401# pylint: disable=W0611, C0411
from examples import (  # noqa: F401
    create_bulk_job,
    create_cmd_job,
    create_credentials,
    create_job,
    create_job_webhook,
    create_sql_job,
    create_tag,
    dbo_update_sql_job,
    delete_job,
    delete_webhook,
    get_about,
    get_about_messages,
    get_conf_info,
    get_credentials,
    get_databases,
    get_job_by_name,
    get_jobs,
    get_job_schedule,
    get_metrics,
    get_pkg,
    get_single_job,
    get_single_job_status,
    get_single_job_webhook_conf_info,
    get_tags,
    get_webhooks,
    start_job,
    update_job,
    update_job_credentials,
    update_job_schedule,
    update_pkg,
    update_a_webhook
)


BASE_URL = "https://fake.zuarbase.net"
API_KEY = "FAKE_API_KEY"


def mock_response(response):
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: response,
            "raise_for_status": lambda: None
        })
    return _request


def _request_delete():
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 204
        })
    return _request


def test_create_bulk_job(mocker, test_bulk_job_fixture):
    """test create_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_bulk_job_fixture))  # noqa: E501
    assert create_bulk_job.main(bulk_job_s=test_bulk_job_fixture) == test_bulk_job_fixture  # noqa: E501


def test_create_credentials(mocker, test_credentials_fixture):
    """testing create_credentials.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_credentials_fixture))  # noqa: E501
    assert create_credentials.main(new_creds=test_credentials_fixture) == test_credentials_fixture  # noqa: E501


def test_create_job(mocker, test_io_job_fixture):
    """testing create_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    assert create_job.main(job=test_io_job_fixture) == test_io_job_fixture  # noqa: E501


def test_create_cmd_job(mocker, test_cmd_job_fixture):
    """testing create_cmd_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_cmd_job_fixture))  # noqa: E501
    assert create_cmd_job.main(job=test_cmd_job_fixture) == test_cmd_job_fixture  # noqa: E501


def test_create_job_webhook(mocker, test_create_job_webhook_fixture, test_io_job_fixture):  # noqa: E501
    """testing create_job_webhook.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    assert create_job_webhook.main(webhook=test_create_job_webhook_fixture) == test_create_job_webhook_fixture  # noqa: E501


def test_create_sql_job(mocker, test_sql_job_fixture):
    """testing create_sql_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_sql_job_fixture))  # noqa: E501
    assert create_sql_job.main(sql_job=test_sql_job_fixture) == test_sql_job_fixture  # noqa: E501


def test_create_tag(mocker, test_tag_fixture):
    """testing create_tag.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_tag_fixture))
    assert create_tag.main(tag=test_tag_fixture) == test_tag_fixture  # noqa: E501


def test_get_about_messages(mocker, test_get_about_messages_fixture):
    """testing get_about_messages.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_messages_fixture))  # noqa: E501
    assert get_about_messages.main(base_url=BASE_URL, api_key=API_KEY) == test_get_about_messages_fixture  # noqa: E501


def test_get_about(mocker, test_get_about_fixture):
    """testing get_about.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_fixture))  # noqa: E501
    assert get_about.main(base_url=BASE_URL, api_key=API_KEY) == test_get_about_fixture  # noqa: E501
    assert get_about.main(base_url=BASE_URL, api_key=API_KEY)["system"]["fqdn"] == "aziz-mitto.zuarbase.net"  # noqa: E501


def test_get_single_job(mocker, test_get_single_job_fixture, test_io_job_fixture):  # noqa: E501
    """testing get_single_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_fixture))  # noqa: E501
    assert get_single_job.main(base_url=BASE_URL, api_key=API_KEY) == test_get_single_job_fixture  # noqa: E501


def test_get_conf_info(mocker, test_get_conf_info_fixture, test_io_job_fixture):  # noqa: E501
    """testing get_about.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_conf_info_fixture))  # noqa: E501
    assert get_conf_info.main(base_url=BASE_URL, api_key=API_KEY) == test_get_conf_info_fixture["conf"]  # noqa: E501


def test_get_credentials(mocker, test_get_credentials_fixture, test_credentials_fixture):  # noqa: E501
    """testing get_credentials.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_credentials_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_credentials_fixture))  # noqa: E501
    assert get_credentials.main(base_url=BASE_URL, api_key=API_KEY) == test_get_credentials_fixture  # noqa: E501


def test_get_databases(mocker, test_get_databases_fixture):
    """testing get_databases.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_databases_fixture))  # noqa: E501
    assert get_databases.main(base_url=BASE_URL, api_key=API_KEY) == test_get_databases_fixture  # noqa: E501


def test_get_job_by_name(mocker, test_get_job_by_name_fixture, test_create_bulk_job_fixture):  # noqa: E501
    """testing get_job_by_name.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_create_bulk_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_by_name_fixture))  # noqa: E501
    assert get_job_by_name.main(base_url=BASE_URL, api_key=API_KEY) == test_get_job_by_name_fixture  # noqa: E501


def test_get_job_schedule(mocker, test_get_job_schedule_fixture, test_io_job_fixture):  # noqa: E501
    """testing get_job_schedule.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_schedule_fixture))  # noqa: E501
    assert get_job_schedule.main(base_url=BASE_URL, api_key=API_KEY) == test_get_job_schedule_fixture["schedule"]  # noqa: E501


def test_search_jobs(mocker, test_get_jobs_fixture):
    """testing get_jobs.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_get_jobs_fixture))  # noqa: E501
    assert list(get_jobs.main(base_url=BASE_URL, api_key=API_KEY)) == test_get_jobs_fixture["jobs"]  # noqa: E501


def test_get_metrics(mocker, test_get_metrics_fixture):
    """testing get_metrics.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_metrics_fixture))  # noqa: E501
    metrics = get_metrics.main(base_url=BASE_URL, api_key=API_KEY)
    assert metrics == test_get_metrics_fixture


def test_get_pkg(mocker, test_get_pkg_fixture):
    """testing get_pkg.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_pkg_fixture))  # noqa; E501
    assert get_pkg.main(base_url=BASE_URL, api_key=API_KEY) == test_get_pkg_fixture  # noqa: E501


def test_get_single_job_webhook_conf_info(mocker, test_get_single_job_webhook_conf_info_fixture, test_create_job_webhook_fixture):  # noqa: E501
    """testing get_single_job_webhook_conf_info.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_webhook_conf_info_fixture))  # noqa:
    assert get_single_job_webhook_conf_info.main(base_url=BASE_URL, api_key=API_KEY) == test_get_single_job_webhook_conf_info_fixture  # noqa: E501


def test_get_tags(mocker, test_get_tags_fixture, test_tag_fixture):
    """testing get_tags.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_tag_fixture))
    mocker.patch("requests.Session.get", new=mock_response(test_get_tags_fixture))  # noqa: E501
    assert get_tags.main(base_url=BASE_URL, api_key=API_KEY) == test_get_tags_fixture  # noqa: E501


def test_get_webhooks(mocker, test_get_webhooks_fixture, test_io_job_fixture):
    """testing get_webhooks.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    assert get_webhooks.main(base_url=BASE_URL, api_key=API_KEY) == test_get_webhooks_fixture  # noqa: E501


def test_start_job(mocker, test_start_job_fixture):
    """testing start_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_start_job_fixture))  # noqa: E501
    assert start_job.main(base_url=BASE_URL, api_key=API_KEY) == test_start_job_fixture  # noqa: E501


def test_get_single_job_status(mocker, test_get_single_job_status_fixture, test_io_job_fixture):  # noqa: E501
    """testing get_single_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_status_fixture))  # noqa: E501
    assert get_single_job_status.main(base_url=BASE_URL, api_key=API_KEY) == test_get_single_job_status_fixture  # noqa: E501


def test_update_job_credentials(mocker, test_update_job_credentials_fixture, test_io_job_fixture, test_get_jobs_fixture):  # noqa: E501
    """testing update_job_credentials.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.post", new=mock_response(test_get_jobs_fixture))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_credentials_fixture))  # noqa: E501
    input_creds = "Fakeforse - fake.fake@zuar.com"
    assert update_job_credentials.main(
        base_url=BASE_URL,
        api_key=API_KEY,
        input_creds=input_creds
    ) == test_update_job_credentials_fixture


def test_update_job(mocker, test_update_job_fixture, test_io_job_fixture):
    """testing update_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_fixture))  # noqa: E501
    updated_job = {
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
        "conf": "string",
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
    assert update_job.main(base_url=BASE_URL, api_key=API_KEY, update_job=updated_job) == test_update_job_fixture  # noqa: E501


def test_update_job_schedule(mocker, test_update_job_schedule_fixture, test_get_job_schedule_fixture, test_io_job_fixture):  # noqa: E501
    """testing update_job_schedule.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_schedule))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_schedule_fixture))  # noqa: E501

    schedule = {
        "value": "daily",
        "type": "daily",
        "daily": {
          "minute": 0,
          "hour": 6,
          "ampm": "AM"
        },
        "hourly": None,
        "custom": None
    }

    assert update_job_schedule.main(
        base_url=BASE_URL,
        api_key=API_KEY,
        schedule=schedule
    ) == test_update_job_schedule_fixture


def test_update_pkg(mocker, test_update_pkg_fixture):
    """testing update_pkg.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_update_pkg_fixture))  # noqa: E501
    assert update_pkg.main(base_url=BASE_URL, api_key=API_KEY) == test_update_pkg_fixture  # noqa: E501


def test_dbo_update_sql_job(mocker, test_dbo_update_sql_job_fixture, test_sql_job_fixture):  # noqa: E501
    """testing dbo_update_sql_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_sql_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_dbo_update_sql_job_fixture))  # noqa: E501
    dbo = "postrgesql://localhost/fake"
    assert dbo_update_sql_job.main(base_url=BASE_URL, api_key=API_KEY, dbo=dbo) == test_dbo_update_sql_job_fixture  # noqa: E501


def test_delete_job(mocker, test_delete_job_fixture, test_io_job_fixture):  # noqa: E501
    """testing delete_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.delete", new=_request_delete())
    assert delete_job.main(base_url=BASE_URL, api_key=API_KEY) == test_delete_job_fixture  # noqa: E501


def test_delete_webhook(mocker, test_delete_job_webhook_fixture, test_io_job_fixture, test_create_job_webhook_fixture):  # noqa: E501
    """testing delete_webhook.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    mocker.patch("requests.Session.delete", new=_request_delete())  # noqa: E501
    assert delete_webhook.main(base_url=BASE_URL, api_key=API_KEY) == test_delete_job_webhook_fixture  # noqa: E501


def test_update_a_webhook(mocker, test_get_webhooks_fixture, test_update_a_webhook_fixture):  # noqa: E501
    """testing update_a_webhook.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    mocker.patch("requests.Session.put", new=mock_response(test_update_a_webhook_fixture))  # noqa: E501
    webhook = "https://fakehook.com"
    old_webhook = "https://oldhook.com"
    assert update_a_webhook.main(base_url=BASE_URL, api_key=API_KEY, webhook=webhook, old_webhook=old_webhook) == [test_update_a_webhook_fixture]  # noqa: E501
