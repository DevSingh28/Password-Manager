from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    user_input_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    a = user_input_1.get()
    b = user_input_2.get()
    c = user_input_3.get()
    new_data = {
        a: {
            "email": b,
            "password": c,
        }
    }

    if len(a) == 0 or len(c) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            user_input_1.delete(0, END)
            user_input_3.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    a = user_input_1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data File Not Found")

    else:
        if a in data:
            email = data[a]["email"]
            password = data[a]["password"]
            messagebox.showinfo(title=a, message=f"Email: {email} \nPassword: {password}")

        else:
            messagebox.showerror(title="Error", message=f"No data available for {a}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

user_input_1 = Entry(width=35)
user_input_1.focus()
user_input_1.grid(row=1, column=1, columnspan=2)

user_input_2 = Entry(width=35)
user_input_2.insert(END, string="devsingh2017dp@gmail.com")
user_input_2.grid(row=2, column=1, columnspan=2)

user_input_3 = Entry(width=35)
user_input_3.grid(row=3, column=1, columnspan=2)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=3)

button2 = Button(text="Add", width=36, command=save)
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text="Search", width=15, command=find_password)
button3.grid(row=1, column=3)
mainloop()
