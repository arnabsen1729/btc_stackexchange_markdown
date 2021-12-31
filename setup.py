import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="stackoverflow_markdown",
    version="0.1.0",
    author="Arnab Sen",
    author_email="arnabsen1729@gmail.com",
    description=("Convert stackoverflow answers to markdown format."),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests', 'html2text'
    ],
    entry_points={
        'console_scripts': [
            'somd = stackoverflow_markdown.scripts.somd:cli',
        ],
    },
    long_description=read('README.md'),
)
