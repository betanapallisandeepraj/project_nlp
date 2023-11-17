import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

def lookup_word():
    word = entry.get()
    dictionary = PyDictionary()

    try:
        meaning = dictionary.meaning(word)
        if meaning:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Meaning of '{word}':\n")
            for part_of_speech, definitions in meaning.items():
                result_text.insert(tk.END, "Meaning of '{}':\n".format(word))
            result_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("No Result", f"No meaning found for '{word}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Simple Dictionary")

# Create and place widgets
label = tk.Label(root, text="Enter a word:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=lookup_word)
search_button.pack(pady=10)

result_text = tk.Text(root, width=40, height=10, state=tk.DISABLED)
result_text.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

