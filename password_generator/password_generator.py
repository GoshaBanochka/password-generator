from tkinter import *
import random
import string


def generator():
    try:
        length = int(pass_len.get())
    except ValueError:
        length = 8
        pass_len.delete(0, END)
        pass_len.insert(0, '8')
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

def save_password():
    password = pass_entry.get()
    if password != '':
        with open('passwords.txt', 'a') as f:
            f.write(password + '\n')
        pass_listbox.insert(END, password)

def load_passwords():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f:
                clean_password = line.strip() 
                if clean_password != "":
                    pass_listbox.insert(END, clean_password)
    except FileNotFoundError:
        pass


root = Tk()
root.title("Password Generator")
root.geometry('400x700')
root.configure(bg='black')
root.resizable(False, False)
root.iconbitmap('icon.ico')


pass_listbox = Listbox(root, font=('Consolas', 20), width=30, bg='black', fg='white')
pass_listbox.pack(side=BOTTOM)


save_button = Button(root, text='Save', command=save_password, font=('Consolas', 20), bg='black', fg='white')
save_button.pack(side=BOTTOM)
                 
gen_button = Button(root, text='Generate Password', command=generator, 
                    font=('Consolas', 20), bg='black', fg='white')
gen_button.pack(side=BOTTOM)


prog_name = Label(root,
              text = 'Random Password Generator',
              font=('Consolas', 20), bg='black', fg='white')
prog_name.pack()

pass_len_label = Label(root, text= 'Length',
                       font = ('Consolas', 20), bg='black', fg='white')
pass_len_label.pack()


pass_len = Entry(root, font=('Consolas', 20), width=5)
pass_len.pack()

pass_entry_label = Label(root, text= 'Your password',
                       font = ('Consolas', 20), bg='black', fg='white')
pass_entry_label.pack(pady=30)
pass_entry = Entry(root, font=('Consolas', 20))
pass_entry.pack(pady=1)

load_passwords()
root.mainloop()