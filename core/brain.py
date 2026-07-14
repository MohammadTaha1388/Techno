class TitanBrain:
    def __init__(self):
        self.memory = []

    def chat(self, message):
        self.memory.append(message)

        if len(self.memory) > 20:
            self.memory.pop(0)

        return f"You said: {message}"
