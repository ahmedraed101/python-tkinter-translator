from googletrans import Translator
from googletrans import LANGCODES, LANGUAGES
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def tranlate():
    # print(dir(frame_one_input_text_input))
    text = frame_one_input_text_input.get("1.0", tk.END)
    print(text)
    list_of_text = text.strip().split("\n")
    print(list_of_text)

# frame one [ScrolledText, optionmenu, button'translate']
# frame two [label, optionmenu, button'copy']


root = tk.Tk()
root.minsize("700", "700")
root.configure(bg="#1c2934")
root.title("translator")

header = tk.Label(
    root, text="Translate any thing you need",
    bg="#03FDD7", fg="black", font=("sans-serif", 16)
)
header.grid(ipady=5, ipadx=5, pady=10)

# frame1 = tk.Frame(root, bg="#1c2934")
# frame1.grid()

# clicked = tk.StringVar()

# listbox = tk.OptionMenu(frame1, clicked, *LANGCODES.keys())
# listbox.config(font=("sans-serif", 16))
# listbox.grid()
frame_one = tk.Frame(root, bg='#1c2934')
frame_one.grid(ipady=10, padx=10)

frame_one_input_text = tk.Frame(frame_one, bg='#1c2934')
frame_one_input_text.grid(column=0, row=0, ipadx=5, ipady=5)

# input text
frame_one_input_text_input = ScrolledText(
    frame_one_input_text, width=50, height=10, padx=10, pady=10)
frame_one_input_text_input.config(
    font=("sans-serif", 18), bg="#B3ECE2", fg="black")
frame_one_input_text_input.grid(column=0, row=0)

# input buttons
frame_one_input_buttons = tk.Frame(frame_one, bg="#1c2934")
frame_one_input_buttons.grid(column=1, row=0)

value = tk.StringVar()
frame_one_input_buttons_select = tk.OptionMenu(
    frame_one_input_buttons, value, *LANGCODES.keys())
frame_one_input_buttons_select.grid(column=0, row=0)
frame_one_input_buttons_select.config(font=("sans-serif", 16))

frame_one_input_buttons_translate = tk.Button(
    frame_one_input_buttons, text="Translate", command=tranlate, font=("sans-serif", 16), foreground="#1c2934")
frame_one_input_buttons_translate.grid(column=0, row=1)

# # frame two for output
frame_two = tk.Frame(root, bg='#1c2934')
frame_two.grid()

# frame_two_output = tk.Frame(frame_two, bg='#1c2934')
frame_two_output = tk.Frame(frame_two, bg='red', width=500)
# frame_two_output.grid(sticky='wse')
frame_two_output.grid(column=0, row=0, padx=10, pady=10)
# frame_two_output.grid_propagate(0)


frame_two_output_text = tk.Label(
    frame_two_output,
    text="Give me your birth date ಠ_ಠ",
    font=("sans-serif", 16),
    background="#1c2934",
    # background="red",
    foreground="white",
    anchor="center",
    wraplength=480
)
frame_two_output_text.grid()

frame_two_buttons = tk.Frame(frame_two, bg='#1c2934')
frame_two_buttons.grid(column=1, row=0)

value_two = tk.StringVar()
frame_two_buttons_select = tk.OptionMenu(
    frame_two_buttons, value_two, *LANGCODES.keys())
frame_two_buttons_select.grid(column=0, row=0)

frame_two_buttons_copy = tk.Button(frame_two_buttons, text="copy translation", command=lambda: print(
    'clicked'), font=("sans-serif", 16), foreground='#1c2934')
frame_two_buttons_copy.grid(column=0, row=1)

root.mainloop()
