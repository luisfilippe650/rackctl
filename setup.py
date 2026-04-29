from setuptools import setup, find_packages

setup(
    name="rackctl",
    version="1.0.0",
    description="CLI para comunicação com a API do RackTables",
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