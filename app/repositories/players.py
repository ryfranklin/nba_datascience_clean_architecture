# app/repositories/players.py
from abc import ABC, abstractmethod
from typing import List


class PlayersRepository(ABC):
    @abstractmethod
    def get_players(self) -> List[dict]:
        pass


class NBAAPIPlayersRepository(PlayersRepository):
    def __init__(self, api_client):
        self.api_client = api_client

    def get_players(self) -> List[dict]:
        response = self.api_client.get_players()
        return response
