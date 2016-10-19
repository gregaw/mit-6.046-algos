import pytest

from algos.j_dynamic_palindrome import longest_palindromic_sequence


@pytest.mark.parametrize(
    "l,result", [
        ('', ''),
        ('a', 'a'),
        ('ab', 'a'),
        ('aba', 'aba'),
        ("character", 'carac'),
        ("charactercharacter", 'caractcarac'),
        ("character" * 100, 'caract' * 99 + 'carac'),
    ]
)
def test_longest_palindromic_sequence(l, result):
    assert longest_palindromic_sequence(l) == result
