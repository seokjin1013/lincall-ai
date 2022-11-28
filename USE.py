import tensorflow_hub as hub
import tensorflow_text
import numpy as np
from json import JSONEncoder

class USE:
    with open('./USE_questions.txt', encoding='utf-8') as f:
        questions = f.readlines()
    with open('./USE_answers.txt', encoding='utf-8') as f:
        answers = f.readlines()
    embed = hub.KerasLayer('USE_model')
    embedded_vectors = embed(questions)
    encoder = JSONEncoder()

    def metric(u, v):
        return np.clip(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)), -1, 1)

    def __new__(cls, q):
        q_embed = cls.embed(q)
        q_cosine = np.array([cls.metric(e1, q_embed[0]) for e1 in cls.embedded_vectors])
        return cls.questions[q_cosine.argmax()] + '|' + cls.answers[q_cosine.argmax()]