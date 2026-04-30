from setuptools import setup, find_packages

setup(
    name="rackctl",
    version="1.0.0",
    description="CLI for communicating with the RackTables API (https://github.com/luisfilippe650/racktables-rest-api) ",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "rackctl=src.__main__:main"
        ]
    },
)