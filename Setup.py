
from setuptools import setup, find_packages
from pathlib import Path
import os

os.chdir(str(Path(__file__).parent))
with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='alijazayeri-geocoding-device',
    version='0.0.1',
    description='Service to retrieve lat/lng of an address.',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    author='Ali Jazayeri',
    author_email='ali.jazayeri@ualberta.ca'
)