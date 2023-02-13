# External modules
from datetime import datetime
# import json
# from io import BytesIO

# Internal modules
from config.config import Config
from app.clients.nba_api import NBAAPIRestClient
from app.repositories.players import NBAAPIPlayersRepository
from app.use_cases.players import GetPlayersUseCase
from app.data_analysis.players import PlayerDataAnalysis

from infrastructure.logging import Logger
# from infrastructure.data_transform import DataTransform
# from infrastructure.s3_storage import S3Storage


if __name__ == '__main__':
    config = Config()
    logger = Logger(__name__)
    current_time = datetime.now()

    api_client = NBAAPIRestClient(config.API_KEY, config.API_HOST)
    repository = NBAAPIPlayersRepository(api_client)
    use_case = GetPlayersUseCase(repository)

    # Extract
    # page = 0
    # per_page = 25
    players = use_case.execute()
    # logger.debug("Players retreived successfully: {}".format(players))

    # Transform
    player_analysis = PlayerDataAnalysis(players['data'])
    logger.debug(player_analysis.get_dataframe_shape())
    # Load to S3
    # s3_storage = S3Storage(config.S3_BUCKET_NAME,
    #                        config.aws_access_key_id,
    #                        config.aws_secret_access_key)
    # s3_storage.create_bucket()
    # file_content = json.dumps(players)
    # file_like_obj = BytesIO(file_content.encode('utf-8'))
    # s3_storage.upload_fileobj(file_like_obj,
    #                           'players_{}.json'.format(current_time))
