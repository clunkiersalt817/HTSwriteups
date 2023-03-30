import requests
import time

while True:
    url = 'https://www.hackthissite.org/missions/basic/11/'
    username = 'clunkiersalt817'
    password = 'nTDVUg6BhdVB4PT'

    response = requests.get(url, auth=(username, password))

    with open('output.txt', 'a') as f:
        f.write(response.text)

    time.sleep(3)