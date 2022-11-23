from pororo import Pororo

class SA:
    model = Pororo(task='sentiment', lang='ko')
    def __new__(cls, sent):
        prob = cls.model(sent, show_probs=True)
        return f"{prob['positive']}"