from tkinter import *
from user_controller import create_user, check_data_to_create_account


def register_user():
    username_info = username.get()
    password_info = password.get()
    password2_info = password2.get()
    budget_info = budget.get()
    label = Label(screen1, text="De")
    label.pack()



    check = check_data_to_create_account(password_info, password2_info,
                                         budget_info, username_info)

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password2_entry.delete(0,END)
    budget_entry.delete(0, END)

    if check == "correct":
        create_user(username_info, password_info, budget_info)
        label.configure(text="Registration Sucess", fg="green", font=("calibri", 11))

    else:
        label.configure(text=check, fg="red", font=("calibri", 11))




def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("350x350")

    global username
    global password
    global password2
    global username_entry
    global password_entry
    global budget_entry
    global password2_entry
    global budget
    username = StringVar()
    password = StringVar()
    budget = StringVar()
    password2 = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="Confirm password * ").pack()
    password2_entry = Entry(screen1, textvariable=password2, show="*")
    password2_entry.pack()
    Label(screen1, text="Budget * ").pack()
    budget_entry = Entry(screen1, textvariable=budget)
    budget_entry.pack()

    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    print("Login session started")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Gift helper")
    Label(text="Gift helper", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()
