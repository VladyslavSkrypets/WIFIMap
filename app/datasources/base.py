from abc import ABC, abstractmethod

from app.datasources import dto


class DataSourceInterface(ABC):
    @abstractmethod
    def load_users_data(self) -> list[dto.User]:
        pass

    @abstractmethod
    def load_hotspots_data(self) -> list[dto.Hotspot]:
        pass

    @abstractmethod
    def load_connections_data(self) -> list[dto.Connection]:
        pass
