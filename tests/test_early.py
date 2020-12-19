from ..Early.Eaerly import *
from ..Early.Configuration import Configuration
from ..Grammar import Grammar


def test_scan_ordinary():
    word = 'abc'
    conf_list_storage = [set(), set()]
    conf_list_storage[0].add(Configuration('S', '.abc', 0))
    scan(conf_list_storage[0], conf_list_storage[1], word, 1)

    assert conf_list_storage[1] == {Configuration('S', 'a.bc', 0)}


def test_scan_unsuitable():
    word = 'abc'
    conf_list_storage = [set(), set()]
    conf_list_storage[0].add(Configuration('S', '.Ubc', 0))
    scan(conf_list_storage[0], conf_list_storage[1], word, 1)

    assert conf_list_storage[1] == set()


def test__check_conf_for_predict():
    assert check_conf_for_predict(Configuration('S', 'ab.S', 0))
    assert not check_conf_for_predict(Configuration('S', 'a.ab', 0))
    assert not check_conf_for_predict(Configuration('S', 'abc.', 0))


def test__check_conf_for_scan():
    assert check_conf_for_scan(Configuration('S', 'ab.a', 0))
    assert not check_conf_for_scan(Configuration('S', 'a.Sb', 0))
    assert not check_conf_for_scan(Configuration('S', 'abc.', 0))


def test_predict():
    grammar = Grammar()
    grammar.add_rule('U', 'xyz')
    conf_list_storage = [set()]
    conf_list_storage[0].add(Configuration('S', '.Ubc', 0))

    predict(conf_list_storage[0], grammar, 0)

    assert conf_list_storage[0] == {Configuration('S', '.Ubc', 0), Configuration('U', '.xyz', 0)}


def test_complete():
    conf_list_storage = [
        {Configuration('A', 'ab.Bcd', 2)},
        {Configuration('B', 'abT.', 0)}
    ]

    complete(conf_list_storage, 1)

    assert conf_list_storage[1] == {Configuration('B', 'abT.', 0), Configuration('A', 'abB.cd', 2)}


def test_complete_unsuatable():
    conf_list_storage = [
        {Configuration('A', 'ab.Ccd', 2)},
        {Configuration('B', 'ab.T', 0)}
    ]

    complete(conf_list_storage, 1)

    assert conf_list_storage[1] == {Configuration('B', 'ab.T', 0)}


def test_whole():
    grammar = Grammar()
    grammar.add_rule('S', 'aTb')
    grammar.add_rule('T', 'bba')

    assert Early(grammar, 'abbab').process_word()
    assert not Early(grammar, 'abab').process_word()
