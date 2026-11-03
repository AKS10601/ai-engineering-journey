import requests

URL = "http://localhost:11434/api/chat"
MODEL = "gemma4:12b"

messages = []  # conversation history

print("Chat with your local model. Type 'quit' to exit.\n")
while True:
    user = input("You: ")
    if user.lower() == "quit":
        break
    messages.append({"role": "user", "content": user})

    r = requests.post(URL, json={"model": MODEL, "messages": messages, "stream": False})
    reply = r.json()["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    print(f"\nAI: {reply}\n")
