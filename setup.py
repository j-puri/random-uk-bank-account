from setuptools import setup, find_packages
import os

def get_long_description():
    with open("./README.md", "r") as fh:
        return fh.read()


def get_requirements():
    with open("./requirements.txt", "r") as requirements:
        install_requires = requirements.read().splitlines()
        print(f"Setting install_requires to {install_requires}")
        return install_requires


setup(
    name='random-uk-bank-account',
    version=os.getenv("VERSION", "0.0.1"),
    author='j.puri',
    author_email='j-puri.github@outlook.com',
    packages=find_packages(exclude=["*test*"]),
    url='https://github.com/j-puri/random-uk-bank-account',
    description='Random UK Bank Account Generator',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=get_requirements(),
)
