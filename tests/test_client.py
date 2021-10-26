"""testing client.py functions"""  # noqa: E902
import requests

from addict import Dict
from mitto_sdk import Mitto


mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )


def mock_response(response):
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: response,
            "raise_for_status": lambda: None
        })
    return _request


def test_init(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    assert mitto.session.params["API_KEY"] == "FAKE_API_KEY"


def test_base_url_ends_with_slash(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    assert mitto.base_url == "https://fake.zuarbase.net"


def test_get_about(mocker, test_get_about_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_fixture))  # noqa: E501
    assert mitto.get_about() == test_get_about_fixture
    assert mitto.get_about()["system"]["fqdn"] == "aziz-mitto.zuarbase.net"


def test_get_job(mocker, test_get_job_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_fixture))  # noqa: E501
    job = mitto.get_job(49)
    assert job == test_get_job_fixture


def test_get_job_schedule(mocker, test_get_job_schedule_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_schedule_fixture))  # noqa: E501
    assert mitto.get_job_schedule(job_id=47) == test_get_job_schedule_fixture["schedule"]  # noqa: E501


def test_update_schedule(mocker, test_update_job_schedule_fixture):
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_schedule_fixture))  # noqa: E501
    assert mitto.update_job_schedule(
        job_id=1,
        job_schedule=test_update_job_schedule_fixture
    ) == test_update_job_schedule_fixture


def test_update_job(mocker, test_update_job_fixture):
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_fixture))  # noqa: E501
    assert mitto.update_job(job_id=52, update_job_body=test_update_job_fixture) == test_update_job_fixture  # noqa: E501


def test_update_job_conf(mocker, test_dbo_update_sql_job_fixture):
    mocker.patch("requests.Session.patch", new=mock_response(test_dbo_update_sql_job_fixture))  # noqa: E501
    assert mitto.update_job_conf(
        job_id=1,
        job_conf=test_dbo_update_sql_job_fixture
    ) == test_dbo_update_sql_job_fixture


def test_create_job(mocker, test_io_job_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    assert mitto.create_job(job=test_io_job_fixture) == test_io_job_fixture


def test_create_cmd_job(mocker, test_cmd_job_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_cmd_job_fixture))  # noqa: E501
    assert (mitto.create_job(job=test_cmd_job_fixture)) == test_cmd_job_fixture


def test_job_action(mocker, test_start_job_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_start_job_fixture))  # noqa: E501
    action = "start"
    job_id = 65
    assert mitto.job_action(job_id, action) == test_start_job_fixture
    assert mitto.start_job(65) == test_start_job_fixture


def test_create_job_webhook(mocker, test_create_job_webhook_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    assert mitto.create_job_webhook(
        job_id=1,
        job_hook=test_create_job_webhook_fixture
    ) == test_create_job_webhook_fixture


def test_get_job_webhooks(mocker, test_get_webhooks_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    assert mitto.get_job_webhooks(
        job_id=1
    ) == test_get_webhooks_fixture


def test_get_jobs(mocker, test_get_jobs_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_get_jobs_fixture))  # noqa: E501
    assert list(mitto.get_jobs()) == test_get_jobs_fixture["jobs"]


def test_start_job(mocker, test_start_job_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_start_job_fixture))  # noqa: E501
    assert mitto.start_job(3) == test_start_job_fixture


def test_migrate_to_new_db(mocker, test_get_job_fixture):
    mocker.patch("requests.Session.patch", new=mock_response(test_get_job_fixture["conf"]))  # noqa: E501
    assert mitto.update_job_conf(
        job_id=49,
        job_conf=test_get_job_fixture["conf"]
    ) == test_get_job_fixture["conf"]


def test_get_tags(mocker, test_get_tags_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_tags_fixture))  # noqa: E501
    assert mitto.get_tags(tags_id=1) == test_get_tags_fixture


def test_delete_job(mocker):
    def _request_delete(*args, params=None, **kwargs):
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    assert mitto.delete_job(job_id=1) == {'status_code': 204}


def test_delete_webhook(mocker):
    def _request_delete(*args, params=None, **kwargs):
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.delete_webhook(webhook_id=1) == {'status_code': 204}


def test_get_about_messages(mocker, test_get_about_messages_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_messages_fixture))  # noqa: E501
    assert mitto.get_about_messages() == test_get_about_messages_fixture


def test_get_webhooks(mocker, test_get_webhooks_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    assert mitto.get_webhooks() == test_get_webhooks_fixture


def test_get_metrics(mocker, test_get_metrics_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_metrics_fixture))  # noqa: E501
    assert mitto.get_metrics() == test_get_metrics_fixture


def test_get_pkg(mocker, test_get_pkg_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_pkg_fixture))  # noqa: E501
    assert mitto.get_pkg() == test_get_pkg_fixture


def test_get_single_job_status(mocker, test_get_single_job_status_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_status_fixture))  # noqa: E501
    assert mitto.get_single_job_status(job_id=1) == test_get_single_job_status_fixture  # noqa: E501


def test_get_bulk_jobs(mocker, test_get_job_by_name_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_by_name_fixture))  # noqa: E501
    assert mitto.get_bulk_jobs() == test_get_job_by_name_fixture


def test_create_bulk_jobs(mocker, test_bulk_job_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_bulk_job_fixture))  # noqa: E501
    assert mitto.create_bulk_jobs(
        bulk_job=test_bulk_job_fixture
    ) == test_bulk_job_fixture


def test_update_pkg(mocker, test_update_pkg_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_update_pkg_fixture))  # noqa: E501
    assert mitto.update_pkg() == test_update_pkg_fixture


def test_create_tags(mocker, test_tag_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_tag_fixture))
    assert mitto.create_tags(tags=test_tag_fixture) == test_tag_fixture


def test_create_credentials(mocker, test_credentials_fixture):
    mocker.patch("requests.Session.post", new=mock_response(test_credentials_fixture))  # noqa: E501
    assert mitto.create_credentials(creds=test_credentials_fixture) == test_credentials_fixture  # noqa: E501


def test_get_credentials(mocker, test_get_credentials_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_credentials_fixture))  # noqa: E501
    assert mitto.get_credentials() == test_get_credentials_fixture


def test_get_databases(mocker, test_get_databases_fixture):
    mocker.patch("requests.Session.get", new=mock_response(test_get_databases_fixture))  # noqa: E501
    assert mitto.get_databases() == test_get_databases_fixture


def test_update_a_webhook(mocker, test_update_a_webhook_fixture):
    mocker.patch("requests.Session.put", new=mock_response(test_update_a_webhook_fixture))  # noqa: E501
    webhook = {
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314"
    }
    assert mitto.update_a_webhook(webhook_id=1, webhook=webhook) == test_update_a_webhook_fixture  # noqa: E501
