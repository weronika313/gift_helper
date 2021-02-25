import tkinter as tk
from tkinter import ttk
from user_controller import check_data_to_create_account, create_user, check_user, user_exists, \
    change_budget, get_remaining_money, get_money_for_gifts
from people_group_controller import get_people_groups
from person_controller import add_person
from gift_category_controller import get_gift_categories
from gift_idea_controller import create_gift_idea, get_gift_ideas_for_selected_occasion_and_price_range, \
    get_gift_ideas_for_selected_occasion, get_all_gift_ideas
from gift_controller import add_gift, get_all_gifts_from_chosen_category, get_all_gifts, get_gift
from person_controller import get_people_from_chosen_group, get_all_people, get_person
from occasion_controller import get_occasions
import random
from selected_gift_contoller import add_selected_gift, get_selected_gifts, \
    mark_gift_as_bought, get_selected_gift, get_bought_gifts
from PIL import ImageTk, Image
import os
import curses
from views import start_app
import wx

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
NAME = "cos_tam"
PASSWORD = "cos"
MONTHS = (' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September',
          ' October', ' November', ' December')
MOTHS_DAY = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
root = None
login_window



def start_with_login():
    global root
    global login_window

    root = GiftHelper()
    root.geometry("1280x720")
    login_window = GiftHelperLogin(root)
    root.mainloop()


def change_name_and_pass(new_name, new_pass):
    global NAME
    global PASSWORD
    NAME = new_name
    PASSWORD = new_pass


def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry("250x100")
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def change_to_text_view_from_login_view():
    login_window.destroy()
    root.destroy()
    curses.wrapper(start_app)


class GiftHelperLogin(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        container = tk.Frame(self)
        self.geometry("400x350")

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, LoginPage, CreateAccountPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="plum4")
        label = tk.Label(self, text="GIFT HELPER", bg="plum4", fg="white", width="300", height="2",
                         font=("Comic Sans MS,", 30, 'bold'))
        label.pack(pady=10, padx=10)

        style = ttk.Style()
        style.configure('D.TButton', font=
        ('calibri', 23, 'bold'),
                        borderwidth='4', foreground='plum4')

        button = ttk.Button(self, text="Login", style='D.TButton',
                            command=lambda: controller.show_frame(LoginPage))
        button.pack(pady=10, ipadx=40)

        button2 = ttk.Button(self, text="Create account", style='D.TButton',
                             command=lambda: controller.show_frame(CreateAccountPage))
        button2.pack(pady=10, ipadx=30)

        button3 = ttk.Button(self, text="Change to text view", style='D.TButton',
                             command=lambda: change_to_text_view_from_login_view())
        button3.pack(pady=10)


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="plum4")
        label = tk.Label(self, text="Login", bg="plum4", fg="white", width="300", height="2",
                         font=("Calibri", 25, 'bold'))
        label.pack(pady=10, padx=10)

        self.enter_frame = tk.Frame(self, bg="plum4", width=200, height=200, pady=3)
        self.enter_frame.pack()

        username_label = tk.Label(self.enter_frame, text="Username: * ", bg="plum4",
                                  fg="plum3", font=("Calibri", 15, 'bold'))
        self.username = tk.StringVar()
        username_entry = tk.Entry(self.enter_frame, textvariable=self.username, fg='plum4')
        username_label.grid(column=0, row=0)
        username_entry.grid(column=1, row=0)

        password_label = tk.Label(self.enter_frame, text="Password: * ", bg="plum4",
                                  fg="thistle3", font=("Calibri", 15, 'bold'))
        self.password = tk.StringVar()
        password_entry = tk.Entry(self.enter_frame, textvariable=self.password, show="*", fg='plum4')
        password_entry.grid(column=1, row=1)
        password_label.grid(column=0, row=1)

        self.button_frame = tk.Frame(self, bg="plum4", width=100, height=100, pady=3)
        self.button_frame.pack()

        style = ttk.Style()
        style.configure('TButton', font=
        ('calibri', 23, 'bold'),
                        borderwidth='5', foreground='plum4')

        confirm_button = ttk.Button(self.button_frame, text="Login", style='D.TButton', command=self.login)
        confirm_button.grid(columnspan=2, padx=10, pady=3)

        button1 = tk.Button(self.button_frame, text="Back", fg='plum4',
                            font=('calibri', 10, 'bold'), width=15, height=0,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(column=0, row=1, pady=3)

        button2 = tk.Button(self.button_frame, text="Create account", fg='plum4',
                            font=('calibri', 10, 'bold'), width=15, height=0,
                            command=lambda: controller.show_frame(CreateAccountPage))
        button2.grid(column=1, row=1, pady=3)

    def login(self):
        username_to_check = self.username.get()
        password_to_check = self.password.get()
        global PASSWORD
        global NAME

        if check_user(username_to_check, password_to_check):
            change_name_and_pass(username_to_check, password_to_check)
            cancel_login()
            UserFrame.create(UserFrame)
            print(PASSWORD)
            print(NAME)


        else:
            popupmsg("Invalid password or username")


def cancel_login():  # exit function
    login_window.withdraw()
    login_window.root.deiconify()


class CreateAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="plum4")
        label = tk.Label(self, text="Create account", bg="plum4", fg="white", width="300",
                         height="2", font=("Calibri", 25, 'bold'))
        label.pack(pady=10, padx=10)

        self.enter_frame = tk.Frame(self, bg="plum4", width=200, height=200, pady=3)
        self.enter_frame.pack()

        username_label = tk.Label(self.enter_frame, text="Username: * ", bg="plum4",
                                  fg="thistle3", font=("Calibri", 15, 'bold'))
        self.username = tk.StringVar()
        username_entry = tk.Entry(self.enter_frame, textvariable=self.username, fg='plum4')
        username_entry.grid(column=1, row=0)
        username_label.grid(column=0, row=0)

        password_label = tk.Label(self.enter_frame, text="Password: * ", bg="plum4",
                                  fg="plum3", font=("Calibri", 15, 'bold'))
        self.password = tk.StringVar()
        password_entry = tk.Entry(self.enter_frame, textvariable=self.password, show="*", fg='plum4')
        password_label.grid(column=0, row=1)
        password_entry.grid(column=1, row=1)

        password_confirm_label = tk.Label(self.enter_frame, text="Password confirm: * ", bg="plum4",
                                          fg="thistle3", font=("Calibri", 15, 'bold'))
        self.password2 = tk.StringVar()
        password_confirm_entry = tk.Entry(self.enter_frame, textvariable=self.password2, show="*")
        password_confirm_label.grid(column=0, row=2)
        password_confirm_entry.grid(column=1, row=2)

        budget_label = tk.Label(self.enter_frame, text="Budget: * ", bg="plum4",
                                fg="plum3", font=("Calibri", 15, 'bold'))
        self.budget = tk.StringVar()
        budget_entry = tk.Entry(self.enter_frame, textvariable=self.budget, fg='plum4')
        budget_label.grid(column=0, row=3)
        budget_entry.grid(column=1, row=3)

        self.button_frame = tk.Frame(self, bg="plum4", width=100, height=100, pady=3)
        self.button_frame.pack()

        style = ttk.Style()
        style.configure('TButton', font=
        ('calibri', 23, 'bold'),
                        borderwidth='5', foreground='MediumOrchid4')

        confirm_button = ttk.Button(self.button_frame, text="Register", style='D.TButton',
                                    command=self.create_account)
        confirm_button.grid(columnspan=2, padx=10, pady=3)

        button1 = tk.Button(self.button_frame, text="Back", fg='plum4',
                            font=('calibri', 10, 'bold'), width=15, height=0,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(column=0, row=1, padx=3, pady=3)

        button2 = tk.Button(self.button_frame, text="Login", fg='plum4',
                            font=('calibri', 10, 'bold'), width=15, height=0,
                            command=lambda: controller.show_frame(LoginPage))
        button2.grid(column=1, row=1, padx=3, pady=3)

    def create_account(self):
        username_to_check = self.username.get()
        password_to_check = self.password.get()
        password2_to_check = self.password2.get()
        budget_to_check = self.budget.get()

        info = check_data_to_create_account(password2_to_check, password_to_check,
                                            budget_to_check, username_to_check)

        if info == 'correct':
            create_user(username_to_check, password_to_check, budget_to_check)
            popupmsg("user created")

        else:
            popupmsg(info)


class GiftHelper(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.withdraw()
        container = tk.Frame(self)
        self.frame = MainPage(self, container)
        self.frame.pack()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.top_frame = tk.Frame(self, bg='thistle3', width=1280, height=100, pady=5, padx=5)
        self.center_frame = CenterFrame(self, controller)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.top_frame.grid(row=0, sticky="ew")
        self.center_frame.grid(row=1, sticky="nsew")

        self.logo = tk.Label(self.top_frame, text="Gift Helper", bg='thistle3',
                             fg='plum4', width="100", height="2", font=("Verdana", 20, 'bold')).pack()


class CenterFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='MediumOrchid4', width=1280, height=620)
        self.menu = Menu(self)
        self.user_data = UserFrame(self, controller)
        self.data = None
        self.switch_frame(DataFrame)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu.grid(row=0, column=0, sticky="ns")
        self.user_data.grid(row=0, column=2, sticky="ns")
        style_t = ttk.Style()
        # this is set background and foreground of the treeview
        style_t.configure("Treeview",
                          background="#E1E1E1",
                          foreground="plum4",
                          rowheight=25,
                          fieldbackground="#plum4")
        style_t.configure("Treeview.Heading", foreground='thistle4', background='plum4', font=("bold"))

        # set backgound and foreground color when selected
        style_t.map('Treeview', background=[('selected', 'plum4')], foreground=[('selected', 'thistle2')])

        style = ttk.Style()

        style.map('TCombobox', fieldbackground=[('readonly', 'white')])
        style.map('TCombobox', selectbackground=[('readonly', 'thistle2')])
        style.map('TCombobox', selectforeground=[('readonly', 'plum4')])

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.data is not None:
            self.data.destroy()
        self.data = new_frame
        self.data.grid(row=0, column=1, sticky='nsew')


class DataFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        img = Image.open('logo.png')
        img = img.resize((800, 450), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(self, image=img)
        panel.image = img
        panel.pack()


class UserFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='MediumOrchid4', width=200, height=620, padx=3, pady=3)

    def create(self):
        self.text = 'Welcome ' + NAME + '!'
        self.label = tk.Label(self, text="Draw", fg='plum1', bg='MediumOrchid4',
                         font=("Calibri", 15, 'bold')).pack(padx=10, pady=10)
        user = user_exists(NAME, PASSWORD)
        money_for_gifts = get_money_for_gifts(user)
        remaining_money = get_remaining_money(user)
        spent_money = money_for_gifts - remaining_money

        budget_label = tk.Label(self, text='Your Budget: ', fg='plum1', bg='MediumOrchid4',
                         font=("Calibri", 15, 'bold')).pack(padx=5, pady=4)

        budget = tk.Label(self, text=str(round(money_for_gifts, 2)), fg='plum1', bg='MediumOrchid4',
                         font=("Calibri", 15, 'bold')).pack(padx=5, pady=4)

        spent_money_label = tk.Label(self, text='Your have already spent: ', fg='plum1', bg='MediumOrchid4',
                                font=("Calibri", 15, 'bold')).pack(padx=5, pady=4)

        spent_money_text = tk.Label(self, text=str(round(spent_money, 2)), fg='plum1', bg='MediumOrchid4',
                          font=("Calibri", 15, 'bold')).pack(padx=5, pady=4)


def get_gift_categories_name_list():
    categories_list = get_gift_categories()
    categories_name = []

    for c in categories_list:
        categories_name.append(c.name)

    return categories_name


def check_category(category_name):
    categories_list = get_gift_categories()

    for n in categories_list:
        if n.name == category_name:
            return True

    return False


def get_category(category_name):
    categories_list = get_gift_categories()

    for n in categories_list:
        if n.name == category_name:
            category = n
            return category


def get_occasions_name_list():
    occasions_list = get_occasions()
    occasions_name = []

    for o in occasions_list:
        occasions_name.append(o.name)

    return occasions_name


def check_occasion(occasion_name):
    occasions_list = get_occasions()

    for o in occasions_list:
        if o.name == occasion_name:
            return True

    return False


def get_occasion_by_name(occasion_name):
    occasions_list = get_occasions()

    for o in occasions_list:
        if o.name == occasion_name:
            occasion = o
            return occasion


class AdGiftIdeaFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        label = tk.Label(self, text="Add gift idea", fg='plum4', width="100", height="2",
                         font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=20)

        gift_name_label = tk.Label(entry_frame, text="Gift name: ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.name = tk.StringVar()
        name_entry = tk.Entry(entry_frame, textvariable=self.name, fg='plum4', width=23)
        gift_name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)

        categories_label = tk.Label(entry_frame, text="Select gift category: ", fg="plum3",
                                    font=("Calibri", 15, 'bold'))
        self.c = tk.StringVar()
        category_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.c)
        category_choosen['values'] = get_gift_categories_name_list()
        categories_label.grid(row=1, column=0)
        category_choosen.grid(row=1, column=1)
        category_choosen.current(0)

        price_min_label = tk.Label(entry_frame, text="Minimum price: ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.price_min = tk.StringVar()
        price_min_entry = tk.Entry(entry_frame, textvariable=self.price_min, fg='plum4', width=23)
        price_min_label.grid(row=2, column=0)
        price_min_entry.grid(row=2, column=1)

        price_max_label = tk.Label(entry_frame, text="Maximum price: ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.price_max = tk.StringVar()
        price_max_entry = tk.Entry(entry_frame, textvariable=self.price_max, width=23)
        price_max_label.grid(row=3, column=0)
        price_max_entry.grid(row=3, column=1)

        self.confirm_button = ttk.Button(self, style="D.TButton", text='add gift idea',
                                         command=lambda: self.add_gift_idea()).pack()

    def add_gift_idea(self):
        name = self.name.get()
        category = self.c.get()
        price_min = self.price_min.get()
        price_max = self.price_max.get()

        if check_category(category):
            if is_float(price_min) and is_float(price_max):
                if price_min < price_max:
                    cat = get_category(category)
                    add_gift(name, int(price_min), int(price_max), cat)
                    popupmsg("Gift idea created")

                else:
                    popupmsg("minimum price must be less than maximum")
            else:
                popupmsg("Price must be numeric")

        else:
            popupmsg("Invalid category name")


def get_people_group_name_list():
    group_list = get_people_groups()
    people_group_name = []

    for n in group_list:
        people_group_name.append(n.name)

    return people_group_name


def check_group(group_name):
    group_list = get_people_groups()

    for n in group_list:
        if n.name == group_name:
            return True

    return False


def get_group(group_name):
    group_list = get_people_groups()

    for n in group_list:
        if n.name == group_name:
            group = n
            return group


class AddPersonFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        label = tk.Label(self, text="Add person", fg='plum4', width="100", height="2",
                         font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=20)

        person_name_label = tk.Label(entry_frame, text="Person name ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.name = tk.StringVar()
        name_entry = tk.Entry(entry_frame, textvariable=self.name, fg='plum4', width=23)
        person_name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)

        person_surname_label = tk.Label(entry_frame, text="Person surname * ", fg="plum3",
                                        font=("Calibri", 15, 'bold'))
        self.surname = tk.StringVar()
        surname_entry = tk.Entry(entry_frame, textvariable=self.surname, fg='plum4', width=23)
        person_surname_label.grid(row=1, column=0)
        surname_entry.grid(row=1, column=1)

        group_label = tk.Label(entry_frame, text="Select the people group: *", fg="plum3",
                               font=("Calibri", 15, 'bold'))
        self.g = tk.StringVar()
        group_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.g)
        group_choosen['values'] = get_people_group_name_list()
        group_label.grid(row=2, column=0)
        group_choosen.grid(row=2, column=1)
        group_choosen.current(0)

        day_label = tk.Label(entry_frame, text="Select the day: *", fg="plum3",
                             font=("Calibri", 15, 'bold'))
        self.d = tk.IntVar()
        day_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.d)
        day_choosen['values'] = list(range(1, 32))
        day_label.grid(row=3, column=0)
        day_choosen.grid(row=3, column=1)
        day_choosen.current(0)

        month_label = tk.Label(entry_frame, text="Select the Month :",
                               fg="plum3",
                               font=("Calibri", 15, 'bold')
                               )

        self.n = tk.StringVar()
        monthchoosen = ttk.Combobox(entry_frame,
                                    textvariable=self.n)
        monthchoosen['values'] = MONTHS
        month_label.grid(row=4, column=0)
        monthchoosen.grid(row=4, column=1)
        monthchoosen.current(0)

        self.confirm_button = ttk.Button(self, style="D.TButton", text='Add person',
                                         command=lambda: self.add_person()).pack()

    def add_person(self):
        name_to_check = self.name.get()
        surname_to_check = self.surname.get()
        group = self.g.get()
        month = self.n.get()
        day = self.d.get()

        if check_group(group):
            if month in MONTHS:
                month_index = MONTHS.index(month)
                month_days = MOTHS_DAY[month_index]

                if month_days > day:
                    add_person(name_to_check, surname_to_check, day, month_index, get_group(group),
                               user_exists(NAME, PASSWORD))
                    popupmsg("Person has been added")


                else:
                    popupmsg("This month have less days")


            else:
                popupmsg("Invalid month name")

        else:
            popupmsg("Invalid group name")


def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


class ChangeBudgetFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=400, height=620, padx=3, pady=3)
        label = tk.Label(self, text="Change budget", fg='plum4', width="100", height="2",
                         font=("Calibri", 20, 'bold'))
        label.pack()
        self.user = user_exists(NAME, PASSWORD)
        enter_frame = tk.Frame(self)
        enter_frame.pack(pady=20)

        budget_label = tk.Label(enter_frame, text="New Budget: ",
                                fg="plum3", font=("Calibri", 15, 'bold'))
        budget_label.grid(row=0, column=0)
        self.budget = tk.StringVar()
        budget_entry = tk.Entry(enter_frame, textvariable=self.budget)
        budget_entry.grid(row=0, column=1)

        self.confirm_button = ttk.Button(self, style="D.TButton", text='Confirm',
                                         command=lambda: self.change_user_budget()).pack()

    def change_user_budget(self):
        budget_to_check = self.budget.get()
        if not is_float(budget_to_check):
            popupmsg("budget must be numeric")
        else:
            money_for_gifts = get_money_for_gifts(self.user)
            remaining_money = get_remaining_money(self.user)
            spent_money = money_for_gifts - remaining_money
            spent_money = round(spent_money, 2)
            change_budget(self.user, int(budget_to_check), spent_money)
            popupmsg("You have successfully changed budget")


def get_selected_gifts_string(user):
    selected_gifts_list = get_selected_gifts(user)
    selected_gifts_string_list = []

    for selected_gift in selected_gifts_list:

        try:
            selected_gift.gift.name = selected_gift.gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        try:
            selected_gift.person.name = selected_gift.person.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        try:
            selected_gift.person.surname = selected_gift.person.surname.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        gift_name = list(selected_gift.gift.name)
        gift_name_with_backspace = ''
        for letter in gift_name:
            if letter == ' ':
                gift_name_with_backspace += '\ '
            else:
                gift_name_with_backspace += letter
        selected_gift_string = str(selected_gift.id) + ' ' + gift_name_with_backspace + ' ' + \
                               selected_gift.person.name + ' ' + selected_gift.person.surname

        selected_gifts_string_list.append(selected_gift_string)

    return selected_gifts_string_list


def get_bought_gifts_string(user):
    selected_gifts_list = get_bought_gifts(user)
    selected_gifts_string_list = []

    for selected_gift in selected_gifts_list:

        try:
            selected_gift.gift.name = selected_gift.gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        try:
            selected_gift.person.name = selected_gift.person.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        try:
            selected_gift.person.surname = selected_gift.person.surname.decode()
        except (UnicodeDecodeError, AttributeError):
            pass

        gift_name = list(selected_gift.gift.name)
        gift_name_with_backspace = ''
        for letter in gift_name:
            if letter == ' ':
                gift_name_with_backspace += '\ '
            else:
                gift_name_with_backspace += letter
        selected_gift_string = str(selected_gift.id) + ' ' + gift_name_with_backspace + ' ' + \
                               selected_gift.person.name + ' ' + selected_gift.person.surname

        selected_gifts_string_list.append(selected_gift_string)

    return selected_gifts_string_list


class ShowBoughtGiftsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        self.frame = tk.Frame(self)
        self.frame.config(width=800, height=600, padx=3, pady=3)

        self.frame.pack()

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Bought gifts:",
                         fg='plum4', width="100", height="2", font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)

        self.user = user_exists(NAME, PASSWORD)
        self.values = get_bought_gifts(self.user)
        style_t = ttk.Style()
        # this is set background and foreground of the treeview
        style_t.configure("Treeview",
                          background="#E1E1E1",
                          foreground="plum4",
                          rowheight=25,
                          fieldbackground="#plum4")
        style_t.configure("Treeview.Heading", foreground='thistle4', background='plum4', font=("bold"))

        # set backgound and foreground color when selected
        style_t.map('Treeview', background=[('selected', 'plum4')], foreground=[('selected', 'thistle2')])

        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "gift_name", "person_name", "person_surname"]

        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")

        self.treeview.column('id', width=50, stretch=tk.NO)
        self.treeview.column('gift_name', width=200, stretch=tk.NO)
        self.treeview.column('person_name', width=200, stretch=tk.NO)
        self.treeview.column('person_surname', width=200, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('gift_name', text="GIFT NAME")
        self.treeview.heading('person_name', text="PERSON NAME")
        self.treeview.heading('person_surname', text="PERSON SURNAME")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        selected_gifts_list = get_bought_gifts_string(self.user)
        for element in selected_gifts_list:
            self.treeview.insert("", "end", values=(element))


class ShowGiftToBuyFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        self.user = user_exists(NAME, PASSWORD)
        self.frame = tk.Frame(self)
        self.frame.config(width=800, height=300, padx=3, pady=3)
        self.down_frame = tk.Frame(self, width=800, height=300)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.down_frame.grid(row=1, column=0, sticky="nsew")

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Selected gifts that you need to buy",
                         fg='plum4', width="100", height="2", font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)

        self.values = get_selected_gifts(self.user)

        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "gift_name", "person_name", "person_surname"]
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")
        self.treeview.column('id', width=50, stretch=tk.NO)
        self.treeview.column('gift_name', width=200, stretch=tk.NO)
        self.treeview.column('person_name', width=200, stretch=tk.NO)
        self.treeview.column('person_surname', width=200, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('gift_name', text="GIFT NAME")
        self.treeview.heading('person_name', text="PERSON NAME")
        self.treeview.heading('person_surname', text="PERSON SURNAME")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        self.selected_gift = ""
        self.treeview.bind('<ButtonRelease-1>', self.selectItem)
        self.update()

        self.confirm_button = ttk.Button(self.down_frame, style="D.TButton", text="Mark gift as bought",
                                         command=lambda: self.mark_gift())

        self.confirm_button.pack()

    def selectItem(self, event):
        curItem = self.treeview.focus()
        self.selected_gift = self.treeview.item(curItem)['values'][0]

    def mark_gift(self):
        selected_gift_pk = int(self.selected_gift)
        selected_gift = get_selected_gift(selected_gift_pk)
        mark_gift_as_bought(selected_gift, self.user)
        self.update()
        popupmsg("Gift marked as bought")

    def update(self):
        items = self.treeview.get_children()
        for item in items:
            self.treeview.delete(item)  # Clear the treeview

        selected_gifts_list = get_selected_gifts_string(self.user)
        for element in selected_gifts_list:
            self.treeview.insert("", "end", values=(element))


def get_people_from_group_string(group, user):
    people_list = get_people_from_chosen_group(group, user)
    people_string_list = []

    for person in people_list:
        person_string = str(person.id) + ' ' + person.name + ' ' + person.surname
        people_string_list.append(person_string)

    return people_string_list


def get_people_string(user):
    people_list = get_all_people(user)
    people_string_list = []

    for person in people_list:
        person_string = str(person.id) + ' ' + person.name + ' ' + person.surname
        people_string_list.append(person_string)

    return people_string_list


class AddNewSelectedGift(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg='white', width=400, height=620, padx=3, pady=3)
        self.label = tk.Label(self, text="Draw a gift from the list of all gifts", fg='plum3', bg='white',
                              font=("Calibri", 15, 'bold')).pack(padx=10, pady=10)

        entry_frame = tk.Frame(self, bg='white')
        entry_frame.pack(pady=20)

        gift_name_label = tk.Label(entry_frame, text="Gift name: ", bg='white',
                                   fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=0, column=0)
        self.name = tk.StringVar()
        name_entry = tk.Entry(entry_frame, textvariable=self.name, width=23, fg='plum4')
        name_entry.grid(row=0, column=1)

        categories_label = tk.Label(entry_frame, text="Select gift category: ", bg='white',
                                    fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=1, column=0)
        self.c = tk.StringVar()
        category_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.c, state="readonly")
        category_choosen['values'] = get_gift_categories_name_list()
        category_choosen.grid(row=1, column=1)
        category_choosen.current(0)

        occasion_label = tk.Label(entry_frame, text="Select occasion: ", bg='white',
                                  fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=2, column=0)
        self.o = tk.StringVar()
        occasion_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.o, state="readonly")
        occasion_choosen['values'] = get_occasions_name_list()
        occasion_choosen.grid(row=2, column=1)
        occasion_choosen.current(0)

        price_label = tk.Label(entry_frame, text="Minimum price: ", bg='white',
                               fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=3, column=0)
        self.price = tk.StringVar()
        price_entry = tk.Entry(entry_frame, textvariable=self.price, width=23, fg='plum4')
        price_entry.grid(row=3, column=1)

        self.confirm_button = ttk.Button(self, style="D.TButton", text='Add new selected gift',
                                         command=lambda: self.add_new_selected_gift(parent)).pack()

    def add_new_selected_gift(self, parent):
        name = self.name.get()
        category = self.c.get()
        occasion = self.o.get()
        price = self.price.get()
        per = parent.person
        person = get_person(int(per))

        if check_category(category):
            if is_float(price):
                cat = get_category(category)
                oca = get_occasion_by_name(occasion)
                gift = add_gift(name, int(price), int(price), cat)
                add_selected_gift(gift, person, oca.id, int(price))
                popupmsg("Gift added to person")
            else:
                popupmsg("Price must be numeric")

        else:
            popupmsg("Invalid category name")


class AddGiftIdeaToPersonFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        self.main_frame = tk.Frame(self, width=800, height=620)
        self.main_frame.pack()
        self.frame = tk.Frame(self.main_frame)
        self.frame.config(width=400, height=620, padx=3, pady=3)
        self.right_frame = tk.Frame(self.main_frame, width=400, height=620)
        self.right_frame.grid(column=1, row=0)
        self.frame.grid(column=0, row=0)

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Choose person", fg='plum4',
                         font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)
        self.options = ["All", "Family", "Friends", "Others"]
        self.user = user_exists(NAME, PASSWORD)
        self.values = get_all_people(self.user)

        self.last_filter_mode = ""  # Combobox change detector
        self.filter_mode = tk.StringVar()
        self.filter_mode.set("All")
        self.combobox = ttk.Combobox(
            self.frame, textvariable=self.filter_mode, state="readonly",
            values=self.options)
        self.combobox.pack(fill="y", pady=5)
        # So that the scroll bar can be packed nicely
        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "name", "surname"]  # These are just examples
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")
        self.treeview.column('id', width=25, stretch=tk.NO)
        self.treeview.column('name', width=150, stretch=tk.NO)
        self.treeview.column('surname', width=150, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('name', text="NAME")
        self.treeview.heading('surname', text="SURNAME")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        self.person = ""
        self.treeview.bind('<ButtonRelease-1>', self.selectItem)
        self.update()

        label = tk.Label(self.right_frame, text="Add gift idea", fg='plum4',
                         font=("Calibri", 20, 'bold'))
        label.pack(pady=10, padx=10)
        entry_frame = tk.Frame(self.right_frame)
        entry_frame.pack(pady=50)

        gift_name_label = tk.Label(entry_frame, text="Gift name: ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.name = tk.StringVar()
        name_entry = tk.Entry(entry_frame, textvariable=self.name, fg='plum4', width=23)
        gift_name_label.grid(column=0, row=0)
        name_entry.grid(column=1, row=0)

        categories_label = tk.Label(entry_frame, text="Select gift category: ",
                                    fg="plum3", font=("Calibri", 15, 'bold'))
        self.c = tk.StringVar()
        category_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.c, state="readonly")
        category_choosen['values'] = get_gift_categories_name_list()
        categories_label.grid(column=0, row=1)
        category_choosen.grid(column=1, row=1)
        category_choosen.current(0)

        occasion_label = tk.Label(entry_frame, text="Select occasion: ",
                                  fg="plum3", font=("Calibri", 15, 'bold'))
        self.o = tk.StringVar()
        occasion_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.o, state="readonly")
        occasion_choosen['values'] = get_occasions_name_list()
        occasion_label.grid(column=0, row=2)
        occasion_choosen.grid(column=1, row=2)
        occasion_choosen.current(0)

        price_min_label = tk.Label(entry_frame, text="Minimum price ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.price_min = tk.StringVar()
        price_min_entry = tk.Entry(entry_frame, textvariable=self.price_min, fg='plum4', width=23)
        price_min_label.grid(column=0, row=3)
        price_min_entry.grid(column=1, row=3)

        price_max_label = tk.Label(entry_frame, text="Maximum price ", fg="plum3", font=("Calibri", 15, 'bold'))
        self.price_max = tk.StringVar()
        price_max_entry = tk.Entry(entry_frame, textvariable=self.price_max, fg='plum4', width=23)
        price_max_label.grid(column=0, row=4)
        price_max_entry.grid(column=1, row=4)

        self.confirm_button = ttk.Button(self.right_frame, style="D.TButton", text='Add gift idea to person',
                                         command=lambda: self.add_gift_to_person()).pack()

    def selectItem(self, event):
        curItem = self.treeview.focus()
        self.person = self.treeview.item(curItem)['values'][0]

    def update(self):
        filter_mode = self.filter_mode.get()

        # Check for change in the filter_mode
        if filter_mode != self.last_filter_mode:

            items = self.treeview.get_children()
            for item in items:
                self.treeview.delete(item)  # Clear the treeview

            # Combobox options
            if filter_mode == "All":
                people_list = get_people_string(self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Family":
                group = get_group("Family")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Friends":
                group = get_group("Friends")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Coworkers":
                group = get_group("Coworkers")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Others":
                group = get_group("Others")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            self.last_filter_mode = filter_mode  # Update current filter mode

        self.after(100, self.update)  # Call this function again

    def add_gift_to_person(self):
        name = self.name.get()
        category = self.c.get()
        occasion = self.o.get()
        person = self.person
        price_min = self.price_min.get()
        price_max = self.price_max.get()

        if check_category(category):
            if is_float(price_min) and is_float(price_max):
                if price_min < price_max:
                    cat = get_category(category)
                    oca = get_occasion_by_name(occasion)
                    per = get_person(int(person))
                    gift = add_gift(name, int(price_min), int(price_max), cat)
                    create_gift_idea(gift, oca, per)
                    popupmsg("Gift idea created")

                else:
                    popupmsg("minimum price must be less than maximum")
            else:
                popupmsg("Price must be numeric")

        else:
            popupmsg("Invalid category name")


class ChooseGiftMenuFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)
        self.menu_frame = tk.Frame(self)
        self.option_frame = None
        self.menu_frame.config(width=440, height=620, padx=3, pady=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.menu_frame.grid(row=0, column=1, sticky="nsew")
        self.switch_option_frame(Draw_gift_from_all_gifts_list)
        self.frame = tk.Frame(self.menu_frame)
        self.frame.config(width=400, height=200, padx=3, pady=3)
        self.frame.pack()

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Choose person", fg='plum4',
                         font=("Calibri", 15, 'bold'))
        label.pack(pady=5, padx=10)
        self.options = ["All", "Family", "Friends", "Others"]
        self.user = user_exists(NAME, PASSWORD)
        self.values = get_all_people(self.user)

        self.last_filter_mode = ""  # Combobox change detector
        self.filter_mode = tk.StringVar()
        self.filter_mode.set("All")
        self.combobox = ttk.Combobox(
            self.frame, textvariable=self.filter_mode, state="readonly",
            values=self.options)
        self.combobox.pack(fill="y", pady=3)
        # So that the scroll bar can be packed nicely
        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "name", "surname"]  # These are just examples
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")
        self.treeview.column('id', width=25, stretch=tk.NO)
        self.treeview.column('name', width=125, stretch=tk.NO)
        self.treeview.column('surname', width=125, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('name', text="NAME")
        self.treeview.heading('surname', text="SURNAME")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        self.person = ""
        self.treeview.bind('<ButtonRelease-1>', self.selectItem)
        self.update()

        label = tk.Label(self.menu_frame, text="Choose gift for person menu", fg='plum4',
                         font=("Calibri", 15, 'bold'))
        label.pack(pady=3, padx=10)

        choose_option1_button = tk.Button(self.menu_frame, text="Choose a gift from the gift ideas list",
                                          width=40, bg='plum4', fg='thistle2', font=("Calibri", 12, 'bold'),
                                          command=lambda: self.switch_option_frame(ChooseGiftFromGiftsIdeasList))
        choose_option1_button.pack()

        choose_option2_button = tk.Button(self.menu_frame, text='Draw a gift from the gift ideas list',
                                          width=40, bg='thistle3', fg='plum4', font=("Calibri", 12, 'bold'),
                                          command=lambda: self.switch_option_frame(Draw_gift_from_gift_idea_list))
        choose_option2_button.pack()

        choose_option3_button = tk.Button(self.menu_frame, text='Add new gift',
                                          width=40, bg='plum4', fg='thistle2', font=("Calibri", 12, 'bold'),
                                          command=lambda: self.switch_option_frame(AddNewSelectedGift))
        choose_option3_button.pack()

        choose_option4_button = tk.Button(self.menu_frame, text="Choose a gift from the list of all gifts",
                                          width=40, bg='thistle3', fg='plum4', font=("Calibri", 12, 'bold'),
                                          command=lambda: self.switch_option_frame(ChooseGiftFromAllGiftList))
        choose_option4_button.pack()

        choose_option5_button = tk.Button(self.menu_frame, text="Draw a gift from the list of all gifts",
                                          width=40, bg='plum4', fg='thistle2', font=("Calibri", 12, 'bold'),
                                          command=lambda: self.switch_option_frame(Draw_gift_from_all_gifts_list))
        choose_option5_button.pack()

    def switch_option_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.option_frame is not None:
            self.option_frame.destroy()
        self.option_frame = new_frame
        self.option_frame.grid(row=0, column=0, sticky='nsew')

    def selectItem(self, event):
        curItem = self.treeview.focus()
        self.person = self.treeview.item(curItem)['values'][0]

    def update(self):
        filter_mode = self.filter_mode.get()

        # Check for change in the filter_mode
        if filter_mode != self.last_filter_mode:

            items = self.treeview.get_children()
            for item in items:
                self.treeview.delete(item)  # Clear the treeview

            # Combobox options
            if filter_mode == "All":
                people_list = get_people_string(self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Family":
                group = get_group("Family")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Friends":
                group = get_group("Friends")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Coworkers":
                group = get_group("Coworkers")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Others":
                group = get_group("Others")
                people_list = get_people_from_group_string(group, self.user)
                for element in people_list:
                    self.treeview.insert("", "end", values=(element))

            self.last_filter_mode = filter_mode  # Update current filter mode

        self.after(100, self.update)  # Call this function again


def get_gifts_from_category_string(category):
    gifts_list = get_all_gifts_from_chosen_category(category)
    gift_string_list = []

    for gift in gifts_list:
        try:
            gift.name = gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass
        name = list(gift.name)
        name_with_backspace = ''
        for letter in name:
            if letter == ' ':
                name_with_backspace += '\ '
            else:
                name_with_backspace += letter

        price_min = str(round(gift.price_min, 2))
        price_max = str(round(gift.price_max, 2))
        gift_string = str(gift.id) + ' ' + name_with_backspace + ' ' + price_min + ' ' + price_max
        gift_string_list.append(gift_string)

    return gift_string_list


def get_gifts_string():
    gifts_list = get_all_gifts()
    gift_string_list = []

    for gift in gifts_list:
        try:
            gift.name = gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass
        name = list(gift.name)
        name_with_backspace = ''
        for letter in name:
            if letter == ' ':
                name_with_backspace += '\ '
            else:
                name_with_backspace += letter

        price_min = str(round(gift.price_min, 2))
        price_max = str(round(gift.price_max, 2))
        gift_string = str(gift.id) + ' ' + name_with_backspace + ' ' + price_min + ' ' + price_max
        gift_string_list.append(gift_string)

    return gift_string_list


class ChooseGiftFromAllGiftList(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg='white', width=400, height=620)
        self.frame = tk.Frame(self)
        self.frame.config(bg='white', width=400, height=300, padx=3, pady=3)
        self.down_frame = tk.Frame(self, bg='white', width=400, height=300)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.down_frame.grid(row=1, column=0, sticky="nsew")

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Choose gift", fg='plum3', bg='white',
                         font=("Calibri", 15, 'bold')).pack(padx=10, pady=10)
        self.options = ("All", "Sweets", "Toys and games", "Electronic devices",
                        "Cosmetics", "Gadgets", "DIY", "Others")
        self.values = get_all_gifts()

        self.last_filter_mode = ""  # Combobox change detector
        self.filter_mode = tk.StringVar()
        self.filter_mode.set("All")
        self.combobox = ttk.Combobox(
            self.frame, textvariable=self.filter_mode, state="readonly",
            values=self.options)
        self.combobox.pack(fill="y", pady=5)
        # So that the scroll bar can be packed nicely
        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "name", "price_min", "price_max"]  # These are just examples
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")
        self.treeview.column('id', width=25, stretch=tk.NO)
        self.treeview.column('name', width=150, stretch=tk.NO)
        self.treeview.column('price_min', width=100, stretch=tk.NO)
        self.treeview.column('price_max', width=100, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('name', text="NAME")
        self.treeview.heading('price_min', text="MINIMUM PRICE")
        self.treeview.heading('price_max', text="MAXIMUM PRICE")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        self.gift = ""
        self.treeview.bind('<ButtonRelease-1>', self.selectItem)
        self.update()

        entry_frame = tk.Frame(self.down_frame, bg='white')
        entry_frame.pack(pady=20)
        occasion_label = tk.Label(entry_frame, text="Select occasion to giving a gift: ", bg='white',
                                  fg="thistle3", font=("Calibri", 11, 'bold')).grid(column=0, row=0)
        self.o = tk.StringVar()
        occasion_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.o, state="readonly")
        occasion_choosen['values'] = get_occasions_name_list()
        occasion_choosen.grid(column=1, row=0)
        occasion_choosen.current(0)

        self.confirm_button = ttk.Button(self.down_frame, style="D.TButton", text="Choose selected gift",
                                         command=lambda: self.choose_gift(parent))

        self.confirm_button.pack(pady=10)

    def selectItem(self, event):
        curItem = self.treeview.focus()
        self.gift = self.treeview.item(curItem)['values'][0]

    def update(self):
        filter_mode = self.filter_mode.get()

        # Check for change in the filter_mode
        if filter_mode != self.last_filter_mode:

            items = self.treeview.get_children()
            for item in items:
                self.treeview.delete(item)  # Clear the treeview

            # Combobox options
            if filter_mode == "All":
                gift_list = get_gifts_string()
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Sweets":
                category = get_category("Sweets")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Toys and games":
                category = get_category("Toys and games")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Electronic devices":
                category = get_category("Electronic devices")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Cosmetics":
                category = get_category("Cosmetics")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Gadgets":
                category = get_category("Gadgets")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "DIY":
                category = get_category("DIY")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Others":
                category = get_category("Others")
                gift_list = get_gifts_from_category_string(category)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            self.last_filter_mode = filter_mode  # Update current filter mode

        self.after(100, self.update)  # Call this function again

    def choose_gift(self, parent):
        gift = get_gift(int(self.gift))
        price = (gift.price_max + gift.price_min) // 2
        per = parent.person
        oca = self.o.get()
        occasion = get_occasion_by_name(oca)
        person = get_person(int(per))
        add_selected_gift(gift, person, occasion.id, price)
        popupmsg("selected gift add")


def get_gift_ideas_from_occasion_string(occasion, person):
    gifts_list = get_gift_ideas_for_selected_occasion(occasion, person)
    gift_string_list = []

    for gift in gifts_list:
        try:
            gift.name = gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass
        name = list(gift.name)
        name_with_backspace = ''
        for letter in name:
            if letter == ' ':
                name_with_backspace += '\ '
            else:
                name_with_backspace += letter

        price_min = str(round(gift.price_min, 2))
        price_max = str(round(gift.price_max, 2))
        gift_string = str(gift.id) + ' ' + name_with_backspace + ' ' + price_min + ' ' + price_max
        gift_string_list.append(gift_string)

    return gift_string_list


def get_gift_ideas_string(person):
    gifts_list = get_all_gift_ideas(person)
    gift_string_list = []

    for gift in gifts_list:
        try:
            gift.name = gift.name.decode()
        except (UnicodeDecodeError, AttributeError):
            pass
        name = list(gift.name)
        name_with_backspace = ''
        for letter in name:
            if letter == ' ':
                name_with_backspace += '\ '
            else:
                name_with_backspace += letter

        price_min = str(round(gift.price_min, 2))
        price_max = str(round(gift.price_max, 2))
        gift_string = str(gift.id) + ' ' + name_with_backspace + ' ' + price_min + ' ' + price_max
        gift_string_list.append(gift_string)

    return gift_string_list


class ChooseGiftFromGiftsIdeasList(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=400, height=620)
        self.frame = tk.Frame(self)
        self.frame.config(bg='white', width=400, height=300, padx=3, pady=3)
        self.down_frame = tk.Frame(self, bg='white', width=400, height=300)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.down_frame.grid(row=1, column=0, sticky="nsew")

        # I like to use pack because I like the aesthetic feel
        # pady is 5 so that the widgets in the frame are spaced evenly
        label = tk.Label(self.frame, text="Choose gift", fg='plum3', bg='white',
                         font=("Calibri", 15, 'bold'))
        label.pack(pady=10, padx=10)
        self.options = ("All", 'Christmas', "Grandmother's day", "Grandfather's day",
                        "Valentine's day", "Women's Day", "Children's day", "Teacher Day",
                        "Saint Nicholas' Day", "Men's day")
        self.person = get_person(int(parent.person))
        self.values = get_all_gift_ideas(self.person)

        self.last_filter_mode = ""  # Combobox change detector
        self.filter_mode = tk.StringVar()
        self.filter_mode.set("All")
        self.combobox = ttk.Combobox(
            self.frame, textvariable=self.filter_mode, state="readonly",
            values=self.options)
        self.combobox.pack(fill="y", pady=5)
        # So that the scroll bar can be packed nicely
        self.treeview_frame = tk.Frame(self.frame)
        self.treeview_frame.pack(expand=True, fill='y')

        column_headings = ["id", "name", "price_min", "price_max"]  # These are just examples
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=column_headings, show="headings")
        self.treeview.column('id', width=25, stretch=tk.NO)
        self.treeview.column('name', width=150, stretch=tk.NO)
        self.treeview.column('price_min', width=100, stretch=tk.NO)
        self.treeview.column('price_max', width=100, stretch=tk.NO)

        self.treeview.heading('id', text="ID")
        self.treeview.heading('name', text="NAME")
        self.treeview.heading('price_min', text="MINIMUM PRICE")
        self.treeview.heading('price_max', text="MAXIMUM PRICE")

        self.treeview.pack(fill="y", side="left")

        self.treeview_scroll = ttk.Scrollbar(
            self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview_scroll.pack(fill="y", side="right")
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)
        self.gift = ""
        self.treeview.bind('<ButtonRelease-1>', self.selectItem)
        self.update()

        self.confirm_button = ttk.Button(self.down_frame, style="D.TButton", text="Choose selected gift",
                                         command=lambda: self.choose_gift(parent))

        self.confirm_button.pack()

    def selectItem(self, event):
        curItem = self.treeview.focus()
        self.gift = self.treeview.item(curItem)['values'][0]

    def update(self):
        filter_mode = self.filter_mode.get()

        # Check for change in the filter_mode
        if filter_mode != self.last_filter_mode:

            items = self.treeview.get_children()
            for item in items:
                self.treeview.delete(item)  # Clear the treeview

            # Combobox options
            if filter_mode == "All":
                gift_list = get_gift_ideas_string(self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == 'Christmas':
                occasion = get_occasion_by_name('Christmas')
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Grandmother's day":
                occasion = get_occasion_by_name("Grandmother's day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Grandfather's day":
                occasion = get_occasion_by_name("Grandfather's day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Valentine's day":
                occasion = get_occasion_by_name("Valentine's day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Women's Day":
                occasion = get_occasion_by_name("Women's Day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Children's day":
                occasion = get_occasion_by_name("Children's day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Teacher Day":
                occasion = get_occasion_by_name("Teacher Day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Saint Nicholas' Day":
                occasion = get_occasion_by_name("Saint Nicholas' Day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            if filter_mode == "Men's day":
                occasion = get_occasion_by_name("Men's day")
                gift_list = get_gift_ideas_from_occasion_string(occasion, self.person)
                for element in gift_list:
                    self.treeview.insert("", "end", values=(element))

            self.last_filter_mode = filter_mode  # Update current filter mode

        self.after(100, self.update)  # Call this function again

    def choose_gift(self, parent):
        gift = get_gift(int(self.gift))
        price = (gift.price_max + gift.price_min) // 2
        oca = self.filter_mode.get()
        occasion = get_occasion_by_name(oca)
        add_selected_gift(gift, self.person, occasion.id, price)
        popupmsg("selected gift add")


class Draw_gift_from_all_gifts_list(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.gift = None
        self.config(bg='white', width=400, height=620, padx=3, pady=3)
        self.label = tk.Label(self, text="Draw a gift from the list of all gifts", fg='plum3', bg='white',
                              font=("Calibri", 15, 'bold')).pack(padx=10, pady=10)

        entry_frame = tk.Frame(self, bg='white')
        entry_frame.pack(pady=20)
        categories_label = tk.Label(entry_frame, text="Select gift category: *", bg='white',
                                    fg="thistle3", font=("Calibri", 12, 'bold')).grid(column=0, row=0)
        self.c = tk.StringVar()
        category_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.c, state="readonly")
        category_choosen['values'] = get_gift_categories_name_list()
        category_choosen.grid(column=1, row=0)
        category_choosen.current(0)
        self.draw_result_label = tk.Label(self, text="Randomly selected gift: ", bg='white', fg="thistle4",
                                          font=("Calibri", 12, 'bold'))

        occasion_label = tk.Label(entry_frame, text="Select occasion: *", bg='white',
                                  fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=1, column=0)
        self.o = tk.StringVar()
        occasion_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.o, state="readonly")
        occasion_choosen['values'] = get_occasions_name_list()
        occasion_choosen.grid(row=1, column=1)
        occasion_choosen.current(0)

        self.draw_button = tk.Button(self, width=20, height=2, fg='thistle2', bg='plum4', text="Click to draw",
                                     font=("Calibri", 12, 'bold'),
                                     command=lambda: self.draw())
        self.draw_button.pack(ipadx=12)
        self.draw_result_label.pack(pady=10)

        self.confirm_button = ttk.Button(self, style="D.TButton", text="Choose this gift",
                                         command=lambda: self.choose_gift(parent))

        self.confirm_button.pack(ipadx=2)

    def draw(self):
        category = self.c.get()
        cat = get_category(category)
        gifts = get_all_gifts_from_chosen_category(cat)
        self.gift = random.choice(gifts)

        string = "Randomly selected gift: " + str(self.gift.name) + ', ' + 'price: ' + \
                 str(round(self.gift.price_min, 2)) + '-' + str(round(self.gift.price_max, 2))
        self.draw_result_label.configure(text=string)

    def choose_gift(self, parent):
        price = (self.gift.price_max + self.gift.price_min) // 2
        per = parent.person
        oca = self.o.get()
        occasion = get_occasion_by_name(oca)
        person = get_person(int(per))
        add_selected_gift(self.gift, person, occasion.id, price)
        popupmsg("selected gift added")


class Draw_gift_from_gift_idea_list(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.gift = None
        self.person = get_person(int(parent.person))
        self.config(bg='white', width=200, height=620, padx=3, pady=3)
        self.label = tk.Label(self, text='Draw a gift from the gift ideas list', fg='plum3', bg='white',
                              font=("Calibri", 15, 'bold')).pack(padx=10, pady=10)

        entry_frame = tk.Frame(self, bg='white')
        entry_frame.pack(pady=20)

        occasion_label = tk.Label(entry_frame, text="Select occasion: *", bg='white',
                                  fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=0, column=0)
        self.o = tk.StringVar()
        occasion_choosen = ttk.Combobox(entry_frame, width=20, textvariable=self.o, state="readonly")
        occasion_choosen['values'] = get_occasions_name_list()
        occasion_choosen.grid(row=0, column=1)
        occasion_choosen.current(0)

        price_min_label = tk.Label(entry_frame, text="Minimum price: ", bg='white',
                                   fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=1, column=0)
        self.price_min = tk.StringVar()
        price_min_entry = tk.Entry(entry_frame, textvariable=self.price_min, width=23, fg='plum4')
        price_min_entry.grid(row=1, column=1)

        price_max_label = tk.Label(entry_frame, text="Maximum price: ", bg='white',
                                   fg="thistle3", font=("Calibri", 12, 'bold')).grid(row=2, column=0)
        self.price_max = tk.StringVar()
        price_max_entry = tk.Entry(entry_frame, textvariable=self.price_max, width=23, fg='plum4')
        price_max_entry.grid(row=2, column=1)
        self.draw_result_label = tk.Label(self, text="Randomly selected gift: ", bg='white',
                                          fg="thistle4", font=("Calibri", 12, 'bold'))

        self.draw_button = tk.Button(self, width=20, height=2, fg='thistle2', bg='plum4', text="Click to draw",
                                      font=("Calibri", 12, 'bold'),
                                      command=lambda: self.draw(parent))
        self.draw_button.pack(pady=2)
        self.draw_result_label.pack(pady=10)

        self.confirm_button = ttk.Button(self, style="D.TButton", text="Select this gift",
                                         command=lambda: self.choose_gift(parent))

        self.confirm_button.pack(pady=2)

    def draw(self, parent):
        occasion = self.o.get()
        ocas = get_occasion_by_name(occasion)
        min_price = self.price_min.get()
        max_price = self.price_max.get()
        person = int(parent.person)
        per = get_person(person)
        gifts = get_gift_ideas_for_selected_occasion_and_price_range(ocas, int(min_price), int(max_price), per)
        self.gift = random.choice(gifts)

        string = "a randomly selected gift: " + str(self.gift.name) + ' - ' + 'price: ' + \
                 str(self.gift.price_min) + '-' + str(self.gift.price_max)
        self.draw_result_label.configure(text=string)

    def choose_gift(self, parent):
        price = (self.gift.price_max + self.gift.price_min) // 2
        per = parent.person
        oca = self.o.get()
        occasion = get_occasion_by_name(oca)
        person = get_person(int(per))
        add_selected_gift(self.gift, person, occasion.id, price)
        popupmsg("selected gift add")


class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg='plum4', width=200, height=620, padx=3)
        b_style = ttk.Style()
        b_style.configure('W.TButton', font=('calibri', 18, 'bold'),
                          borderwidth='3', foreground='plum4')
        self.show_selected_gift_to_buy_button = ttk.Button(self, style='W.TButton',
                                                           text='Show selected gifts',
                                                           command=lambda: parent.switch_frame(ShowGiftToBuyFrame))
        self.show_selected_gift_to_buy_button.pack(ipadx=24, ipady=10)

        self.choose_gift_for_person_button = ttk.Button(self, style='W.TButton', text='Choose a gift for person',
                                                        command=lambda: parent.switch_frame(ChooseGiftMenuFrame))
        self.choose_gift_for_person_button.pack(ipady=10)

        self.add_gift_idea_button = ttk.Button(self, style='W.TButton', text='Add gift idea',
                                               command=lambda: parent.switch_frame(AdGiftIdeaFrame))
        self.add_gift_idea_button.pack(ipadx=53, ipady=10)

        self.add_gift_idea_to_person_button = ttk.Button(self, style='W.TButton', text='Add gift idea to person',
                                                         command=lambda: parent.switch_frame(AddGiftIdeaToPersonFrame))
        self.add_gift_idea_to_person_button.pack(ipadx=5, ipady=10)

        self.show_bought_gifts_button = ttk.Button(self, style='W.TButton', text='Show bought gifts',
                                                   command=lambda: parent.switch_frame(ShowBoughtGiftsFrame))
        self.show_bought_gifts_button.pack(ipadx=29, ipady=10)

        self.add_person_button = ttk.Button(self, style='W.TButton', text='Add person',
                                            command=lambda: parent.switch_frame(AddPersonFrame))
        self.add_person_button.pack(ipadx=53, ipady=10)

        self.change_budget_button = ttk.Button(self, style='W.TButton', text='Change your budget',
                                               command=lambda: parent.switch_frame(ChangeBudgetFrame))
        self.change_budget_button.pack(ipadx=19, ipady=10)


root = GiftHelper()
root.geometry("1280x720")

login_window = GiftHelperLogin(root)

root.mainloop()
