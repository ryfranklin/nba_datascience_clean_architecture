from pandas import DataFrame


class PlayerDataAnalysis:
    def __init__(self, players_data: dict):
        self.players_df = DataFrame(players_data)

    def get_dataframe_shape(self):
        return self.players_df.shape

    def get_top_ten_players_by_points_per_game(self):
        top_ten_players = self.players_df.sort_values(
            by='points_per_game', ascending=False
        ).head(10)

        return top_ten_players
