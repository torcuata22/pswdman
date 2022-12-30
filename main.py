from tkinter import *
from tkinter import messagebox
#messagebox is a module of code, not a class! (it's not imported with *)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# SAVE PASSWORD 
def save():
    #use get() to get data from entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #create message box to confirm user is happy with password:
    #messagebox.showinfo(title="Title", message="Message")
    #messagebox.askyesno(title,message, options)
    #messagebox.askquestion(title, message, options)
    #messagebox.yesnocancel(title, message, options)

    messagebox.askokcancel(title=website, message=f"This is the information you entered: \n website: {website}\n email: {email}\n password: {password}\n Is it ok to save?")




    with open("data.txt", "a") as data_file:
        data_file.write(f"website: {website} | email: {email} | password: {password} \n")
    website_entry.delete(0, END) #(0, END) deletes all text in widget 
    #email_entry.delete(0, END)
    password_entry.delete(0,END)

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# title_label = Label(text="Timer")
# title_label.grid(column=1, row=0)

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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=17, command = save) 
add_button.grid(column=1, row=4)

#Entries:
website_entry = Entry()
website_entry.grid(column=1, row=1)# columnspan=2)
website_entry.focus() #makes cursornappear on "website" entry

email_entry = Entry()
email_entry.grid(column=1, row=2)# columnspan=2)
email_entry.insert(0, "marilynmarquez@email.com") #prefills email field, 0 is 0-index, if I wasnt to add at the end, use END

password_entry = Entry()
password_entry.grid(column=1, row=3)











window.mainloop()