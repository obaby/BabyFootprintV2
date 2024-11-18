import binascii
import math
from datetime import datetime, timedelta, date
import calendar


def get_today_zero_time():
    """
    获取当前零点时间
    """
    time_now = datetime.now()
    zero_time = time_now - timedelta(hours=time_now.hour) - timedelta(minutes=time_now.minute) - timedelta(
        seconds=time_now.second) - timedelta(microseconds=time_now.microsecond)
    return zero_time


def get_current_hour():
    """
    获取当前整点时间
    """
    time_now = datetime.now()
    time_now_hour = time_now - timedelta(minutes=time_now.minute) - timedelta(seconds=time_now.second) - timedelta(
        microseconds=time_now.microsecond)
    return time_now_hour


def get_last_five_minutes_time():
    """
    获取上一个整五分钟时间
    """
    time_now = datetime.now()
    mins = math.floor(time_now.minute / 5) * 5
    time_now_hour = time_now - timedelta(minutes=time_now.minute) - timedelta(seconds=time_now.second) - timedelta(
        microseconds=time_now.microsecond) + timedelta(minutes=mins)
    return time_now_hour


def get_month_start_time():
    now = datetime.now().date()
    this_month_start = datetime(now.year, now.month, 1)
    this_month_end = datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    return this_month_start


def get_month_before_this_time(zero_time):
    if zero_time.month == 1:
        zero_time = date(zero_time.year - 1, 12, 1)
    else:
        zero_time = date(zero_time.year, zero_time.month - 1, 1)
    return zero_time


def get_year_before_this_time(zero_time):
    zero_time = date(zero_time.year - 1, 1, 1)

    return zero_time


def get_month_first_and_last_day(year, month):
    # 获取当前月的第一天的星期和当月总天数
    weekDay, monthCountDay = calendar.monthrange(year, month)
    # 获取当前月份第一天
    firstDay = date(year, month, day=1)
    # 获取当前月份最后一天
    lastDay = date(year, month, day=monthCountDay)
    # 返回第一天和最后一天
    return firstDay, lastDay


def get_past_month_first_and_last_day():
    if date.today().month == 1:
        lastMonthFirstDay = date(date.today().year - 1, 12, 1)
    else:
        lastMonthFirstDay = date(date.today().year, date.today().month - 1, 1)
    lastMonthLastDay = date(date.today().year, date.today().month, 1) - timedelta(1)
    return lastMonthFirstDay, lastMonthLastDay


def get_year_first_and_last_day(now_time):
    this_year_start = datetime(now_time.year, 1, 1)
    this_year_end = datetime(now_time.year + 1, 1, 1) - timedelta(days=1)
    return this_year_start, this_year_end


def get_this_week_start_day():
    today = date.today()
    return today - timedelta(days=today.weekday())


def get_past_week_start_and_end_day():
    today = date.today()
    # threeWeeksAgo_start = today - timedelta(days=today.weekday() + 21)
    # threeWeeksAgo_end = today - timedelta(days=today.weekday() + 15)
    # twoWeeksAgo_start = today - timedelta(days=today.weekday() + 14)
    # twoWeeksAgo_end = today - timedelta(days=today.weekday() + 8)
    last_week_start = today - timedelta(days=today.weekday() + 7)
    last_week_end = today - timedelta(days=today.weekday() + 1)
    return last_week_start, last_week_end


def get_week_start_and_end_day_at_date(q_date):
    t = q_date - timedelta(days=q_date.weekday())
    e = t + timedelta(days=7)
    return t, e


def get_past_week_start_and_end_day_at_date(q_date):
    last_week_start = q_date - timedelta(days=q_date.weekday() + 7)
    last_week_end = q_date - timedelta(days=q_date.weekday() + 1)
    return last_week_start, last_week_end


def crc32_to_hex(s):
    crc = binascii.crc32(s.encode())
    return hex(crc)[2:].zfill(8)


if __name__ == "__main__":
    # print(get_last_five_minutes_time())
    # print(get_month_start_time())
    # print(get_today_zero_time() - get_month_start_time())
    print(get_month_first_and_last_day(get_today_zero_time().year, get_month_start_time().month))
    # print(get_past_month_first_and_last_day())
    # print(get_past_week_start_and_end_day())
    print(get_current_hour())
