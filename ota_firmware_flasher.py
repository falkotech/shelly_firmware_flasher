"""
This script starts a server on port 8000 and then sends a GET request to Shelly device, 
so it downloads the latest firmware to the Shelly.
Requires that you have the latest firmware file somewhere in the same directory as this script.
"""
from http.server import test, SimpleHTTPRequestHandler
import requests
from requests.exceptions import ConnectTimeout
import threading
import socket
import time



old_version = True

def run_server():
    print('Starting server.............\n')
    test(SimpleHTTPRequestHandler, port=8000)


# Check if Shelly is online
def shelly_online():
    try:
        print('Checking Shelly........\n\n')
        r = requests.get('http://192.168.33.1/settings', timeout=3)
        if r.status_code == 200:
            print('Shelly is online')
            return True
    except ConnectTimeout:
        inform_of_error_and_show_config()  


def inform_of_error_and_show_config():
    print('ERROR: Request has timed out. Shelly can not be reached.')
    print('Please check your network connection and try again.')
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print(f"Your Computer Name is: {hostname}")
    print(f"Your Computer IP Address is: {IPAddr}\n") 


def latest_version():
    try:
        res = requests.get('http://192.168.33.1/settings',timeout=1).json()
        if res['fw'] == "20220209-094058/v1.11.8-g8c7bb8d":
            print('Shelly is up to date!!\n')
            return True
        else:
            print('...Shelly is NOT up to date')
            return False
    except ConnectTimeout:
        inform_of_error_and_show_config()


def download_file():
    # Curl to Shelly so it can download the file
    requests.get('http://192.168.33.1/ota?url=http://192.168.33.2:8000/v1.11.8/SHPLG-S.zip')
    print('Shelly downloaded the file')


def start():
    # Check if Shelly is online
    if shelly_online() and not latest_version():
        # run server in separate thread
        thread = threading.Thread(target=run_server)
        thread.start()
        time.sleep(2)
        # Curl to Shelly so it can download the file
        download_file()
        # wait while updating
        time.sleep(2)
        # Check version
        res = requests.get('http://192.168.33.1/settings',timeout=1).json()
        if res['fw'] == "20220209-094058/v1.11.8-g8c7bb8d":
            print('Shelly is up to date!!\n')

        

if __name__ == '__main__':
    start()