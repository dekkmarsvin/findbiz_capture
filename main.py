import os
import selenium
import logging
from logger import getlogger

logger = getlogger()

def get_chrome_ver():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Google\\Chrome\\BLBeacon")
    chrome_version = winreg.QueryValueEx(key, "version")[0]
    return chrome_version

def prepare_chrome_driver():
    import requests
    LATEST_DRIVER_URL = "https://chromedriver.storage.googleapis.com/index.html?path="
    chrome_version = get_chrome_ver()
    chrome_version = chrome_version[0:chrome_version.rfind('.')]
    LATEST_RELEASE_URL = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version}"
    logger.info(f"chrome_version:{chrome_version}")
    print("check current driver version")
    print("check latest driver version")
    req_LATEST_RELEASE = requests.get(LATEST_RELEASE_URL)
    if(req_LATEST_RELEASE.status_code == requests.codes.ok):
        logger.debug(f"LATEST_RELEASE:{req_LATEST_RELEASE.text}")

def main():
    prepare_chrome_driver()

if __name__ == "__main__":
    main()