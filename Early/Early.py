from .Configuration import Configuration
from .Grammar.Grammar import Grammar
from typing import List, NoReturn, Set
from copy import deepcopy


def check_conf_for_predict(conf) -> bool:
    if conf.finish[-1] == '.':
        return False
    return conf.finish[conf.finish.index('.') + 1].isupper()


def check_conf_for_scan(conf: Configuration) -> bool:
    if conf.finish[-1] == '.':
        return False
    return conf.finish[conf.finish.index('.') + 1].islower()


def check_conf_for_complete(conf):
    return conf.finish[-1] == '.'


def scan(conf_list: Set[Configuration], conf_list_next: Set[Configuration], word: str, j: int) -> NoReturn:
    assert j > 0
    for conf in conf_list:
        if check_conf_for_scan(conf):
            dot_index = conf.finish.index('.')
            if conf.finish[dot_index + 1] == word[j - 1]:
                new_conf_finish = conf.finish[:dot_index] + conf.finish[dot_index + 1]\
                                  + '.' + conf.finish[dot_index + 2:]
                conf_list_next.add(Configuration(conf.start, new_conf_finish, conf.i))


def predict(conf_list: Set[Configuration], grammar: Grammar, j: int):
    to_add = set()
    for conf in conf_list:
        if check_conf_for_predict(conf):
            dot_index = conf.finish.index('.')
            for letter, finish_set in grammar.rules.items():
                if letter == conf.finish[dot_index + 1]:
                    for finish in finish_set:
                        to_add.add(Configuration(letter, '.' + finish, j))
    for item in to_add:
        conf_list.add(item)


def complete(conf_list_storage: List[Set[Configuration]], j: int):
    to_add = set()
    for conf_low in conf_list_storage[j]:
        if check_conf_for_complete(conf_low):
            for conf_up in conf_list_storage[conf_low.i]:
                if check_conf_for_predict(conf_up):
                    dot_index = conf_up.finish.index('.')
                    if conf_low.start == conf_up.finish[dot_index + 1]:
                        new_conf_up_finish = conf_up.finish[:dot_index] + conf_up.finish[dot_index + 1] +\
                                             '.' + conf_up.finish[dot_index + 2:]
                        to_add.add(Configuration(conf_up.start, new_conf_up_finish, conf_up.i))
    for item in to_add:
        conf_list_storage[j].add(item)


class Early:
    grammar: Grammar
    word: str
    conf_list_storage: List[Set[Configuration]]

    def __init__(self, gr: Grammar, word: str):
        self.grammar = Grammar()
        self.grammar.rules = deepcopy(gr.rules)
        self.grammar.start_letter = deepcopy(gr.start_letter)
        self.word = word
        assert 'Z' not in self.grammar.rules.keys()
        self.grammar.add_rule('Z', self.grammar.start_letter)
        self.conf_list_storage = [set() for i in range(len(word) + 1)]

    def process_word(self) -> bool:
        self.conf_list_storage[0].add(Configuration('Z', '.{}'.format(self.grammar.start_letter), 0))
        self.build_conf_list()
        return Configuration('Z', '{}.'.format(self.grammar.start_letter), 0) in self.conf_list_storage[len(self.word)]

    def build_conf_list(self) -> NoReturn:
        for j in range(len(self.word) + 1):
            if j > 0:
                scan(self.conf_list_storage[j - 1], self.conf_list_storage[j], self.word, j)
            while True:
                old_size = len(self.conf_list_storage[j])
                complete(self.conf_list_storage, j)
                predict(self.conf_list_storage[j], self.grammar, j)
                if len(self.conf_list_storage[j]) == old_size:
                    break
        pass

