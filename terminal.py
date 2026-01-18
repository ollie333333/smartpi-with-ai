from .ai import ask_model

def start_terminal_chat():
    print("=== SmartPi Local AI Chat ===")
    print("Type 'exit' or 'quit' to leave.\\n")
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        reply = ask_model(user_text)
        print("SmartPi:", reply)
        print()
