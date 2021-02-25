from models import User
from base import session


def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


def user_exists(username, password):
    user = session.query(User).filter(User.username == username, User.password == password).first()
    return user.id


def check_user(username, password):
    user = session.query(User).filter(User.username == username, User.password == password).first()
    if user:
        return True
    else:
        return False


def check_password(password, password2):
    if password == password2:
        return True
    else:
        return False


def check_data_to_create_account(password, password2, budget, username):

    if check_user(username, password):
        return "this username is already in use"
    if password != password2:
        return "password and verify password must be the same"
    if not is_float(budget):
        return "budget must be numeric"

    return "correct"


def get_money_for_gifts (user_id):
    user = session.query(User).filter(User.id == user_id).first()
    money_for_gifts = user.money_for_gifts
    return money_for_gifts


def get_remaining_money(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    remaining_money = user.remaining_money
    return remaining_money


def get_username(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    username = user.username
    return username


def create_user(username, password, budget):
    user = User(username, budget, budget, password)
    session.add(user)
    session.commit()


def change_budget(user_id, new_budget, spent_money):
    user = session.query(User).filter(User.id == user_id).first()
    user.money_for_gifts = new_budget
    user.remaining_money = new_budget - spent_money
    session.commit()





