from tkinter import *
from tkinter import messagebox
import pandas as pd

# __________________________Stage 1 - validating the email_____________________________ #
special_char = ['~', ':', "'", '+', '[', '\\', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
                '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def validate():
    user = user_input.get()

    id_mail = [x for x in user if x in "@."]
    if len(id_mail) == 2 and id_mail[0] == '@' and id_mail[1] == ".":
        if user[(user.index("@") + 1)] != ".":
            if user[0] not in numbers and user[0] not in special_char:
                if 5 < len(user) <= 20:
                    upper_count, lower_count, number_count, special_count = 0, 0, 0, 0
                    for i in range(len(user)):
                        if user[i].isupper():
                            upper_count += 1
                        elif user[i].islower():
                            lower_count += 1
                        elif user[i].isdigit():
                            number_count += 1
                        else:
                            special_count += 1
                    if upper_count >= 1 and lower_count >= 1 and number_count >= 1 and special_count >= 1:
                        messagebox.showinfo(title="Success", message="Your mail id entered is validated")
                        return True
                    else:
                        messagebox.showinfo(title="Oops", message="Your mail id entered is invalid\n"
                                                                  " The mail id should contain:\n One uppercase\n "
                                                                  "One digit\n One special character\n One lowercase")
                        return False
                else:
                    messagebox.showinfo(title="Oops", message="Your mail id entered is invalid\n"
                                                              " The mail id should contain:\n One uppercase\n "
                                                              "One digit\n One special character\n One lowercase")
                    return False
            else:
                messagebox.showinfo(title="Oops", message="Your mail id entered is invalid\n"
                                                          " The mail id should contain:\n One uppercase\n "
                                                          "One digit\n One special character\n One lowercase")
                return False
        else:
            messagebox.showinfo(title="Oops", message="Your mail id entered is invalid\n"
                                                      " The mail id should contain:\n One uppercase\n "
                                                      "One digit\n One special character\n One lowercase")
            return False
    else:
        messagebox.showinfo(title="Oops", message="Your mail id entered is invalid\n"
                                                  " The mail id should contain:\n One uppercase\n "
                                                  "One digit\n One special character\n One lowercase")
        return False


# __________________________Stage 2 - Store the data in a file_____________________________ #

def save():
    save_user = user_input.get()
    save_pass = pass_input.get()

    if len(save_user) == 0 or len(save_pass) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave the fields empty!")
    else:
        df = pd.read_csv("data.txt", names=["Mail_id", "Password"])
        data_check = df.loc[df.Mail_id == save_user]
        if len(data_check) > 0:
            messagebox.showinfo(title="Oops", message="This mail id is already registered.please login")
        else:
            if validate():
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{user_input.get()}, {pass_input.get()}\n")
                    user_input.delete(0, END)
                    pass_input.delete(0, END)
                    messagebox.showinfo(title="Success", message="You have successfully registered as user!")


# __________________________Stage 3 - Reading the data____________________________________ #

def check():
    check_user = user_input.get()
    check_pass = pass_input.get()
    if len(check_user) == 0 or len(check_pass) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave the fields empty!")

    else:
        with open("data.txt", "r") as data:
            data_file = data.read()
            if check_user in data_file and check_pass in data_file:
                messagebox.showinfo(title="Success", message="You have successfully logged in!")
                user_input.delete(0, END)
                pass_input.delete(0, END)
            else:
                messagebox.showinfo(title="Oops", message=f"If you are not a user, please register! "
                                                          "or check whether the entered details are correct")


# __________________________Stage 4 - getting the value from the stored file____________________________________ #

def get_value():
    pass_input.delete(0, END)
    get_user = user_input.get()
    get_pass = pass_input.get()
    if len(get_user) > 0 and len(get_pass) == 0:
        data = pd.read_csv("data.txt", names=["Mail_id", "Password"])
        value = data.loc[data.Mail_id == get_user]
        if len(value) > 0:
            answer = data.loc[data.Mail_id == get_user].Password.item()
            pass_input.insert(0, answer)
            messagebox.showinfo(title="Password Retrieved", message="Password has been pasted from your stored file."
                                                                    "Please login now!")
        else:
            messagebox.showinfo(title="Please Register", message="Please register you are not a user")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Registration and Login System")
window.config(padx=50, pady=50)

canvas = Canvas(width=250, height=250)
login_img = PhotoImage(file="login.png")
canvas.create_image(125, 100, image=login_img)
canvas.grid(row=0, column=1)

# Label

login_label = Label(text="Login", fg="blue", font=("Courier", 50, "bold"))
login_label.grid(row=1, column=1)

user_name = Label(text="Username/E-mail:", font=("Courier", 10, "bold"))
user_name.grid(row=2, column=0)

pass_name = Label(text="Password:", font=("Courier", 10, "bold"))
pass_name.grid(row=3, column=0)

# Entry
user_input = Entry(width=60)
user_input.focus()
user_input.grid(row=2, column=1, columnspan=3)

pass_input = Entry(width=60)
pass_input.grid(row=3, column=1, columnspan=3)

# Button

login = Button(text="Login", width=35, command=check)
login.grid(row=5, column=1, columnspan=1)

forget_pass = Button(text="Forgot Password?", width=15, command=get_value)
forget_pass.grid(row=5, column=2, columnspan=1)

register = Button(text="Register", width=52, command=save)
register.grid(row=6, column=1, columnspan=3)

window.mainloop()
