import pytest
from bubble_algo import bubble_sort

def test_bubble_sort_small_list():
    # Arrange
    data = [3, 1, 2]
    expected = [1, 2, 3]

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected


def test_bubble_sort_large_list():
    # Arrange
    data = list(range(200, 0, -1))
    expected = list(range(1, 201))

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected


def test_bubble_sort_empty_list():
    # Arrange
    data = []
    expected = []

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected


def test_bubble_sort_non_list():
    # Arrange
    bad_input = 123

    # Act / Assert
    with pytest.raises(TypeError):
        bubble_sort(bad_input)