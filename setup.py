from pip.req import parse_requirements
from setuptools import setup, find_packages

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')
install_reqs_dev = parse_requirements('requirements_dev.txt')

# reqs is a list of requirements.txt
# reqs_dev is a list of requirements_dev.txt
reqs = install_reqs
reqs_dev = install_reqs_dev

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python-mitto-sdk",
    version="0.0.7",
    author="Justin Freels",
    author_email="justin@zuar.com",
    description="Python library to interact with Mitto's API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfreels/python-mitto-sdk",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        reqs,
        reqs_dev
    ],
    extras_require={
        "dev": [
            "setuptools",
            "twine",
            "wheel",
            "python-dotenv"
        ]
    },
    python_requires='>=3.6',
)
