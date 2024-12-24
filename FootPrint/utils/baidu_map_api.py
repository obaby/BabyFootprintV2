import requests


def get_location_cordinate(location_name, server_key):
    resp = requests.get('https://api.map.baidu.com/geocoding/v3/?address='+location_name+ '&output=json&ak='+ server_key)

    print(resp.json())
    js = resp.json()
    if js['status'] == 0:
        return js['result']['location']['lng'],js['result']['location']['lat']
    return None, None

if __name__ == '__main__':
    get_location_cordinate('上海','')