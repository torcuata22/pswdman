from tkinter import *
import random
from tkinter import messagebox
import json
#messagebox is a module of code, not a class! (it's not imported with *)
#import pyperclip (won't import it for some reason, although it is installed) LECTURE 268
#pyperclip allows you to save info in clipboard automatically so you can paste it (password)


# PASSWORD GENERATOR

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters-1)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols-1)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers-1)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    #use join method to create password:
    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)



# SAVE PASSWORD 
def save():
    website = website_entry.get() #use get() to get data from entries
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email':email,
            'password': password
        }
        }

    if len(website) == 0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you filled out all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data:
                data = json.load(data_file)
               
        except FileNotFoundError:
            with open("data.json",'w') as data_file:
                #Save updated data:
                json.dump(new_data, data_file, indent=4)

        else:
            #Update old data:
            data.update(new_data)
            with open("data.json",'w') as data_file:
                #Save updated data:
                json.dump(data, data_file, indent=4)

        finally:
                website_entry.delete(0, END) #(0, END) deletes all text in widget 
                #email_entry.delete(0, END)
                password_entry.delete(0,END)


#FIND PASSWORD:

def find_password():
    website = website_entry.get()
    #search through data.json:
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"] #BECAUSE DATA IS  A NESTED DICTIONARY
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#add image using canvas widget:
canvas = Canvas(width=300 ,height=300)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(150, 150, image= logo_img) 

canvas.grid(column=1, row=0) #without this it won't show the image

website_label = Label(text="Website: ",)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ",)
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ",)
password_label.grid(column=0, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=19, command = save) 
add_button.grid(column=1, row=4)

#Entries:
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus() #makes cursor appear on "website" entry

email_entry = Entry(width=21)
email_entry.grid(column=1, row=2)# columnspan=2
email_entry.insert(0, "marilynmarquez@email.com") #prefills email field, 0 is 0-index, if I wasnt to add at the end, use END

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)











window.mainloop()




#NOTES:
# #data_file.write(f"website: {website} | email: {email} | password: {password} \n")
            # #To write json file: use "r" with context manager
            # #json.dump(new_data, data_file, indent=4) #first: format I want to use (json), second, the file I'm dumping
            # #To read json data: use load():
            # data = json.load(data_file)
            # #print(data)

            # #to update data: json.update, use "w" with context manager
            # data.update(new_data)
            # json.dump(data, data_file, indent=4) 

            #OLD POP-UP:
             #is_ok = messagebox.askokcancel(title=website, message=f"This is the information you entered:\n website: {website}\n email: {email}\n password: {password}\n Is it ok to save?")
        #if is_ok: