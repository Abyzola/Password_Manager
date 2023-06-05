import json
from tkinter import *
from random import shuffle, randint, choice
import pyperclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # Copying password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    fresh_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty")
    else:
        # Using the try, except, else and finally format
        try:
            with open("data.json", "r") as new_file:
                # Reading old data
                data = json.load(new_file)
        except FileNotFoundError:
            with open("data.json", "w") as new_file:
                json.dump(fresh_data, new_file, indent=4)
        else:
            data.update(fresh_data)
            with open("data.json", "w") as new_file:
                json.dump(data, new_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as new_file:
            data = json.load(new_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:  {email}\nPassword:  {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FF8E9E")

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30, bg="#EEEEEE")
website_entry.grid(row=1, column=1)


# Email
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=30, bg="#EEEEEE")
email_entry.insert(0, "your@gmail.com")
email_entry.grid(row=2, column=1)

# Password
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_entry = Entry(width=30, bg="#EEEEEE")
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_button = Button(text="Generate Password", width=15, command=generate_password, bg="#F9B5D0")
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=30, command=save, bg="#65E892")
add_button.grid(row=4, column=1)

# Search
search_button = Button(text="Search", width=15, command=find_password, bg="#F9B5D0")
search_button.grid(row=1, column=2)


window.mainloop()
