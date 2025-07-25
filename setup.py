import os

from setuptools import find_packages, setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


LONG_DESCRIPTION = read("README.md")


setup(
    name="tempmailwrapper",
    version="0.0.7",
    author="Jim",
    author_email="jimballoonsgit@gmail.com",
    url="https://github.com/jim-vl/tempmailwrapper",
    description="API wrapper for Temp Mail API.",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    keywords=[
        "python",
        "tempmail",
        "temporary",
        "email",
        "wrapper",
    ],
    download_url="https://github.com/jim-vl/tempmailwrapper/archive/refs/tags/0.0.7.tar.gz",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
