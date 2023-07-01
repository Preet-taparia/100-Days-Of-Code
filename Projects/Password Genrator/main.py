import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint


def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



def save_password():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email":email,"password":password,}}
     
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please provide all information")
    else:
        try:       
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)   


def find_password():
    website = website_entry.get()
    
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exist")
        
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Website does not exist")
    
            


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg='#856ff8')


website_label = Label(text="Website:", width=13)
website_label.grid(row=0, column=0, padx=5, pady=5)

email_label = Label(text="Email/Username:", width=13)
email_label.grid(row=1, column=0, padx=5, pady=5)

password_label = Label(text="Password:", width=13)
password_label.grid(row=2, column=0, padx=5, pady=5)

website_entry = Entry(width=40)
website_entry.grid(row=0, column=1, padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=59)
email_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
email_entry.insert(END, "preettaparia@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(row=2, column=1, padx=5, pady=5)

search_button = Button(text="Search",width=15, command= find_password)
search_button.grid(row=0, column=2, padx=5, pady=5)

generate_password_button = Button(text = "Genrate Password",width=15, command= generate_password )
generate_password_button.grid(row=2, column=2, padx=5, pady=5)

add_buton = Button(text = "Add", width=50, command=save_password)
add_buton.grid(row=3, column=1, columnspan=2, padx=5, pady=5)


window.mainloop()