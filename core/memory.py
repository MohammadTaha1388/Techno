class Memory:

    def __init__(self, max_items=100):
        self.max_items = max_items
        self.messages = []

    def add(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

        if len(self.messages) > self.max_items:
            self.messages.pop(0)

    def history(self):
        return self.messages

    def clear(self):
        self.messages.clear()

    def last(self):
        if self.messages:
            return self.messages[-1]
        return None

    def size(self):
        return len(self.messages)
