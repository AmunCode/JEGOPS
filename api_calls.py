import requests

def get_device_info(imei):
    url = "https://clientapiv2.phonecheck.com/cloud/cloudDB/GetDeviceInfo"

    payload = {
        'Apikey': '3ccc2e79-4167-497d-8262-bc8ef8d9182d',
        'Username': 'jegsons45',
        'IMEI': imei
    }

    response = requests.request("POST", url, data=payload)

    device_info = response.json()

    # print(device_info)

    print(device_info['BatteryHealthPercentage'])

get_device_info('353220104534844')
