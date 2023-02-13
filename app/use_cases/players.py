from typing import List


class GetPlayersUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self) -> List[dict]:
        return self.repository.get_players()
