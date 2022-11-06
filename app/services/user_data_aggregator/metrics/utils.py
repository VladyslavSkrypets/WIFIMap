from datetime import datetime, date, timedelta

from app.services.user_data_aggregator import dto


def last_year_date_period() -> dto.DatetimePeriod:
    past_year = datetime.now().year - 1

    return dto.DatetimePeriod(
        date_start=date(year=past_year, month=1, day=1),
        date_end=date(year=past_year, month=12, day=31),
    )

def last_month_date_period() -> dto.DatetimePeriod:
    first_day_current_month = date.today().replace(day=1)

    last_day_prev_month = first_day_current_month - timedelta(days=1)
    first_day_prev_month = first_day_current_month - timedelta(days=last_day_prev_month.day)

    return dto.DatetimePeriod(
        date_start=first_day_prev_month,
        date_end=last_day_prev_month
    )

def last_week_date_period() -> dto.DatetimePeriod:
    today_date = date.today()

    last_day_prev_week = today_date - timedelta(days=today_date.weekday()) - timedelta(days=1)
    first_day_prev_week = last_day_prev_week - timedelta(days=6)

    return dto.DatetimePeriod(
        date_start=first_day_prev_week,
        date_end=last_day_prev_week
    )
