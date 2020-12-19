from typing import Dict, List


# in Grammar rules:
# non terminals - big letters   - S, U, V, T...
#     terminals - small letters - a, b, c, d...
#     terminals - e for epsilon

class Grammar:
    start_letter = 'S'
    rules: Dict[str, List[str]] = dict()

    def __init__(self):
        self.rules = dict()

    def add_rule(self, start: str, finish: str):
        assert start.isalpha() and start.isupper()
        assert finish.isalpha()
        if start in self.rules:
            self.rules[start].append(finish)
        else:
            self.rules[start] = [finish]

