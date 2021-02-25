from models import Occasion
from models import PeopleGroup
from models import GiftCategory
from models import Gift
from base import session


# create Occasion

christmas = Occasion('Christmas', 24, 12)
grandmother_day = Occasion("Grandmother's day", 21, 1)
grandfather_day = Occasion("Grandfather's day", 22, 1)
valentines_day = Occasion("Valentine's day", 14, 2)
women_day = Occasion("Women's Day", 8, 3)
childrens_day = Occasion("Children's day", 1, 6)
teacher_day = Occasion("Teacher Day", 14, 10)
saint_nicholas_day = Occasion("Saint Nicholas' Day", 6, 12)
mens_day = Occasion("Men's day", 10, 3)

# create people group

friends = PeopleGroup("Friends",)
family = PeopleGroup("Family",)
coworkers = PeopleGroup("Coworkers",)
others_group = PeopleGroup("Others",)

# create gift category
sweets = GiftCategory("Sweets")
toys_and_games = GiftCategory("Toys and games")
electronic_devices = GiftCategory("Electronic devices")
cosmetics = GiftCategory("Cosmetics")
gadgets = GiftCategory("Gadgets")
diy = GiftCategory("DIY")
others_cat = GiftCategory("Others")

# create gifts
mug = Gift("Mug with personalized inscription", 20, 40, gadgets)
bungee_jump = Gift("Bungee jump", 150, 300, others_cat)
chocolate = Gift("Chocolate", 2, 10, sweets)
chocolate_box = Gift("Chocolate box", 10, 30, sweets)


session.add(christmas)
session.add(saint_nicholas_day)
session.add(childrens_day)
session.add(grandfather_day)
session.add(grandmother_day)
session.add(mens_day)
session.add(teacher_day)
session.add(valentines_day)
session.add(women_day)

session.add(family)
session.add(friends)
session.add(coworkers)
session.add(others_group)

session.add(sweets)
session.add(toys_and_games)
session.add(electronic_devices)
session.add(cosmetics)
session.add(gadgets)
session.add(diy)
session.add(others_cat)
session.add(mug)
session.add(bungee_jump)
session.add(chocolate)
session.add(chocolate_box)

session.commit()
session.close()
