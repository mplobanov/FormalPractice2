from Early.Configuration import Configuration
from Grammar import Grammar

g = Grammar()

g.add_rule('S', 'Tbc')
g.add_rule('S', 'c')

g.add_rule('T', 'Sb')
g.add_rule('T', 'a')

g.add_rule('S', 'aUba')
g.add_rule('S', 'b')

g.add_rule('U', 'cS')
g.add_rule('U', 'e')