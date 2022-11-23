from pororo import Pororo

class Summary:
    model = Pororo(task='summary', lang='ko')
    def __new__(cls, sent, **kwargs):
        return cls.model(sent, **kwargs)