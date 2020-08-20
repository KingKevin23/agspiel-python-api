#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agspiel-python-api",
    version="0.3.1",
    author="KingKevin23",
    author_email="code@kingkevin.de",
    description="Python API für das AG-Spiel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/KingKevin23/agspiel-python-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "webbot>=0.33",
        "requests>=2.24.0",
        "beautifulsoup4>=4.9.1"
    ],
)