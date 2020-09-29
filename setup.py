import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="price_prediction_moddel",
    description="End to end lightGBM regression model to predict house prices in Beijing",
    author="Bowen",
    packages=find_packages(exclude=["data", "figures", "output", "notebooks"]),
    long_description=read("README.md"),
)
