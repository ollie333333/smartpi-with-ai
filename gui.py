import tkinter as tk
from .ai import ask_model

def run_gui():
    ai = ask_model
    def send_message():
        txt = user_input.get().strip()
        if not txt:
            return
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"You: {txt}\\n")
        reply = ai(txt)
        chat_box.insert(tk.END, f"SmartPi: {reply}\\n\\n")
        chat_box.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)

    root = tk.Tk()
    root.title("SmartPi Chat")
    root.geometry("600x500")
    chat_box = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
    chat_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    user_input = tk.Entry(root, font=("Arial", 14))
    user_input.pack(fill=tk.X, padx=10, pady=(0,10))
    user_input.bind("<Return>", lambda e: send_message())
    tk.Button(root, text="Send", command=send_message).pack()
    root.mainloop()
