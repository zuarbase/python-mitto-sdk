"""Connect to mitto API and call endpoints"""

import requests
import hjson


class Mitto:
    # pylint: disable=R0904
    """
    Mitto instance
    """
    def __init__(self, base_url, api_key, verify=True):
        if base_url.endswith("/"):
            self.base_url = base_url[:-1]
        else:
            self.base_url = base_url

        # set up the session
        self.session = requests.Session()

        # bypass auth if running on localhost
        if self.base_url.endswith(":7127"):
            self.api_root = ""
            self.api_key = ""
        else:
            self.api_root = "/api"
            self.api_key = api_key
            self.session.params = {
                "API_KEY": self.api_key
            }

        self.verify = verify

    def page_through_results(self, url, params, limit=50, offset=0):
        """
        Page through results returned by Mitto API.
        """
        params["offset"] = offset
        params["limit"] = limit
        more_pages = True

        while more_pages:
            response = self.session.post(url=url, params=params)
            response.raise_for_status()
            data = response.json()
            pagination = data.get("pagination")
            if pagination:
                more_pages = pagination.get("more_pages")
                offset = pagination.get("offset")
                params["offset"] = offset + params["limit"]
            yield data

    def get_jobs(
        self,
        search=None,
        tag=None,
        job_type=None,
        start=None,
        end=None,
        status=None,
        **kwargs
    ):
        # pylint: disable=R0913
        """
        Get jobs from Mitto API. Filter using search, tag, type, and/or status.
        """
        uri = "/v2/jobs/search"
        url = f"{self.base_url}{self.api_root}{uri}"

        params = {
            "search": search,
            "tag": tag,
            "type": job_type,
            "start": start,
            "end": end,
            "status": status
        }

        results = self.page_through_results(url=url, params=params, **kwargs)
        for result in results:
            yield from result["jobs"]

    def get_job(self, job_id):
        """
        Get job from Mitto API. Pass in a valid job id.
        """
        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url)
        results.raise_for_status()

        job = results.json()
        if job.get("conf"):
            conf = job["conf"]
            job["conf"] = hjson.loads(conf)

        return job

    def job_action(self, job_id, action):
        """
        Run action on job
        """
        uri = f"/v2/jobs/{job_id}/:actions"
        url = f"{self.base_url}{self.api_root}{uri}"
        post_data = {
            "action": action.upper()
        }
        results = self.session.post(url=url, json=post_data)
        results.raise_for_status()
        return results.json()

    def start_job(self, job_id):
        """
        Start a job
        """
        return self.job_action(job_id, "start")

    def get_about(self):
        """
        Get system information from Mitto API.
        """
        uri = "/v2/about"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url)
        results.raise_for_status()
        return results.json()

    def delete_job(self, job_id):
        """
        Delete job from Mitto. Pass in a valid job id.
        """
        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.delete(url)
        return results

    def create_job(self, job, **kwargs):
        """
        Create a new Mitto job.
        """
        assert isinstance(job, dict)

        uri = "/v2/jobs"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url=url, json=job, **kwargs)
#        results.raise_for_status()
        return results.json()

    def get_job_schedule(self, job_id=None, **kwargs):
        """
        Get a job's schedule. Pass in a valid job id.
        """

        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url=url, **kwargs)
        results.raise_for_status()
        job = results.json()
        return job["schedule"]

    def update_job_schedule(self, job_id=None, job_schedule=None, **kwargs):
        """
        Update a job's schedule. Pass in a valid job id and schedule.
        """
        assert isinstance(job_id, int)
        assert isinstance(job_schedule, dict)

        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.patch(url=url, json=job_schedule, **kwargs)
        results.raise_for_status()
        return results.json()

    def update_job(self, job_id, update_job_body, **kwargs):
        """
        Update an existing Mitto job
        """
        assert isinstance(job_id, int)
        assert isinstance(update_job_body, dict)

        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.patch(url, json=update_job_body, **kwargs)
        results.raise_for_status()
        return results.json()

    def update_job_conf(self, job_id, job_conf, **kwargs):
        """
        Update an existing Mitto job conf.
        """
        assert isinstance(job_id, int)

        uri = f"/v2/jobs/{job_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.patch(url, json=job_conf, **kwargs)
        results.raise_for_status()
        return results.json()

    def create_job_webhook(self, job_id=None, job_hook=None, **kwargs):
        """
        Add a web hook to a job. Pass in a valid job id and webhook.
        """
        assert isinstance(job_id, int)
        assert isinstance(job_hook, dict)

        uri = f"/v2/jobs/{job_id}/webhooks"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url=url, json=job_hook, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_job_webhooks(self, job_id=None, **kwargs):
        """
        Get info about single job current webhook, if it exists.
        """
        assert isinstance(job_id, int)

        uri = f"/v2/jobs/{job_id}/webhooks"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url=url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_tags(self, **kwargs):
        """
        Get info about tags of job, if it exists.
        """

        uri = "/tags"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url=url, **kwargs)
        results.raise_for_status()
        return results.json()

    def delete_webhook(self, webhook_id=None):
        """
        Delete webhook from Mitto job. Pass in a valid webhook id.
        """
        uri = f"/webhooks/{webhook_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.delete(url)
        return results

    def get_about_messages(self, **kwargs):
        """
        Get about messages.
        """

        uri = "/v2/about/messages"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_webhooks(self, **kwargs):
        """
        Get all webhooks.
        """

        uri = "/webhooks"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_metrics(self, **kwargs):
        """
        Get metrics.
        """

        uri = "/v2/metrics"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_pkg(self, **kwargs):
        """
        Get the list of Mitto packages.
        """
        uri = "/v2/pkg"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def update_pkg(self, **kwargs):
        """
        Update the packages state.
        """

        uri = "/v2/pkg/refresh"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_single_job_status(self, job_id, **kwargs):
        """
        Retieve status of single job.
        """

        uri = f"/v2/jobs/{job_id}/status"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_bulk_jobs(self, name=None, **kwargs):
        """
        Get Jobs or Sequences by name. Pass a valid name of job
        """

        uri = f"/v2/bulk/jobs?name={name}&"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        results.raise_for_status()
        return results.json()

    def create_bulk_jobs(self, bulk_job=None, **kwargs):
        """
        Create a new Mitto job.
        """
        assert isinstance(bulk_job, list)

        uri = "/v2/bulk/jobs"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url=url, json=bulk_job, **kwargs)
        return results.json()

    def create_tags(self, tags, **kwargs):
        """
        Create a new tag in Mitto.
        """
        assert isinstance(tags, dict)

        uri = "/tags"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url, json=tags, **kwargs)
        results.raise_for_status()
        return results.json()

    def get_credentials(self, **kwargs):
        """
        Return all credentials.
        """
        uri = "/credentials"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url, **kwargs)
        return results.json()

    def create_credentials(self, creds, **kwargs):
        """
        Create a new credentials in Mitto instance.
        """
        assert isinstance(creds, dict)

        uri = "/credentials"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.post(url, json=creds, **kwargs)
        return results.json()

    def get_databases(self):
        """
        Get all databases.
        """

        uri = "/v2/databases"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.get(url)
        results.raise_for_status()
        return results.json()

    def update_a_webhook(self, webhook_id, webhook, **kwargs):
        """
        Update a webhook.
        """

        assert isinstance(webhook_id, int)
        assert isinstance(webhook, dict)

        uri = f"/webhooks/{webhook_id}"
        url = f"{self.base_url}{self.api_root}{uri}"

        results = self.session.put(url, json=webhook, **kwargs)
        results.raise_for_status()
        return results.json()
