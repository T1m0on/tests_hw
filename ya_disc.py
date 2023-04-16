import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.link_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.link_list_of_files = 'https://cloud-api.yandex.net/v1/disk/resources/public'
        self.bad_link = 'https://cloud-api.yandex.net/v1/disk/resources/wefgwe'
        self.params = {'path': 'test'}
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self):
        response = requests.put(self.link_create_folder, headers=self.headers, params=self.params)
        return response.status_code

    def check_folder(self):
        response = requests.get(self.link_list_of_files, headers=self.headers, params=self.params)
        return response.status_code

    def failure_function(self):
        response = requests.get(self.bad_link, headers=self.headers, params=self.params)
        return response.status_code


