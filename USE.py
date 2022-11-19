import tensorflow_hub as hub
import tensorflow_text
import numpy as np

class USE:
    with open('./USE_questions.txt', encoding='utf-8') as f:
        questions = f.readlines()
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")
    embedded_vectors = embed(questions)

    def metric(u, v):
        return np.clip(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)), -1, 1)

    def __new__(cls, q):
        q_embed = cls.embed(q)
        q_cosine = np.array([cls.metric(e1, q_embed[0]) for e1 in cls.embedded_vectors])
        return cls.questions[q_cosine.argmax()]