# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером
# “Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових
# запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
# Завдання потрiбно зробити використовуючи модуль requests
import os

import pytest
import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


def get_img_urls() -> list:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    photos = data.get('photos', [])

    img_urls = [photo.get('img_src') for photo in photos if 'img_src' in photo]
    return img_urls


def download_img_by_url(img_url, file_name):
    response = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(response.content)


@pytest.fixture(autouse=True)
def cleanup_after_test():
    yield

    images = ['mars_photo1.jpg', 'mars_photo2.jpg']
    for image in images:
        if os.path.exists(image):
            os.remove(image)
        print(f"Cleaned up: Removed '{image}'")


@pytest.mark.parametrize("img_url, image_name", [
    (get_img_urls()[0], 'mars_photo1.jpg'),
    (get_img_urls()[1], 'mars_photo2.jpg')
])
def test_download_file(img_url, image_name):
    download_img_by_url(img_url, image_name)

    assert os.path.exists(image_name), f"'{image_name}' was not downloaded"
