import pytests
from main import apply_n_times, filter_changed, square

def test_filter_changed(capsys):
    numbers = [5, 3, 4, 1, 2]
    n = 2
    
    result_generator = filter_changed(numbers, square, n)
    out_filter = filter(lambda x: x > 15, result_generator) #фильтр
    sorted_result = list(out_filter)
    print(sorted_result)
    captured = capsys.readouterr()
    expected_output = "[625, 81, 256]\n"
    assert captured.out == expected_output
