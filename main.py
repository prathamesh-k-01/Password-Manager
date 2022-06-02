from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_passwordf():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_letters.extend(password_symbols)
    password_letters.extend(password_numbers)
    random.shuffle(password_letters)

    password_1 = ""
    for char in password_letters:
        password_1 += char

    password_input.insert(0, password_1)
    pyperclip.copy(password_1)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_store = website_input.get()
    username = email_username_input.get()
    password_store = password_input.get()

    new_dict = {website_store: {
        "username": username,
        "password": password_store,
    }
    }
    if len(website_store) == 0 or len(password_store) < 8:
        messagebox.askretrycancel(title=f"{website_store}", message="Please Check Inputs")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)
            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        except:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_dict, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)


# -----------------------------Search Feature----------------------------#

def search():
    website_search = website_input.get()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")

    if website_search in data:
        email = data[website_search]["username"]
        password_s = data[website_search]["password"]
        messagebox.showinfo(title=website_search, message=f"The  User id: {email} \nThe Password: {password_s}")
        pyperclip.copy(password_s)
    else:
        messagebox.showinfo(title="Error", message="No Website found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, )
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Arial", 10, "bold"), pady=10, padx=10)

website.grid(column=0, row=1)

website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1)

email_username = Label(text="Email/Username:", font=("Arial", 10, "bold"), pady=10, padx=10)

email_username.grid(column=0, row=2)

email_username_input = Entry(width=45)
email_username_input.insert(0, "prathmeshkulkarni1409@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:", font=("Arial", 10, "bold"), pady=10, padx=10)
password.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password = Button(text="Generate Password", pady=2, padx=2, command=generate_passwordf)
generate_password.grid(column=2, row=3)

ok = Button(text="OK", width=36, pady=2, padx=2, command=save)
ok.grid(column=1, row=4, columnspan=2)

search_button = Button(text="🔍  Search", pady=2, padx=2, width=20, bg="yellow", command=search)
search_button.grid(column=2, row=1)
window.mainloop()
