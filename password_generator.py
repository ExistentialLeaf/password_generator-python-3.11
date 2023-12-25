from operator import le
import random,string
import tkinter as tk
import tkinter.ttk as ttk

from kiwisolver import strength

def password():
    len = int(len_slider.get())
    num = check_var.get()
    strength = stren_var.get()
    lower = string.ascii_lowercase
    letter = lower + string.ascii_uppercase
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    num_len = len//3
    
    if strength == 'weak':
        if num:
            len -= num_len
            pwd += ''.join(random.choices(dig,k=num_len))
        pwd += ''.join(random.choices(lower,k=len))
        
    elif strength == 'strong':
        if num:
            len -= num_len
            pwd += ''.join(random.choices(dig,k=num_len))
        pwd += ''.join(random.choices(letter,k=len))
        
    elif strength == 'very':
        ran = random.randint(2,num_len)
        if num:
            len -= ran
            pwd += ''.join(random.choices(dig,k=ran))
        pwd += ''.join(random.choices(punct,k=ran))
        pwd += ''.join(random.choices(letter,k=len-ran))
    
    pwd = list(pwd)
    random.shuffle(pwd)
    pwd_var.set(''.join(pwd))
    
def copy():
    genpwd.clipboard_clear()
    genpwd.clipboard_append(pwd_var.get())

pwds = {'weak': [], 'strong': [], 'very': []}
def save_pwd():
    pwd_save = pwd_var.get()
    strength = stren_var.get()
    pwds[strength].append(pwd_save)

    with open("password.txt", "w") as file:
        for stren_type in pwds:
            file.write(f"{stren_type.capitalize()} Passwords:\n")
            for pwd in pwds[stren_type]:
                file.write(f"{pwd}\n")
            file.write("\n") 
    
def update_pwd_bg(*args):
    bg_ = {'weak': 'red', 'strong': 'orange', 'very': 'green'}
    bg_pwd = bg_.get(stren_var.get(), 'light blue')
    style.configure('TMenubutton', background=bg_pwd, font=('Arial', 12))    
    
genpwd = tk.Tk()
genpwd.title("Password Generator")
genpwd.config(cursor="hand2", bg='dark blue')

style = ttk.Style()

frame_pwd = tk.Frame(genpwd, bg='dark blue')
frame_pwd.pack(padx=10, pady=10)

label_len = tk.Label(frame_pwd, text="Length of Password:", bg='dark blue', fg='orange', font=('Arial', 12))
label_len.grid(row=0, column=0)

len_slider = tk.Scale(frame_pwd, from_=6, to=20, orient="horizontal", bg='light blue')
len_slider.grid(row=0, column=1)

check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(frame_pwd, text="Include Numbers", variable=check_var, bg='dark blue', fg='orange', font=('Arial', 12))
checkbox.grid(row=1, column=1,columnspan=2)

stren_var = tk.StringVar(value='weak')
stren_label = tk.Label(frame_pwd, text="Select Strength:", bg='dark blue', fg='orange', font=('Arial', 12))
stren_label.grid(row=2, column=0)

stren_opt = ['weak', 'strong', 'very']
stren_menu = ttk.OptionMenu(frame_pwd, stren_var, stren_opt[0], *stren_opt)
stren_menu.grid(row=2, column=1)

gen_button = tk.Button(frame_pwd, text="Generate Password", command=password, bg='light blue', font=('Arial', 12))
gen_button.grid(row=3, columnspan=2, pady=10)

pwd_var = tk.StringVar()
pwd_label = tk.Label(frame_pwd, textvariable=pwd_var, height=2, width=30, relief='sunken',bg='light blue')
pwd_label.grid(row=4, column=0, columnspan=1, padx=5)
pwd_label.configure(font=('Arial', 10), padx=4)

stren_var.trace_add('write', update_pwd_bg)
update_pwd_bg()

copy_ = tk.Button(frame_pwd, text="Copy to Clipboard", command=copy, bg='light blue', font=('Arial', 13))
copy_.grid(row=4, column=1, padx=5)

save_= tk.Button(frame_pwd, text="Save Password", command=save_pwd, bg='light blue', font=('Arial', 13))
save_.grid(row=5, columnspan=2, pady=10)

genpwd.mainloop()
