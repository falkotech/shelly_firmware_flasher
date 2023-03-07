# Introduction 

**ota_firmware_flasher** starts a server on port 8000 and then sends a GET request to Shelly device, 
so it downloads the latest firmware to the Shelly from your device without needing an actual internet connection.
It does require that you have the latest firmware file somewhere in the same directory as this script.

This script is written to significantly reduce the time needed to flash shelly devices over-the-air with updated firmware. This is very useful if you have lots of Shelly devices to update.
It makes use of the [HTTP api endpoints available for Shelly devices.](https://shelly-api-docs.shelly.cloud/gen1/#common-http-api)

##Before 
you would have to:
- Connect to shelly device
- Enter wifi credentials
- Reboot shelly and find ip on your network
- Connect to shelly and send GET request to download firmware OTA

##Now 
- all you need to do is connect to shelly and run `ota_firmware_flasher.py`