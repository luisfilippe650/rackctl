from setuptools import setup, find_packages

setup(
    name="rackctl",
    version="1.0.0",
    description="CLI for communicating with the RackTables API",
    author="INPE/CPTEC - COIDS",
    author_email="luis.nogueira@inpe.br",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "requests",
        "python-dotenv",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "rackctl=src.__main__:main"
        ]
    },
    python_requires=">=3.8",
)