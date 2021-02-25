from models import Occasion
from base import session
from datetime import date
import datetime


def get_occasions():
    occasions = session.query(Occasion).all()
    return occasions


def get_occasion(pk):
    occasion = session.query(Occasion).filter(Occasion.id == pk).first()
    return occasion


def get_next_occasion():
    occasions = session.query(Occasion).all()
    today_day = datetime.datetime.now().day
    today_month = datetime.datetime.now().month
    min_occasion_month = 1000
    min_occasion_day = 1000

    for occasion in occasions:
        day = occasion.day
        month = occasion.month
        if min_occasion_month >= (month - today_month) >= 0:
            if min_occasion_day >= (day - today_day) >= 0:
                next_occasion = occasion
                min_occasion_day = day - today_day
                min_occasion_month = month - today_month

    return next_occasion









