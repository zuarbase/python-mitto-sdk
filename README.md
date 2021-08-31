# python-mitto-sdk
Python Mitto SDK

## Overview:

Python library to interact with Mitto's API.

## Installation:
```python
pip install python-mitto-sdk
```

## Usage:
```python
# What's my Mitto version?
from mitto_sdk import Mitto

BASE_URL = "https://{mitto_url}"
API_KEY = ""

mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )

about = mitto.get_about()
version = about["version"]
print(version)
```


## dev notes
## unset PYTHONPATH before creating the python environment
```python
export PYTHONPATH=
```


## Creating .env file with your $MITTO_BASE_URL and $MITTO_API_KEY:
```python
cd /path/to/your/python-mitto-sdk && echo "MITTO_BASE_URL=https://your-mitto.zuarbase.net">.env && echo "MITTO_API_KEY=<YOUR_API_KEY>">>.env
```


## activate .env 
```python
make pyenv
source pyenv/bin/activate
```


## Changing path to examples dir for testing python-mitto-sdk package(please, make sure that you are in python-mitto-sdk folder):
```python
export PYTHONPATH=`pwd`:`pwd`/examples
```

## Example usage of the [Mitto](https://www.zuar.com/products/mitto) Python SDK  
  
```python
├── create_cmd_job.py # create a new cmd job
├── create_job.py # create a new sql job
├── create_job_webhook.py # add a webhook to a job
├── create_jobs_from_template # create jobs using jinja templates
│   ├── create_jobs_from_template.py
│   └── templates
│       └── sql.json # template
├── get_about.py # get info like version, timezone, plugins, etc
├── get_conf_info.py # search job configs
├── get_job_schedule.py # get a job's schedule
├── get_jobs.py # get a list of jobs
├── migrate_to_new_db.py # change jobs using one database to use another
├── start_job.py # start a job
├── update_job.py # update a job with a new config
└── update_job_schedule.py # update a job's scheduling
```


## Running test via command "pytest tests/*" or "make" can create some jobs, so do not be surprised at this.
