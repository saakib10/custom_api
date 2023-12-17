from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_api/__init__.py
from custom_api import __version__ as version

setup(
	name="custom_api",
	version=version,
	description="Custom API",
	author="Invento Software Limited",
	author_email="munim@invento.com.bd",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
