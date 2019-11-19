#!/bin/env python

from setuptools import setup, find_packages

fuckcaptcha_classifiers = [
    "Intended Audience :: Developers",
    "License :: Public Domain",
    "Topic :: Software Development :: Libraries",
]

with open("README.rst", "r") as f:
  fuckcaptcha_readme = f.read()

setup(
    name="fuckcaptcha",
    version="0.1.0",
    author="Franc[e]sco",
    author_email="lolisamurai@tfwno.gf",
    url="https://github.com/Francesco149/fuckcaptcha",
    py_modules=["fuckcaptcha"],
    packages=find_packages(),
    package_data={"fuckcaptcha_data": ["fuck.js"]},
    description="bypass reCAPTCHA detection in pyppeteer",
    long_description=fuckcaptcha_readme,
    license="Unlicense",
    classifiers=fuckcaptcha_classifiers,
    keywords="stealth recaptcha captcha chrome chromium headless bypass",
    install_requires=[]
)
