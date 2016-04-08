# pylint: disable=bad-whitespace, missing-docstring

"""Give me Diamond"""

from src.give_me_diamond import diamond


def test_simple_diamond():
    expected =  ' *\n'
    expected += '***\n'
    expected += ' *\n'
    assert diamond(3) == expected


def test_big_diamond():
    expected =  '  *\n'
    expected += ' ***\n'
    expected += '*****\n'
    expected += ' ***\n'
    expected += '  *\n'
    assert diamond(5) == expected

