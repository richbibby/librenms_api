from httpx import Client
from pprint import pprint as pp

api = Client(base_url="http://yourlibrenms_ip_ddr/api/v0/")
api.headers['X-Auth-Token'] = "your_auth_token"


def get_bgp_data_as_json():
    result = api.get('/bgp')
    pp(result.json())


if __name__ == '__main__':
    get_bgp_data_as_json()
