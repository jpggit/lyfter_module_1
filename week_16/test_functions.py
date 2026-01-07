import pytest
from functions import (
    addition, 
    reverse, 
    counter, 
    alpha_organizer, 
    prime_checker)


# ---------- addition ----------
def test_addition_with_positive_numbers():
    # Arrange
    numbers = [1, 2, 3, 4]
    expected = 10

    # Act
    result = addition(numbers)

    # Assert
    assert result == expected


def test_addition_with_negative_numbers():
    # Arrange
    numbers = [-1, -2, -3]
    expected = -6

    # Act
    result = addition(numbers)

    # Assert
    assert result == expected


def test_addition_with_empty_list():
    # Arrange
    numbers = []
    expected = 0

    # Act
    result = addition(numbers)

    # Assert
    assert result == expected


# ---------- reverse ----------
def test_reverse_simple_string():
    # Arrange
    text = "hello"
    expected = "olleh"

    # Act
    result = reverse(text)

    # Assert
    assert result == expected


def test_reverse_empty_string():
    # Arrange
    text = ""
    expected = ""

    # Act
    result = reverse(text)

    # Assert
    assert result == expected


def test_reverse_palindrome():
    # Arrange
    text = "tacocat"
    expected = "tacocat"

    # Act
    result = reverse(text)

    # Assert
    assert result == expected


# ---------- counter ----------
### Usamos capsys para capturar cosas que se imprimen cuando no hay un output real de la función

def test_counter_mixed_case(capsys):
    # Arrange
    text = "May the Force be with you"

    # Act
    counter(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "There’s 2 upper cases and 18 lower cases\n"
    assert captured.out == expected_output



def test_counter_no_letters(capsys):
    # Arrange
    text = "1234 !!!"

    # Act
    counter(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "There’s 0 upper cases and 0 lower cases\n"
    assert captured.out == expected_output


def test_counter_all_upper(capsys):
    # Arrange
    text = "ABC"

    # Act
    counter(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "There’s 3 upper cases and 0 lower cases\n"
    assert captured.out == expected_output


# ---------- alpha_organizer (capsys otra vez)----------

def test_alpha_organizer_example_text(capsys):
    # Arrange
    text = "python-variable-funcion-computadora-monitor"

    # Act
    alpha_organizer(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "computadora-funcion-monitor-python-variable\n"
    assert captured.out == expected_output


def test_alpha_organizer_two_words(capsys):
    # Arrange
    text = "banana-apple"

    # Act
    alpha_organizer(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "apple-banana\n"
    assert captured.out == expected_output


def test_alpha_organizer_single_word(capsys):
    # Arrange
    text = "python"

    # Act
    alpha_organizer(text)
    captured = capsys.readouterr()

    # Assert
    expected_output = "python\n"
    assert captured.out == expected_output


# ---------- prime_checker (capsys otra vez) ----------

def test_prime_checker_mixed_numbers(capsys):
    # Arrange
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Act
    prime_checker(numbers)
    captured = capsys.readouterr()

    # Assert
    expected_output = "[3, 5, 7]\n"
    assert captured.out == expected_output


def test_prime_checker_only_primes_over_two(capsys):
    # Arrange
    numbers = [11, 12, 13, 14, 15]

    # Act
    prime_checker(numbers)
    captured = capsys.readouterr()

    # Assert
    expected_output = "[11, 13]\n"
    assert captured.out == expected_output


def test_prime_checker_no_primes(capsys):
    # Arrange
    numbers = [0, 1, 2, 4, 6, 8, 9]

    # Act
    prime_checker(numbers)
    captured = capsys.readouterr()

    # Assert
    expected_output = "[]\n"
    assert captured.out == expected_output