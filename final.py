from tkinter import *
from random import randint

root = Tk()
root.title('Strong Password Generator')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

def entry_box(length):

    pw_entry.delete(0, END)

    my_password = ''

    for x in range(length):
        my_password += chr(randint(33,126))

    pw_entry.insert(0, my_password)


def clip():

    root.clipboard_clear()

    root.clipboard_append(pw_entry.get())

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Times New Roman", 24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Times New Roman", 24), bd=0, bg="green")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)


my_button = Button(my_frame, text="Generate password", command=lambda: entry_box(int(my_entry.get())))
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy", command=clip)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
