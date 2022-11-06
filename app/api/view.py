from flask import Blueprint, jsonify, request

from app.datasources import CSVDataSource
from app.services.user_data_aggregator import UserDataAggregator
from app.services.user_data_aggregator.metrics import (
    CreatedHotspotsPerUserMetric,
    HotspotsPerUserWithLocationMetric,
    HotspotsPerUserQualityByScoreMetric,
    HotspotsPerUserByCreatedPeriodMetric,
    UniqueHotspotsPerUserByPeriodMetric
)


api = Blueprint(
    name='api',
    import_name=__name__
)


@api.route('/fetch-metrics')
def index():
    metrics = [
        CreatedHotspotsPerUserMetric,
        HotspotsPerUserWithLocationMetric,
        HotspotsPerUserQualityByScoreMetric,
        HotspotsPerUserByCreatedPeriodMetric,
        UniqueHotspotsPerUserByPeriodMetric
    ]
    try:
        users_limit = int(request.args.get('limit', 10))

        users_data = tuple(
            UserDataAggregator(data_source=CSVDataSource())
            .aggregate(metrics=metrics)
        )

        return jsonify([data.dict() for data in users_data[:users_limit]])
    except Exception:
        return jsonify({'exception': 'Error occurred during processing request'}, 400)
