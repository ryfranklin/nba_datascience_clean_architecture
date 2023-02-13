from abc import ABC, abstractmethod
from typing import List
import requests


class NBAAPI(ABC):
    @abstractmethod
    def get_players(self) -> List[dict]:
        pass


class NBAAPIRestClient(NBAAPI):
    def __init__(self, api_key: str, api_host: str):
        self.api_key = api_key
        self.api_host = api_host

    def get_players(self) -> List[dict]:
        url = "https://free-nba.p.rapidapi.com/players"
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
