from setuptools import setup, find_packages

setup(
    name="ezauv",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[],
    description="Framework for modular AUVs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Matthew Baltay",
    author_email="baltaym28@bcdschool.org",
    url="https://github.com/modular-auv/modular-auv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)