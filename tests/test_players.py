import unittest
from app.use_cases.players import GetPlayersUseCase
from app.repositories.players import NBAAPIPlayersRepository
from app.clients.nba_api import NBAAPIRestClient
from config.config import Config


class TestGetPlayersUseCase(unittest.TestCase):
    def test_execute(self):
        config = Config()

        api_client = NBAAPIRestClient(config.API_KEY, config.API_HOST)
        repository = NBAAPIPlayersRepository(api_client)
        use_case = GetPlayersUseCase(repository)

        page = 0
        per_page = 25
        players = use_case.execute(page, per_page)

        self.assertIsNotNone(players)
        self.assertGreater(len(players), 0)


if __name__ == '__main__':
    unittest.main()
