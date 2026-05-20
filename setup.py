from pathlib import Path
from setuptools import setup, find_packages

BASE_DIR = Path(__file__).parent
README = BASE_DIR / "README.md"

long_description = README.read_text(encoding="utf-8") if README.exists() else "CLI for communicating with the RackTables API"

setup(
    name="rackctl",
    version="1.0.0",
    description="CLI for communicating with the RackTables API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="INPE/CPTEC - COIDS",
    author_email="luis.nogueira@inpe.br",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "python-dotenv",
        "pyyaml",
    ],
    data_files=[
        ('/etc/rackctl', ['config/rackctl.yaml'])
    ],
    entry_points={
        "console_scripts": [
            "rackctl=rackctl.main:main"
        ]
    },
    python_requires=">=3.8",
)