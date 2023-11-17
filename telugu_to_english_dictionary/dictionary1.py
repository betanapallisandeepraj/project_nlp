import tkinter as tk
from tkinter import messagebox

# Replace this with your actual dataset of English to Telugu words and meanings
english_to_telugu_dict = {
    "hello": "హలో",
    "world": "ప్రపంచం",
    "python": "పైథాన్"
}

def lookup_word():
    word = entry.get().lower()

    try:
        telugu_meaning = english_to_telugu_dict.get(word)
        if telugu_meaning:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Meaning of '{word}': {telugu_meaning}")
            result_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("No Result", f"No meaning found for '{word}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("English to Telugu Dictionary")

# Create and place widgets
label = tk.Label(root, text="Enter an English word:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=lookup_word)
search_button.pack(pady=10)

result_text = tk.Text(root, width=40, height=10, state=tk.DISABLED)
result_text.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

