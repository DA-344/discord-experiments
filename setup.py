from setuptools import setup

version: str = "0.0.1"
description: str = "A wrapper to the Discord Experiments API"
long_description: str = open("README.md", "r").read()

setup(
    name = "discord-experiments",
    version = version,
    author = "Developer Anonymous",
    author_email = "dev.anony.8593@gmail.com",
    description = description,
    long_description = long_description,
    packages = ["discord-experiments", "discord-experiments.utils"],
    install_requires = ["discord.py"],
    keywords = ["discordexperiments", "experiments", "dcexps", "discordexps"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Recommended Python Version :: 3.X"
    ]
)
