from Early.Early import *
from Early.Grammar import Grammar


class Algo:
    algo: Early
    grammar: Grammar

    def __init__(self):
        pass

    def fit(self, gr: Grammar):
        self.grammar = gr

    def predict(self, word: str):
        return Early(self.grammar, word).process_word()