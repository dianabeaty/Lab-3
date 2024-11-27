import tkinter as tk
import random
from tkinter import messagebox
import string
import pygame

window = None
dec_input_entry = None
key_display = None

def generate_key():
    dec_input = dec_input_entry.get()
    
    if not dec_input.isdigit() or len(dec_input) != 3:
        messagebox.showerror("Ошибка", "Введите корректное DEC-число (3 знака).")
        return

    shifts = [int(digit) for digit in dec_input]
    key_parts = []
    current_length = 5

    for i, shift in enumerate(shifts):
        block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=current_length))
        key_parts.append(block)

        if i % 2 == 0:
            block = shift_string(block, shift)
        else:
            block = shift_string(block, -shift)

        current_length -= 1
    
    last_block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    key_parts.append(last_block)

    key = '-'.join(key_parts)
    key_display.delete(0, tk.END)
    key_display.insert(0, key)

def shift_string(s, shift):
    characters = string.ascii_uppercase + string.digits
    shifted = []
    
    for char in s:
        if char in characters:
            index = characters.index(char)
            new_index = (index + shift) % len(characters)
            shifted.append(characters[new_index])
        else:
            shifted.append(char)
    
    return ''.join(shifted)

def setup_ui():
    global window, dec_input_entry, key_display

    window = tk.Tk()
    window.title("Key Generator")
    window.geometry("1300x750")

    bg_image = tk.PhotoImage(file="photo_2024-11-26 19.36.13 copy.png")

    window.bg_image = bg_image
    
    background_label = tk.Label(window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(window, borderwidth=2, relief="groove", bg='#800000')
    frame.pack(padx=5, pady=5)
    frame.place(x=569, y=448)
    
    dec_input_label = tk.Label(frame, text="Введите DEC-число (3 знака)", bg='white')
    dec_input_label.pack(pady=3, padx=3)
    
    dec_input_entry = tk.Entry(window, bg='#800000', fg="white")
    dec_input_entry.pack(pady=5)
    dec_input_entry.place(relx=0.444, rely=0.65)

    generate_button = tk.Button(window, text="Сгенерировать ключ", command=generate_key)
    generate_button.pack(pady=3, padx=10)
    generate_button.place(x=585.5, y=525)

    key_display = tk.Entry(window, font=("Arial", 14), bg='#800000', justify='center', fg="white")
    key_display.pack(pady=10)
    key_display.place(relx=0.45, rely=0.75)

    
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/user/Downloads/Моя Кофейня_ Рецепты и Истории. 2.mp3")
    pygame.mixer.music.play(-1)





if __name__ == "__main__":
    setup_ui()
    window.mainloop()