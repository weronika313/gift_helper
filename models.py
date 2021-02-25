from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from base import engine

Base = declarative_base(engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column('username', String(32))
    money_for_gifts = Column('money_for_gifts', Numeric)
    remaining_money = Column('remaining_money', Numeric)
    password = Column('password', String(120))

    def __init__(self, username, money_for_gifts, remaining_money, password):
        self.username = username
        self.money_for_gifts = money_for_gifts
        self.remaining_money = remaining_money
        self.password = password


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    surname = Column('surname', String(32))
    birthday_day = Column('birthday_day', Integer, nullable=True)
    birthday_month = Column('birthday_month', Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('people_groups.id'))

    selected_gift = relationship("SelectedGift", uselist=False, back_populates="person")
    group = relationship("PeopleGroup")
    user = relationship("User")

    def __init__(self, name, surname, birthday_day, birthday_month, group, user):
        self.name = name
        self.surname = surname
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.group = group
        self.user = user


class GiftIdea(Base):
    __tablename__ = 'gift_ideas'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    gift_id = Column(Integer, ForeignKey('gifts.id'))
    occasion_id = Column(Integer, ForeignKey('occasions.id'))

    gift = relationship("Gift")
    occasion = relationship("Occasion")
    person = relationship("Person")

    def __init__(self, gift, occasion, person):
        self.gift = gift
        self.occasion = occasion
        self.person = person


class PeopleGroup(Base):
    __tablename__ = 'people_groups'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(60))

    def __init__(self, name):
        self.name = name


class Gift(Base):
    __tablename__ = 'gifts'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(60))
    price_min = Column('price_min', Numeric)
    price_max = Column('price_max', Numeric)
    category_id = Column(Integer, ForeignKey('gift_categories.id'))

    category = relationship("GiftCategory")

    def __init__(self, name, price_min, price_max, category):
        self.name = name
        self.price_min = price_min
        self.price_max = price_max
        self.category = category


class GiftCategory(Base):
    __tablename__ = 'gift_categories'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(60))

    def __init__(self, name):
        self.name = name


class SelectedGift(Base):
    __tablename__ = 'selected_gifts'
    id = Column(Integer, primary_key=True)
    price = Column('price', Numeric)
    person_id = Column(Integer, ForeignKey('people.id'))
    gift_id = Column(Integer, ForeignKey('gifts.id'))
    occasion_id = Column(Integer, ForeignKey('occasions.id'))
    bought = Column('bought', Boolean, default=False)

    gift = relationship("Gift")
    occasion = relationship("Occasion")
    person = relationship("Person", back_populates="selected_gift")

    def __init__(self, price, gift, occasion, person):
        self.price = price
        self.gift = gift
        self.occasion = occasion
        self.person = person


class Occasion(Base):
    __tablename__ = 'occasions'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(60))
    day = Column('day', Integer)
    month = Column('month', Integer)

    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month


Base.metadata.create_all(engine)
