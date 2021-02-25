from models import PeopleGroup
from base import session

def get_people_groups():
    people_groups = session.query(PeopleGroup).all()
    return people_groups

