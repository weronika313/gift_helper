from models import GiftCategory
from base import session


def get_gift_categories():
    categories = session.query(GiftCategory).all()
    return categories


def get_category(pk):
    category = session.query(GiftCategory).filter(GiftCategory.id == pk).first()
    return category
