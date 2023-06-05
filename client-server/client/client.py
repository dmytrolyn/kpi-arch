from urllib.request import urlopen, Request
import json

api_url = 'http://localhost:3001'

class Client:
    def get_pens(self):
        url = f'{api_urL}/api/pens'
        response = urlopen(url)
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return None

    def add_pen(self, pen_type):
        url = f'{api_url}/api/pens'
        data = {'pen': pen_type}
        data = json.dumps(data).encode()
        request = Request(url, data=data, headers={'Content-Type': 'application/json'})
        response = urlopen(request)
        if response.status == 200:
            return 'Successfully created'
        else:
            return None