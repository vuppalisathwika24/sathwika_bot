import ollama

MODEL = "llama3.2"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]


def main():
    print(f"Sathwika Bot ({MODEL}) — type 'quit' to exit")
    print("-" * 40)

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(model=MODEL, messages=messages)
        reply = response["message"]["content"]

        print(f"Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
