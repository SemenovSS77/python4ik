import pytests
from main import linearize_recursive, linearize_iterative, sequence_recursive, sequence_iterative

# Тест для linearize_recursive
def test_linearize_recursive(capsys):
    # Вызываем функцию, которая печатает результат
    print(linearize_recursive([1, 2, [3, 4, [5, [6, []]]]]))
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "[1, 2, 3, 4, 5, 6]\n"  # Ожидаемый вывод
    assert captured.out == expected_output

# Тест для linearize_iterative
def test_linearize_iterative(capsys):
    # Вызываем функцию, которая печатает результат
    print(linearize_iterative([1, 2, [3, 4, [5, [6, []]]]]))
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "[1, 2, 3, 4, 5, 6]\n"  # Ожидаемый вывод
    assert captured.out == expected_output

# Тест для sequence_recursive
def test_sequence_recursive(capsys):
    # Вызываем функцию, которая печатает результат
    print(sequence_recursive(5))
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "(81, 81)\n"  # Ожидаемый вывод
    assert captured.out == expected_output

# Тест для sequence_iterative
def test_sequence_iterative(capsys):
    # Вызываем функцию, которая печатает результат
    print(sequence_iterative(5))
    captured = capsys.readouterr()  # Захватываем вывод
    expected_output = "(81, 81)\n"  # Ожидаемый вывод
    assert captured.out == expected_output