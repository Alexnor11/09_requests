import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.API_BASE_URL = 'https://cloud-api.yandex.net/'
        self.token = token
        self.headers = {'Authorization': token}

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # 1-й запрос - получение ссылки для загрузки файла
        r = requests.get(self.API_BASE_URL + 'v1/disk/resources/upload/', params={
            'path': 'py-43/bears.jpg'
        }, headers=self.headers)
        upload_url = r.json()['href']  # Получаем ссылку
        pprint(upload_url)

        # 2-й запрос - загрузка файла на диск по полной ссылке
        with open(file_path, 'rb') as f:
            data = f.read()
            r = requests.put(upload_url, headers=self.headers, files={'file': data})
            # проверка доступности ресурса
            print(r.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'bears.jpg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)