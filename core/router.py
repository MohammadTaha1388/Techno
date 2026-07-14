class Router:

    def __init__(self):
        self.models = {
            "chat": "qwen",
            "code": "deepseek",
            "vision": "llama",
            "reasoning": "mistral"
        }

    def get_model(self, task):
        return self.models.get(task, "qwen")
