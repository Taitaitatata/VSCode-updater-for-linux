import os
import pprint
import time
import urllib.error
import urllib.request
import subprocess

subprocess.call(["./rmpack.sh"])

print("Hi, I am Visual Studio Code Updater(Linux armhf Edition) Download 57.1MB")
print("Downloading...")

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
url = 'https://aka.ms/linux-arm64-deb'
dst_path = 'code.deb'
download_file(url, dst_path)
print("Package Installing the package")
time.sleep(5)
subprocess.call(["./installpack.sh"])
print("Ver.2020.11.29.1 Copyright 2020 Taitaitatata All Rights Reserved.")