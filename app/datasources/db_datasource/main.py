from app.datasources import dto
from app.datasources.base import DataSourceInterface


class DatabaseDataSource(DataSourceInterface):
    def load_users_data(self) -> list[dto.User]:
        pass

    def load_hotspots_data(self) -> list[dto.Hotspot]:
        pass

    def load_connections_data(self) -> list[dto.Connection]:
        pass
