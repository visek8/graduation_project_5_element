import allure
import requests


@allure.title("api test")
def test_post_image():
    url = "https://img.5element.by/upload/rk/84c/84cfd5aa35e5d03f8fad0a442d0172ee.jpg"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
