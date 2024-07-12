import pytest

from service import calculate


def test_calculate_addition():
    assert calculate("1+2+3+4") == 10


def test_calculate_subtraction():
    assert calculate("10-1-2-3") == 4


def test_calculate_mixed_addition_subtraction():
    assert calculate("10+1-2+3") == 12


def test_calculate_single_number():
    assert calculate("5") == 5


def test_calculate_negative_result():
    assert calculate("2-3") == -1


def test_calculate_addition_and_negative():
    assert calculate("2+3-5") == 0


def test_calculate_with_leading_and_trailing_spaces():
    assert calculate(" 2+3-1 ") == 4


def test_calculate_with_multiple_digits():
    assert calculate("12+34-5") == 41


def test_calculate_with_large_numbers():
    assert calculate("1000+2000-300") == 2700


def test_calculate_with_complex_expression():
    assert calculate("10+20-30+40-50+60-70+80-90+100") == 70


def test_calculate_with_spaces_between_numbers_and_operators():
    assert calculate("2 + 3 - 1") == 4


def test_calculate_with_only_addition():
    assert calculate("2+3+4+5") == 14


def test_calculate_with_only_subtraction():
    assert calculate("10-3-2-1") == 4


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
