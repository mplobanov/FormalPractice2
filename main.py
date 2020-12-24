from Algo import Algo
from Early.Grammar.Grammar import Grammar

g = Grammar()

g.add_rule('S', 'Tbc')
g.add_rule('S', 'c')

g.add_rule('T', 'Sb')
g.add_rule('T', 'a')

g.add_rule('S', 'aUba')
g.add_rule('S', 'b')

g.add_rule('U', 'cS')
g.add_rule('U', '')

algo = Algo()
algo.fit(g)

w1 = 'accbabbc'
print(w1, algo.predict(w1))
w2 = 'a'
print(w2, algo.predict(w2))
w3 = 'abcbbcba'
print(w3, algo.predict(w2))
