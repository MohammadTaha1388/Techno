class Reasoning:

    def think(self, message):

        text = message.lower()

        if "کد" in text:
            return "code"

        if "تصویر" in text:
            return "vision"

        if "برنامه" in text:
            return "planner"

        return "chat"
