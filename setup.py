from distutils.core import setup
from setuptools import find_packages

setup(
    name="FlaskNER",
    version="0.0.1",
    description="Simple NER app",
    packages=find_packages(include=["static", "templates"],exclude=["test"])

)