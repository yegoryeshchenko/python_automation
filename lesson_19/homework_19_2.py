# Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль request зробить
# через POST upload якогось зображення на сервер, за допомогою GET отримає посилання на цей файл str
# і потiм за допомогою DELETE зробить видалення файлу з сервера
import os

import requests

base_url = 'http://127.0.0.1:8080'
test_image = "homework_19_test_picture.jpg"
folder_path = os.path.join(os.getcwd(), 'source_images')


def upload_file(file_name):
    file_path = os.path.join(folder_path, file_name)

    url = base_url + '/upload'

    with open(file_path, 'rb') as file:
        files = {'image': file}
        response = requests.post(url, files=files)
    response.raise_for_status()
    return response


def get_image_url(file_name):
    url = base_url + '/image' + '/' + file_name

    headers = {
        'Content-Type': 'text',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    image_url = data.get('image_url')
    return image_url


def delete_image(file_name):
    url = base_url + '/delete' + '/' + file_name
    response = requests.delete(url)
    data = response.json()
    return data.get('message')


def test_image_should_be_successfully_uploaded():
    image_for_test = "homework_19_test_picture.jpg"
    response = upload_file(image_for_test)
    data = response.json()
    expected_image_url = f'{base_url}/uploads/{image_for_test}'
    actual_image_url = data.get('image_url')
    assert expected_image_url == actual_image_url, 'image_url is not valid'


def test_verify_image_url():
    image_for_test = "homework_19_test_picture.jpg"
    upload_file(image_for_test)
    expected_get_image_url = f'{base_url}/uploads/{image_for_test}'
    assert expected_get_image_url == get_image_url(image_for_test), 'image_url is not valid'


def test_image_should_be_successfully_deleted():
    image_for_test = "homework_19_test_picture.jpg"
    upload_file(image_for_test)
    expected_message = f'Image {image_for_test} deleted'
    assert expected_message == delete_image(image_for_test), 'message is not valid'
