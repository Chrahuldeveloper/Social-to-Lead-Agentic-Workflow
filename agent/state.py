class AgentState:
    def __init__(self, question):
        self.question = question
        self.intent = None
        self.context = None
        self.answer = None
