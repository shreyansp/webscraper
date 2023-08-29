from urllib import request
from zipfile import ZipFile
from os import path, mkdir, system
import logging as log
import venv
import subprocess
import sys

dirname, filename = path.split(path.abspath(__file__))
location = path.join(dirname,'drivers')
log.basicConfig(level=log.INFO)

if not path.exists(location):
    mkdir(location)
    log.info(f'mkdir {location}')

download_location = path.join(location,'chromedriver_win32.zip')
if not path.exists(path.join(location,'chromedriver.exe')):
    if not path.exists(download_location):
        chrome_version = '108.0.5359.71' #'107.0.5304.18'
        chrome_driver_url = f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip'
        request.urlretrieve(chrome_driver_url, download_location)
        log.info(f'Downloading {chrome_driver_url}')
        ZipFile(download_location).extractall(location)
        log.info(f'Unzipping {download_location}')
else:
    log.info(f'chromedriver exists in: {location}')

venv_location = path.join(dirname, 'venv')
if not path.exists(venv_location):
    log.info(f'Creating python venv in: {venv_location}')
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "virtualenv"])  # package
    # subprocess.check_call([sys.executable, "-m", "virtualenv", "venv"])  # package
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])  # package
    # venv.create('venv')
log.info(f'Activating venv: {venv_location}')

venv_activate_path = path.join(venv_location, r'Scripts\activate.ps1')

# system(f'bash --rcfile ./venv.sh')
# system(venv_activate_path)
