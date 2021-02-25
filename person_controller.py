from models import Person, User
from base import session


def add_person(name, surname, day, month, group, user):
    user = session.query(User).filter(User.id == user).first()
    person = Person(name, surname, day, month, group, user)
    session.add(person)
    session.commit()


def get_people_from_chosen_group(group, user):
    people = session.query(Person).filter(Person.group == group,
                                          Person.user.has(User.id == user)).all()
    return people


def get_all_people(user):
    people = session.query(Person).filter(Person.user.has(User.id == user)).all()
    return people



def get_person(pk):
    person = session.query(Person).filter(Person.id == pk).first()
    return person


