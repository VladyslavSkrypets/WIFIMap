import re
from datetime import datetime, date

from pydantic import (
    BaseModel as PydanticBaseModel,  # noqa
    EmailStr,
    validator,
    Field
)


class BaseModel(PydanticBaseModel):
    class Config:
        anystr_strip_whitespace = True  # noqa

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):  # noqa
        if v == '':
            return None
        return v

    @staticmethod
    def parse_date(datetime_str: str) -> date:
        pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        date_str = re.search(pattern, datetime_str).group()
        return datetime.strptime(date_str, '%Y-%m-%d').date()


class User(BaseModel):
    user_id: int = Field(alias='id')
    email: EmailStr
    user_created_at: str | date = Field(alias='created_at')
    user_updated_at: str | date = Field(alias='updated_at')

    def __init__(self, **data):
        super().__init__(**data)

        self.user_created_at = self.parse_date(self.user_created_at)
        self.user_updated_at = self.parse_date(self.user_updated_at)


class Connection(BaseModel):
    connection_id: int = Field(alias='id')
    installation_id: int
    hotspot_id: int
    connected_at: str | date

    def __init__(self, **data):
        super().__init__(**data)

        self.connected_at = self.parse_date(self.connected_at)


class Hotspot(BaseModel):
    hotspot_id: int = Field(alias='id')
    owner_id: int
    score_v4: float | None
    foursquare_id: str | None
    google_place_id: str | None
    hotspot_created_at: str | date = Field(alias='created_at')

    def __init__(self, **data):
        super().__init__(**data)

        self.hotspot_created_at = self.parse_date(self.hotspot_created_at)
