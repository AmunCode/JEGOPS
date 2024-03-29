import requests


def get_device_info(imei):
    url = "https://clientapiv2.phonecheck.com/cloud/cloudDB/GetDeviceInfo"

    payload = {
        'Apikey': '3ccc2e79-4167-497d-8262-bc8ef8d9182d',
        'Username': 'jegsons45',
        'IMEI': imei
    }

    response = requests.request("POST", url, data=payload)
    print(response.ok)
    if response.ok:
        device_info = response.json()
        return device_info
    else:
        return False

