import requests

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        str = ""

        for k, v in data.items():
            str += f'{k} : {v}\n'
        
        return str
        
    except requests.exceptions.ConnectionError:
        return "Error"