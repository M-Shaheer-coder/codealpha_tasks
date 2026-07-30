from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = source_lang.get()
    target = target_lang.get()

    # Language codes
    languages = {
        "English": "en",
        "Urdu": "ur",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Hindi": "hi",
        "Arabic": "ar",
        "Chinese": "zh-CN"
    }

    try:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- Main Window ---------------- #

window = Tk()
window.title("Language Translation Tool")
window.geometry("700x600")
window.configure(bg="white")

# Heading
heading = Label(
    window,
    text="Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="blue"
)
heading.pack(pady=15)

# Input Label
Label(
    window,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="white"
).pack()

# Input Text Box
input_text = Text(window, height=7, width=60, font=("Arial", 11))
input_text.pack(pady=10)

# Language Frame
frame = Frame(window, bg="white")
frame.pack()

# Source Language
Label(
    frame,
    text="Source Language",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=0, padx=20)

source_lang = ttk.Combobox(
    frame,
    values=[
        "English",
        "Urdu",
        "French",
        "Spanish",
        "German",
        "Hindi",
        "Arabic",
        "Chinese"
    ],
    state="readonly",
    width=18
)
source_lang.current(0)
source_lang.grid(row=1, column=0, padx=20)

# Target Language
Label(
    frame,
    text="Target Language",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=1, padx=20)

target_lang = ttk.Combobox(
    frame,
    values=[
        "English",
        "Urdu",
        "French",
        "Spanish",
        "German",
        "Hindi",
        "Arabic",
        "Chinese"
    ],
    state="readonly",
    width=18
)
target_lang.current(1)
target_lang.grid(row=1, column=1, padx=20)

# Translate Button
Button(
    window,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=translate_text
).pack(pady=20)

# Output Label
Label(
    window,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="white"
).pack()

# Output Text Box
output_text = Text(window, height=7, width=60, font=("Arial", 11))
output_text.pack(pady=10)

window.mainloop()
