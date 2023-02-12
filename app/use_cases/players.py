from typing import List


class GetPlayersUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, page: int, per_page: int) -> List[dict]:
        return self.repository.get_players(page, per_page)
