import curses
from math import *


def show_person(person, i):
    name = decode(person.name)
    surname = decode(person.surname)

    person_data_to_show = str(i) + '-' + name + '-' + surname

    return person_data_to_show

def gift_stat(stdscr):
    h, w = stdscr.getmaxyx()
    y = h-12
    x = w//8 - 3

    part1 ="                __   __              "
    part2 ="              ((__\o/__))            "
    part3 =".----------------//^\\---------------."
    part4 ="|               //   \\              |"
    part5 ="|                                   |"
    part6 ="|                                   |"
    part7 ="|                                   |"
    part8 ="|                                   |"
    part9 ="|                                   |"
    part10="|                                   |"
    part11="|                                   |"
    part12="'--------------=======--------------'"

    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(4))

    stdscr.addstr(y, x, part1)
    stdscr.addstr(y + 1, x, part2)
    stdscr.addstr(y+2, x, part3)
    stdscr.addstr(y+3, x, part4)
    stdscr.addstr(y+4, x, part5)
    stdscr.addstr(y+5, x, part6)
    stdscr.addstr(y+6, x, part7)
    stdscr.addstr(y+7, x, part8)
    stdscr.addstr(y+8, x, part9)
    stdscr.addstr(y+9, x, part10)
    stdscr.addstr(y+10, x, part12)
    stdscr.attroff(curses.color_pair(4))


def logo(stdscr):
    h, w = stdscr.getmaxyx()
    y = 2
    x = w//2 - 20
    logo_part_1 = " _____ _  __ _     _          _"
    logo_part_2 = "|  __ (_)/ _| |   | |        | |                "
    logo_part_3 = "| | __| |  _| __| | '_ \ / _ \ | '_ \ / _ \ '__|"
    logo_part_4 = "| |_\ \ | | | |_  | | | |  __/ | |_) |  __/ |   "
    logo_part_5 = " \____/_|_|  \__| |_| |_|\___|_| .__/ \___|_|  "
    logo_part_6 = "                               | |              "
    logo_part_7 = "                               |_|               "
    stdscr.addstr(y+1, x, logo_part_1, curses.COLOR_RED)
    stdscr.addstr(y+2, x, logo_part_2, curses.COLOR_RED)
    stdscr.addstr(y+3, x, logo_part_3, curses.COLOR_RED)
    stdscr.addstr(y+4, x, logo_part_4, curses.COLOR_RED)
    stdscr.addstr(y+5, x, logo_part_5, curses.COLOR_RED)
    stdscr.addstr(y+6, x, logo_part_6, curses.COLOR_RED)
    stdscr.addstr(y+7, x, logo_part_7, curses.COLOR_RED )

def gift(stdscr):
    part1= "8CGGGGG0008                     880GCLLffLLCG"
    part2= "0i;i1fCLLfffttL0       8     0L1i1i111ttfftiiii0"
    part3= "0f111L0    8GfttffCLt111fGGf1tC088       iii10"
    part4= "80CftffLCG0G00tiiiiiiii1CCCCLftftttffffLC0"
    part5= "0GGGG0GCffttt11tft11111111i;;;;i1ttLLCCGGGGGGG8"
    part6= "C                  .;iiiii:                    .8"
    part7= " f   fCCCCCCCCCCCCCCCCG0G0GCCCCCCCCCCCCCCCCCC;   0"
    part8= "║  .                                            ░   0"
    part9= "║  .█                                           ░   0"
    part10= "║  .█                                           ░   0"
    part11= "║  .█                                           ░   0"
    part12="║  .█                                           ░   0"
    part13="║  .█                                           ░   0"
    part14="║  .█                                           ░   0"
    part20="║  .█                                           ░   0"
    part21= "║  .█                                           ░   0"
    part22= "║  .█                                           ░   0"
    part23= "║  .█                                           ░   0"
    part24="║  .█                                           ░   0"
    part25="║  .                                            ░   0"
    part26="█   t████████████████████████████████████████░   █"
    part27="█                                              .█"
    part28="███████████████████████████████████████████████"
    h, w = stdscr.getmaxyx()
    y = 2
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(4))

    x = w // 2 - len(part1) // 2
    stdscr.addstr(y+1, x, part1)
    x = w // 2 - len(part2) // 2
    stdscr.addstr(y+2, x, part2)
    x = w // 2 - len(part3) // 2
    stdscr.addstr(y+3, x, part3)
    x = w // 2 - len(part4) // 2
    stdscr.addstr(y+4, x, part4)
    x = w // 2 - len(part5) // 2
    stdscr.addstr(y+5, x, part5)
    x = w // 2 - len(part6) // 2
    stdscr.addstr(y+6, x, part6)
    x = w // 2 - len(part7) // 2
    stdscr.addstr(y+7, x, part7)
    x = w // 2 - len(part8) // 2
    stdscr.addstr(y+8, x, part8)
    x = w // 2 - len(part9) // 2
    stdscr.addstr(y+9, x, part9)
    stdscr.addstr(y+10, x, part10)
    stdscr.addstr(y+11, x, part11)
    stdscr.addstr(y+12, x, part12)
    stdscr.addstr(y+13, x, part13)
    stdscr.addstr(y+14, x, part14)
    stdscr.addstr(y+15, x, part20)
    stdscr.addstr(y+16, x, part21)
    stdscr.addstr(y+17, x, part22)
    stdscr.addstr(y+18, x, part23)
    stdscr.addstr(y+19, x, part24)
    stdscr.addstr(y+20, x, part25)
    stdscr.addstr(y+21, x, part26)
    x = w // 2 - len(part27) // 2
    stdscr.addstr(y+22, x, part27)
    x = w // 2 - len(part28) // 2
    stdscr.addstr(y+23, x, part28)
    stdscr.attroff(curses.color_pair(4))


def show_gift(gift, i):
    name = gift.name
    if isinstance(name, bytes):
        name = name.decode()
    price_min = str(round(gift.price_min, 2))
    price_max = str(round(gift.price_max, 2))

    gift_data_to_show = str(i) + ' - ' + name + ' - ' + 'price: ' + price_min + '-' + price_max
    return gift_data_to_show


def show_selected_gift(selected_gift, i):
    gift_name = selected_gift.gift.name
    if isinstance(gift_name, bytes):
        gift_name = gift_name.decode()

    person_name = selected_gift.person.name
    if isinstance(person_name, bytes):
        person_name = person_name.decode()

    person_surname = selected_gift.person.surname
    if isinstance(person_surname, bytes):
        person_surname = person_surname.decode()
    selected_gift_to_show = str(i) + ' - ' + gift_name + ' for ' + person_name + ' ' + person_surname

    return selected_gift_to_show


def print_menu(stdscr, selected_row_idx, idx_color, menu, title):
    stdscr.clear()
    gift(stdscr)
    h, w = stdscr.getmaxyx()
    y = h//2 - len(menu)//2 - 3
    x = w//2 - len(title)//2
    stdscr.addstr(y, x, title, curses.A_BOLD)
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(idx_color))
            stdscr.addstr(y, x, row)

            stdscr.attroff(curses.color_pair(idx_color))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def dont_show_input(stdscr, prompt_string, amount, idx):
    curses.echo()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(prompt_string) // 2
    y = h // 2 - amount // 2 + idx+1
    stdscr.addstr(y, x, prompt_string, curses.A_BOLD)
    stdscr.refresh()
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(6))
    input_to_show = stdscr.getstr(y, x+len(prompt_string)+1, 30, )
    stdscr.attroff(curses.color_pair(6))
    return input_to_show


def show_input(stdscr, prompt_string, amount, idx):
    curses.echo()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(prompt_string) // 2
    y = h // 2 - amount // 2 + idx+1
    stdscr.addstr(y, x, prompt_string, curses.A_BOLD)
    stdscr.refresh()
    input_to_show = stdscr.getstr(y, x+len(prompt_string)+1, 30)
    return input_to_show


def decode(byte_string):
    return byte_string.decode("utf-8")


def choose_object_from_the_list(stdscr, objects, object_type):
    stdscr.clear()
    row_num = len(objects)
    max_row = 10
    h, w = stdscr.getmaxyx()
    x = w // 2 - 64 // 2
    y = h // 2 - (max_row + 2) // 2
    if object_type == "selected_gift":
        instruction = "Press ENTER to mark gift as 'bought', press C to Cancel"
    elif object_type == "bought_gift":
        instruction = "Press ENTER or 'C' to Cancel"
    else:
        instruction = "Press ENTER to choose, press C to Cancel"
    instruction_x = w//2 - len(instruction) // 2
    stdscr.addstr(y-2, instruction_x, instruction )
    box = curses.newwin(max_row + 2, 64, y, x)
    box.box()
    highlight_text = curses.color_pair(1)
    normal_text = curses.A_NORMAL

    pages = int(ceil(row_num / max_row))
    position = 1
    page = 1
    for i in range(1, max_row + 1):
        if row_num == 0:
            box.addstr(1, 1, "This list is empty", highlight_text)
        else:
            if i == position:
                if object_type == 'person':
                    str = show_person(objects.__getitem__(i-1), i)
                elif object_type == 'selected_gift' or object_type == 'bought_gift':
                    str = show_selected_gift(objects.__getitem__(i-1), i)
                else:
                    str = show_gift(objects.__getitem__(i-1), i)
                box.addstr(i, 2, str, highlight_text)
            else:
                if object_type == 'person':
                    str = show_person(objects.__getitem__(i-1), i)
                elif object_type == 'selected_gift' or object_type == 'bought_gift':
                    str = show_selected_gift(objects.__getitem__(i-1), i)
                else:
                    str = show_gift(objects.__getitem__(i-1), i)
                box.addstr(i, 2, str, normal_text)
            if i == row_num:
                break

    stdscr.refresh()
    box.refresh()

    x = stdscr.getch()
    i = 0
    while x != 27:
        if x == curses.KEY_DOWN:
            if page == 1:
                if position < i:
                    position = position + 1
                else:
                    if pages > 1:
                        page = page + 1
                        position = 1 + (max_row * (page - 1))
            elif page == pages:
                if position < row_num:
                    position = position + 1
            else:
                if position < max_row + (max_row * (page - 1)):
                    position = position + 1
                else:
                    page = page + 1
                    position = 1 + (max_row * (page - 1))
        if x == curses.KEY_UP:
            if page == 1:
                if position > 1:
                    position = position - 1
            else:
                if position > (1 + (max_row * (page - 1))):
                    position = position - 1
                else:
                    page = page - 1
                    position = max_row + (max_row * (page - 1))
        if x == ord("\n") and row_num != 0:
            stdscr.erase()
            stdscr.border(0)
            return objects.__getitem__(i-1)

        if x == ord("c"):
            break
        box.erase()
        box.border(0)

        for i in range(1 + (max_row * (page - 1)), max_row + 1 + (max_row * (page - 1))):
            if row_num == 0:
                box.addstr(1, 1, "This list is empty", highlight_text)
            else:
                if i + (max_row * (page - 1)) == position + (max_row * (page - 1)):
                    if object_type == 'person':
                        str = show_person(objects.__getitem__(i - 1), i)
                    elif object_type == 'selected_gift' or object_type == 'bought_gift':
                        str = show_selected_gift(objects.__getitem__(i - 1), i)
                    else:
                        str = show_gift(objects.__getitem__(i - 1), i)
                    box.addstr(i - (max_row * (page - 1)), 2, str, highlight_text)
                else:
                    if object_type == 'person':
                        str = show_person(objects.__getitem__(i - 1), i)
                    elif object_type == 'selected_gift' or object_type == 'bought_gift':
                        str = show_selected_gift(objects.__getitem__(i - 1), i)
                    else:
                        str = show_gift(objects.__getitem__(i - 1), i)
                    box.addstr(i - (max_row * (page - 1)), 2, str, normal_text)
                if i == row_num:
                    break

        stdscr.refresh()
        box.refresh()
        x = stdscr.getch()


def show_element_to_choose_with_instruction (stdscr, instruction, x, y, element):
    stdscr.addstr(y, x, instruction, curses.A_BOLD)
    element_to_show = '<-' + str(element) + '->'
    param_x_for_el = x + len(instruction) + 2
    stdscr.addstr(y, param_x_for_el, element_to_show)
    stdscr.clrtoeol()
    stdscr.refresh()


def choose_option(stdscr, list, prompt_string, amount, idx, type):
    curses.echo()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(prompt_string) // 2
    y = h // 2 - amount // 2 + idx+1

    current_id = 0
    to_show = ''
    current_element = list.__getitem__(current_id)
    if type == 'list':
        to_show = current_element.name
    elif type == 'tab':
        to_show = current_element
    show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, to_show)
    stdscr.refresh()

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_LEFT and current_id > 0:

            current_id -= 1
            current_element = list.__getitem__(current_id)
            if type == 'list':
                to_show = current_element.name
            elif type == 'tab':
                to_show = current_element
            show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, to_show)
            stdscr.refresh()
        elif key == curses.KEY_RIGHT and current_id < len(list) - 1:

            current_id += 1
            current_element = list.__getitem__(current_id)
            if type == 'list':
                to_show = current_element.name
            elif type == 'tab':
                to_show = current_element
            show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, to_show)
            stdscr.refresh()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if type == 'tab':
                return current_id+1
            return current_element


def choose_number(stdscr, minimum, maximum, prompt_string, amount, idx):
    curses.echo()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(prompt_string) // 2
    y = h // 2 - amount // 2 + idx+1

    current_number = minimum

    show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, current_number)
    stdscr.refresh()

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_LEFT and current_number > minimum:

            current_number -= 1
            show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, current_number)
            stdscr.refresh()
        elif key == curses.KEY_RIGHT and current_number < maximum:

            current_number += 1
            show_element_to_choose_with_instruction(stdscr, prompt_string, x, y, current_number)
            stdscr.refresh()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_number