from tkinter import *
from tkinter import messagebox
import string
import random
import json


# create password


def password_generator():
    password_entry.delete(0, END)
    num_char_list = list(string.digits)
    letter_char_list_up = list(string.ascii_uppercase)
    letter_char_list_low = list(string.ascii_lowercase)
    special_char_list = list("!@#$%^&*()")

    password = []
    for i in range(4):
        password.append(random.choice(num_char_list))
    for i in range(2):
        password.append(random.choice(letter_char_list_low))

    password.append(random.choice(letter_char_list_up))
    password.append(random.choice(special_char_list))

    random.shuffle(password)

    passs = ""

    for item in password:
        passs += item

    password_entry.insert(0, passs)


# SAVE PASSWORD


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="oops", message="Please make sure you haven't left any fields empty")
    else:
        with open("data1.json", "r") as data1_file:
            # json dosyasını okuma
            data1 = json.load(data1_file)
            # updating old data with new data
            data1.update(new_data)
            # json dosyasına yazma
            json.dump(new_data, data1_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "seymaaozlerr@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(
    text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
