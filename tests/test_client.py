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