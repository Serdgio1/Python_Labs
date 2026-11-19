import  tkinter as tk
from tkinter import messagebox
import random
import subprocess

def letter_to_digit(letter):
    position = ord(letter.upper()) - ord('A') + 1
    return position % 10

def generate_key(word):
    word = word.upper()

    if len(word) != 6 or not word.isalpha() or not word.isascii():
        raise ValueError('Invalid word')

    first_block = ''.join(random.choices(word, k=3))

    second_block = ''.join(
        str(letter_to_digit(letter)) for letter in word
    )

    third_block = ''.join(random.choices(word, k=3))

    return f'{first_block}-{second_block}-{third_block}'

def generate_on():
    word = word_entry.get()
    try:
        key = generate_key(word)
        key_entry.config(state='normal')
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)
        key_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid 6-letter word.')

def on_close():
    music.terminate()
    root.destroy()

root = tk.Tk()
root.title('Witcher key generator')
root.geometry('600x450')
root.resizable(False, False)

root.configure(bg='#171717')

root.protocol('WM_DELETE_WINDOW', on_close)

music = subprocess.Popen(
    ['afplay', 'Geralt_of_Rivia.mp3'],
)

background_photo = tk.PhotoImage(file='witcher.png')

background_label = tk.Label(
    root,
    image=background_photo,
)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = tk.Frame(root, bg='#171717')
main_frame.pack(expand=True)

title_label = tk.Label(
    main_frame,
    text='WITCHER KEY GENERATOR',
    font=('Georgia', 24, 'bold'),
    fg='#D5C5A1',
    bg='#171717'
)
title_label.pack(pady=30)

input_label = tk.Label(
    main_frame,
    text='ENTER A 6-LETTER WORD:',
    font=('Arial', 11),
    fg='#AAAAAA',
    bg='#171717'
)
input_label.pack(pady=5)

word_entry = tk.Entry(
    main_frame,
    font=('Arial', 16),
    justify='center',
    bg='#292929',
    fg='#FFFFFF',
    insertbackground='#FFFFFF',
    relief='flat',
)
word_entry.pack(pady=10, ipady=8)

generate_button = tk.Button(
    main_frame,
    text='GENERATE KEY',
    font=('Arial', 12, 'bold'),
    fg='#F5E6C8',
    bg='#A83232',
    activebackground='#C44747',
    activeforeground='#FFFFFF',
    relief='flat',
    borderwidth=0,
    cursor='hand2',
    command=generate_on
)
generate_button.pack(pady=20, ipadx=30, ipady=8)

key_entry = tk.Entry(
    main_frame,
    font=('Consolas', 18, 'bold'),
    justify='center',
    bg='#292929',
    fg='#D5C5A1',
    relief='flat',
    state='readonly',
)
key_entry.pack(pady=15, ipady=8)

root.mainloop()