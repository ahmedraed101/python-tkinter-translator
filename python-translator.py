from langfunc import detect_lang, translate
from googletrans import Translator
from googletrans import LANGCODES, LANGUAGES
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


t = Translator()


def trans_command():
    text = input_text.get("1.0", tk.END)
    translated_text = translate(
        t, text.strip(), LANGCODES[src_lang.get()], LANGCODES[dest_lang.get()]
    )
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.INSERT, translated_text)
    output_text.config(state=tk.DISABLED)


def copy_func():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))


# root
root = tk.Tk()
root.minsize("700", "700")
root.configure(bg="#1c2934")
root.title("translator")

header = tk.Label(
    root, text="Translate any thing you need",
    bg="#03FDD7", fg="black", font=("sans-serif", 16)
)
header.grid(ipady=5, ipadx=5, pady=20)

#
# frame one
#
frame_one = tk.Frame(root, bg="#1c2934")
frame_one.grid(padx=10)

# src lang label
src_lang_label = tk.Label(
    frame_one, text="FROM: ",
    bg="#1c2934", fg="white", font=("sans-serif", 16))
src_lang_label.grid(column=0, row=0, padx=5)

# src langauage select box
src_lang = tk.StringVar()
src_lang.set(LANGUAGES["en"])
src_language_select = tk.OptionMenu(
    frame_one,
    src_lang,
    *LANGCODES.keys()
)
src_language_select.config(font=("sans-serif", 16), width=20)
src_language_select.grid(column=1, row=0)

# dest lang label
dest_lang_label = tk.Label(
    frame_one, text="TO: ",
    bg="#1c2934", fg="white", font=("sans-serif", 16)
)
dest_lang_label.grid(column=2, row=0, padx=5)

# dest langauge select
dest_lang = tk.StringVar()
dest_lang.set(LANGUAGES["en"])
dest_language_select = tk.OptionMenu(
    frame_one,
    dest_lang,
    *LANGCODES.keys()
)
dest_language_select.config(font=("sans-serif", 16), width=20)
dest_language_select.grid(column=3, row=0)

# input frame
input_frame = tk.Frame(root, bg="#1c2934")
input_frame.grid()

# input scrolledtext
input_text = ScrolledText(
    input_frame, width=50, height=6,
    padx=20, pady=20, selectbackground="#3FA074", selectforeground="#F8EDFD"
)
input_text.config(font=("sans-serif", 18), bg="#E6F9F6", fg="black")
input_text.grid(column=0, row=1, columnspan=2, pady=15)

# detect langauage button
detect_language_button = tk.Button(
    input_frame,
    text="detect language",
    command=lambda: src_lang.set(
        LANGUAGES[detect_lang(t, input_text.get("1.0", tk.END))]),
    font=("sans-serif", 16),
    foreground='#05B281',
    width=20
)
detect_language_button.grid(column=0, row=2)

# clear button
clear_button = tk.Button(
    input_frame,
    text="Clear",
    command=lambda: input_text.delete("1.0", tk.END),
    font=('sans-serif', 16),
    foreground="#D20E5C",
    width=20
)
clear_button.grid(column=1, row=2)

# translate button
translate_button = tk.Button(
    input_frame,
    text="Translate",
    command=trans_command,
    font=('sans-serif', 16),
    foreground="#0563B2",
    width=50
)
translate_button.grid(column=0, row=3, pady=10, columnspan=2)

#
# frame two
#
frame_two = tk.Frame(root, bg="#1c2934")
frame_two.grid(pady=20)

# output scrolledtext
output_text = ScrolledText(
    frame_two, width=50, height=6,
    padx=20, pady=20, selectbackground="#3FA074", selectforeground="#F8EDFD",
    state=tk.DISABLED
)
output_text.config(font=("sans-serif", 18), bg="#1c2934", fg="white")
output_text.grid(column=0, row=1, columnspan=2, pady=15)

# copy button
copy_button = tk.Button(
    frame_two, text="Copy",
    command=copy_func,
    font=('sans-serif', 16),
    foreground="#07888E",
    width=40
)
copy_button.grid(column=0, row=2)

root.resizable(0, 0)

root.mainloop()
