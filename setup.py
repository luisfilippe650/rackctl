from setuptools import setup, find_packages

setup(
    name="rackctl",
    version="1.0.0",
    description="CLI for communicating with the RackTables API",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "rackctl=src.__main__:main"
        ]
    },
)