import requests

url = 'https://api.superjob.ru/2.0/vacancies/'
response = requests.get(url)
s = response.json()

def test_get_from_superjob():
    assert s != None