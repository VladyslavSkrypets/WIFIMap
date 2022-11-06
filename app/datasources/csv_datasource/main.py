import os
from csv import DictReader
from typing import Generator

from app.datasources import dto
from app.datasources.base import DataSourceInterface


_DATA_FOLDER = 'data'


class CSVDataSource(DataSourceInterface):
    _DATA_SOURCE_FOLDER_PASS = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        _DATA_FOLDER
    )

    def _read_data_file(self, file_name: str, map_model) -> Generator:
        file_path = os.path.join(self._DATA_SOURCE_FOLDER_PASS, f"{file_name}.csv")

        with open(file_path, errors='ignore', encoding='utf-8') as data_file:
            return (map_model(**record) for record in tuple(DictReader(data_file)))

    def load_users_data(self) -> Generator[dto.User, None, None]:
        file_name = 'users_test'

        return self._read_data_file(file_name=file_name, map_model=dto.User)

    def load_hotspots_data(self) -> Generator[dto.Hotspot, None, None]:
        file_name = 'hotspots_test'

        return self._read_data_file(file_name=file_name, map_model=dto.Hotspot)

    def load_connections_data(self) -> Generator[dto.Connection, None, None]:
        file_name = 'conns_test'

        return self._read_data_file(file_name=file_name, map_model=dto.Connection)
