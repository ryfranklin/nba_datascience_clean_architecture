import pandas as pd


class DataTransform:
    def __init__(self, data):
        self.data = data

    def transform_data(self):
        dataframe = pd.DataFrame(self.data)
        return dataframe
