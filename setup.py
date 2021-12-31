import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="btc_stackexchange_markdown",
    version="0.1.0",
    author="Arnab Sen",
    author_email="arnabsen1729@gmail.com",
    description=(
        "Fetch bitcoin stackexchange answers and export as markdown files."),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests', 'html2text'
    ],
    entry_points={
        'console_scripts': [
            'btcmd = btc_stackexchange_markdown.scripts.btcmd:cli',
        ],
    },
    long_description=read('README.md'),
)
