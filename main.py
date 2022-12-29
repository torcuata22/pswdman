from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
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

add_button = Button(text="Add", width=17) #course has RadioButton
add_button.grid(column=1, row=4)

#Entries:
website_entry = Entry()
website_entry.grid(column=1, row=1)# columnspan=2)
email_entry = Entry()
email_entry.grid(column=1, row=2)# columnspan=2)
password_entry = Entry()
password_entry.grid(column=1, row=3)











window.mainloop()