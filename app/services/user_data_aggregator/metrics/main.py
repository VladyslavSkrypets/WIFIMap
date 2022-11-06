from app.services.user_data_aggregator.metrics.base import MetricInterface

import pandas as pd

from app.services.user_data_aggregator import dto
from app.services.user_data_aggregator.metrics.utils import (
    last_month_date_period,
    last_week_date_period
)


class CreatedHotspotsPerUserMetric(MetricInterface):
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        self.aggregated_model.hotspots_created_count, _ = calculated_dataframe.shape


class HotspotsPerUserWithLocationMetric(MetricInterface):
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        hotpots_with_location = calculated_dataframe[
            calculated_dataframe['foursquare_id'].notnull() |
            calculated_dataframe['google_place_id'].notnull()
        ]

        self.aggregated_model.hotspots_with_location_count, _ = hotpots_with_location.shape


class HotspotsPerUserQualityByScoreMetric(MetricInterface):
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        calculated_dataframe = calculated_dataframe[calculated_dataframe['score_v4'].notnull()]

        good_hotspots_count, _ = calculated_dataframe[
            calculated_dataframe['score_v4'] > 0.6
        ].shape

        normal_hotspots_count, _ = calculated_dataframe[
            (calculated_dataframe['score_v4'] < 0.6) &
            (calculated_dataframe['score_v4'] > 0.3)
        ].shape

        bad_hotspots_count, _ = calculated_dataframe[
            calculated_dataframe['score_v4'] < 0.3
        ].shape
        
        self.aggregated_model.hotspots_count_quality_by_score = dto.HotspotsCountQuality(
            good_hotspots=good_hotspots_count,
            normal_hotspots=normal_hotspots_count,
            bad_hotspots_count=bad_hotspots_count
        )


class HotspotsPerUserByCreatedPeriodMetric(MetricInterface):
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        all_time_count, _ = calculated_dataframe.shape

        last_month_dates = last_month_date_period()
        last_month_count, _ = calculated_dataframe[
            (calculated_dataframe['hotspot_created_at'] >= last_month_dates.date_start) &
            (calculated_dataframe['hotspot_created_at'] <= last_month_dates.date_end)
        ].shape

        last_week_dates = last_week_date_period()
        last_week_count, _ = calculated_dataframe[
            (calculated_dataframe['hotspot_created_at'] >= last_week_dates.date_start) &
            (calculated_dataframe['hotspot_created_at'] <= last_week_dates.date_end)
        ].shape

        self.aggregated_model.hotspots_count_by_created_period = dto.HotspotsCountCreatedPeriod(
            all_time=all_time_count,
            last_month=last_month_count,
            last_week=last_week_count
        )


class UniqueHotspotsPerUserByPeriodMetric(MetricInterface):
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        pass
