from typing import Union
from functools import lru_cache

import pandas as pd

from app.datasources import CSVDataSource, DatabaseDataSource
from app.services.user_data_aggregator.dto import AggregatedUserData


_POSSIBLE_DATA_SOURCES_TYPE = Union[
    CSVDataSource,
    DatabaseDataSource
]


class UserDataAggregator:
    def __init__(self, data_source: _POSSIBLE_DATA_SOURCES_TYPE) -> None:
        self._data_source = data_source

    @property
    @lru_cache()
    def hotspots_data_pd(self) -> pd.DataFrame:
        return pd.DataFrame([
            data.dict() for data in self._data_source.load_hotspots_data()
        ])

    @property
    @lru_cache()
    def connections_data_pd(self) -> pd.DataFrame:
        return pd.DataFrame([
            data.dict() for data in self._data_source.load_connections_data()
        ])

    def aggregate(self, metrics: list):
        for source_user_data in self._data_source.load_users_data():

            aggregated_user_data = AggregatedUserData(
                id=source_user_data.user_id,
                email=source_user_data.email
            )

            user_data_df = pd.DataFrame([source_user_data.dict()])
            user_hotspots_data_df = pd.merge(
                user_data_df, self.hotspots_data_pd, left_on='user_id', right_on='owner_id'
            )
            data_dt = pd.merge(
                user_hotspots_data_df, self.connections_data_pd, on='hotspot_id'
            )

            for metric in metrics:
                metric(aggregated_model=aggregated_user_data).calculate(
                    calculated_dataframe=data_dt
                )

            yield aggregated_user_data

