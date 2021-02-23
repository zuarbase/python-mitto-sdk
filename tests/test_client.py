import requests

from src.mitto_sdk import Mitto

def test_init(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    mitto = Mitto(
        base_url="https://fake.com",
        api_key="FAKE_API_KEY"
    )
    assert mitto.session.params["API_KEY"] == "FAKE_API_KEY"