import requests
import json


BASE_URL = "https://euw1.api.riotgames.com"
with open('config.json') as f:
    API_KEY = json.load(f)['api_key']


def __request(path):
    return requests.get(f"{BASE_URL}{path}?api_key={API_KEY}").json()


def get_summoner_data(summonername):
    return __request(f"/lol/summoner/v4/summoners/by-name/{summonername}")
