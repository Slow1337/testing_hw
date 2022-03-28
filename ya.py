import requests

class YaActor():
    def __init__(self, token: str):
        self.token = token
        self.uri = 'https://cloud-api.yandex.net/v1/disk/'
        self.path = ''
    
    def get_directory_info(self, path: str):
        "Метод получать информацию о папке"
        self.path = path
        method = 'resources'
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': path
        }
        url = f'{self.uri}{method}'
        response = requests.get(url=url, headers=headers, params=params)
        return response

    def make_directory(self, path: str):
        """Метод создает папку на яндекс.диске"""
        self.path = path
        method = 'resources'
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': path
        }
        url = f'{self.uri}{method}'
        response = requests.put(url=url, headers=headers, params=params)
        return response

with open('yatoken.txt', 'r', encoding='utf-8') as f:
    yatoken = f.readline().strip('\n')

ya_instance = YaActor(yatoken)
result = ya_instance.get_directory_info('ass')
result = result.status_code
print(result)