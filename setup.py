from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in taysir/__init__.py
from taysir import __version__ as version

setup(
	name="taysir",
	version=version,
	description="A coran school management system",
	author="S-Amine",
	author_email="saidi.amine.p@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
