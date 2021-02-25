from models import GiftIdea
from base import session


def create_gift_idea(gift, occasion, person):
    gift_idea = GiftIdea(gift, occasion, person)
    session.add(gift_idea)
    session.commit()


def get_gift_ideas_for_selected_occasion(occasion, person):
    gift_ideas = session.query(GiftIdea).filter(GiftIdea.occasion == occasion,
                                          GiftIdea.person == person).all()
    gifts = []
    for g in gift_ideas:
        gift = g.gift
        gifts.append(gift)
    return gifts


def get_all_gift_ideas(person):
    gift_ideas = session.query(GiftIdea).filter(GiftIdea.person == person).all()
    gifts = []
    for g in gift_ideas:

        print(g.occasion.name)
        gift = g.gift
        gifts.append(gift)
    return gifts


def get_gift_ideas_for_selected_occasion_and_price_range(occasion, price_min, price_max, person):
    gift_ideas = session.query(GiftIdea).filter(GiftIdea.occasion == occasion,
                                          GiftIdea.person == person).all()
    gifts = []
    for g in gift_ideas:
        gift = g.gift
        if gift.price_min <= price_min and gift.price_max >= price_max:
            gifts.append(gift)
    return gifts
