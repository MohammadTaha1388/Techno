from core.memory import Memory
from core.router import Router
from core.reasoning import Reasoning
from core.planner import Planner


class TitanBrain:

    def __init__(self):

        self.memory = Memory()

        self.router = Router()

        self.reasoning = Reasoning()

        self.planner = Planner()

    def chat(self, message):

        self.memory.add("user", message)

        task = self.reasoning.think(message)

        model = self.router.get_model(task)

        answer = f"[{model.upper()}] در حال پردازش: {message}"

        self.memory.add("assistant", answer)

        return answer
