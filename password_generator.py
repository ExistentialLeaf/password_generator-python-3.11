import random,string
import tkinter as tk
import tkinter.ttk as ttk

def password():
    length = int(length_slider.get())
    num = checkbox_var.get()
    strength = strength_var.get()
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    num_len = length // 3
    
    if strength == 'weak':
        if num:
            length -= num_len
            pwd += ''.join(random.choices(dig, k=num_len))
        pwd += ''.join(random.choices(lower, k=length))
        
    elif strength == 'strong':
        if num:
            length -= num_len
            pwd += ''.join(random.choices(dig, k=num_len))
        pwd += ''.join(random.choices(letter, k=length))
        
    elif strength == 'very':
        ran = random.randint(2, num_len)
        if num:
            length -= ran
            pwd += ''.join(random.choices(dig, k=ran))
        pwd += ''.join(random.choices(punct, k=ran))
        pwd += ''.join(random.choices(letter, k=length - ran))
        
    pwd = list(pwd)
    random.shuffle(pwd)
    password_var.set(''.join(pwd))
    
def copy_to_clipboard():
    genpwd.clipboard_clear()
    genpwd.clipboard_append(password_var.get())

passwords = {'weak': [], 'strong': [], 'very': []}
def save_password():
    password_to_save = password_var.get()
    strength = strength_var.get()
    passwords[strength].append(password_to_save)

    with open("password.txt", "w") as file:
        for strength_type in passwords:
            file.write(f"{strength_type.capitalize()} Passwords:\n")
            for pwd in passwords[strength_type]:
                file.write(f"{pwd}\n")
            file.write("\n")

def update_password_bg(*args):
    bg_colors = {'weak': 'red', 'strong': 'orange', 'very': 'green'}
    bg_password = bg_colors.get(strength_var.get(), 'light blue')
    style.configure('TMenubutton', background=bg_password, font=('Arial', 12))

genpwd = tk.Tk()
genpwd.title("Password Generator")
genpwd.config(cursor="hand2", bg='dark blue')

style = ttk.Style()

frame = tk.Frame(genpwd, bg='dark blue')
frame.pack(padx=10, pady=10)

label_length = tk.Label(frame, text="Length of Password:", bg='dark blue', fg='orange', font=('Arial', 15))
label_length.grid(row=0, column=0)

length_slider = tk.Scale(frame, from_=6, to=20, orient="horizontal", bg='light blue')
length_slider.grid(row=0, column=1)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(frame, text="Include Numbers", variable=checkbox_var, bg='dark blue', fg='orange', font=('Arial', 12))
checkbox.grid(row=1, column=1,columnspan=2)

strength_var = tk.StringVar(value='weak')
strength_label = tk.Label(frame, text="Select Strength:", bg='dark blue', fg='orange', font=('Arial', 12))
strength_label.grid(row=2, column=0)

strength_options = ['weak', 'strong', 'very']
strength_menu = ttk.OptionMenu(frame, strength_var, strength_options[0], *strength_options)
strength_menu.grid(row=2, column=1)

generate_button = tk.Button(frame, text="Generate Password", command=password, bg='light blue', font=('Arial', 12))
generate_button.grid(row=3, columnspan=2, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(frame, textvariable=password_var, height=2, width=30, relief='sunken',bg='light blue')
password_label.grid(row=4, column=0, columnspan=1, padx=5)
password_label.configure(font=('Arial', 10), padx=4)

strength_var.trace_add('write', update_password_bg)
update_password_bg()

copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, bg='light blue', font=('Arial', 13))
copy_button.grid(row=4, column=1, padx=5)

save_button = tk.Button(frame, text="Save Password", command=save_password, bg='light blue', font=('Arial', 13))
save_button.grid(row=5, columnspan=2, pady=10)

genpwd.mainloop()