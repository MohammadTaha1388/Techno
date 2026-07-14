from core.brain import TitanBrain

brain = TitanBrain()

print("🚀 Titan AI v0.1.0 Started")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    answer = brain.chat(user)
    print("Titan:", answer)
