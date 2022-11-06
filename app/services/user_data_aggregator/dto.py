from datetime import date
from typing import NamedTuple

from pydantic import BaseModel, EmailStr


class DatetimePeriod(NamedTuple):
    date_start: date
    date_end: date


class HotspotsCountPeriod(BaseModel):
    all_time: int = 0
    last_month: int = 0
    last_week: int = 0


class HotspotsCountCreatedPeriod(HotspotsCountPeriod):
    pass


class UniqueHotspotsCountPeriod(HotspotsCountPeriod):
    last_year: int = 0


class HotspotsCountQuality(BaseModel):
    good_hotspots: int = 0
    normal_hotspots: int = 0
    bad_hotspots: int = 0


class AggregatedUserData(BaseModel):
    id: int
    email: EmailStr
    hotspots_created_count: int = 0
    hotspots_with_location_count: int = 0
    hotspots_count_by_created_period: HotspotsCountCreatedPeriod = HotspotsCountCreatedPeriod()
    hotspots_count_quality_by_score: HotspotsCountQuality = HotspotsCountQuality()
    # unique_hotspots_by_period:
