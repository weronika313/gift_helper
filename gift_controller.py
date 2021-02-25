from models import Gift
from base import session
from gift_category_controller import get_category


def add_gift(name, price_min, price_max, category):
    gift = Gift(name, price_min, price_max, category)
    session.add(gift)
    session.commit()
    return gift


def get_all_gifts_from_chosen_category(category):
    gifts = session.query(Gift).filter(Gift.category == category).all()
    return gifts


def get_all_gifts():
    gifts = session.query(Gift).all()
    return gifts


def get_gift(pk):
    gift = session.query(Gift).filter(Gift.id == pk).first()
    return gift
