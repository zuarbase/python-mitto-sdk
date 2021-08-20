import os
import json
import pytest


@pytest.fixture(scope="session")
def test_bulk_job_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "bulk_job.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_cmd_job_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "cmd_job.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_credentials_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "credentials.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_io_job_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "io_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_create_job_webhook_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "create_job_webhook.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_sql_job_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "sql_job.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_tag_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "tag.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_about_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_about.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_about_messages_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_about_messages.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_conf_info_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_conf_info.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_credentials_fixture(test_credentials_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_credentials.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_databases_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_databases.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_job_by_name_fixture(test_bulk_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job_by_name.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_job_schedule_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job_schedule.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_job_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_single_job_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_jobs_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_jobs.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_metrics_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_metrics.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_pkg_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_pkg.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_single_job_status_fixture(test_io_job_fixture, test_start_job_fixture):  # noqa: E501
    path = os.path.join(os.path.dirname(__file__), "data", "get_single_job_status.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_single_job_webhook_conf_info_fixture(test_create_job_webhook_fixture):  # noqa: E501
    path = os.path.join(os.path.dirname(__file__), "data", "get_single_job_webhook_conf_info.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_tags_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "get_tags.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_get_webhooks_fixture(test_create_job_webhook_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "get_webhooks.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_start_job_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "start_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_update_job_credentials_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "update_job_credentials.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_update_job_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "update_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_update_job_schedule_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "update_job_schedule.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_update_pkg_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "update_pkg.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_delete_job_fixture(test_io_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "delete_job.json")
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_delete_job_webhook_fixture(test_io_job_fixture, test_create_job_webhook_fixture):  # noqa: E501
    path = os.path.join(os.path.dirname(__file__), "data", "delete_webhook.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_dbo_update_sql_job_fixture(test_sql_job_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "dbo_update_sql_job.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data


@pytest.fixture(scope="session")
def test_update_a_webhook_fixture(test_get_webhooks_fixture):
    path = os.path.join(os.path.dirname(__file__), "data", "update_a_webhook.json")  # noqa: E501
    f = open(f'{path}', 'r')
    data = json.load(f)
    return data
