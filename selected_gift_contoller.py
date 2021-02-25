from models import SelectedGift, User, Person
from base import session
from occasion_controller import get_occasion


def add_selected_gift(gift, person, occasion_id, price):
    occasion = get_occasion(occasion_id)
    selected_gift = SelectedGift(price, gift, occasion, person)
    session.add(selected_gift)
    session.commit()


def get_selected_gifts(user):
    people = session.query(Person).filter(Person.user.has(User.id == user)).all()
    gifts = session.query(SelectedGift).all()
    selected_gifts = []
    for p in people:
        for g in gifts:
            if g.person == p:
                if not g.bought:
                    selected_gifts.append(g)
    return selected_gifts


def get_selected_gift(pk):
    selected_gift = session.query(SelectedGift).filter(SelectedGift.id == pk).first()
    return selected_gift


def get_bought_gifts(user):
    people = session.query(Person).filter(Person.user.has(User.id == user)).all()
    gifts = session.query(SelectedGift).all()
    selected_gifts = []
    for p in people:
        for g in gifts:
            if g.person == p:
                if g.bought:
                    selected_gifts.append(g)
    return selected_gifts


def mark_gift_as_bought(gift, user_id):
    pk = gift.id
    gift_to_buy = session.query(SelectedGift).filter(SelectedGift.id == pk).first()
    gift_to_buy.bought = True
    user = session.query(User).filter(User.id == user_id).first()
    user.remaining_money = user.remaining_money - gift_to_buy.price
    session.commit()
