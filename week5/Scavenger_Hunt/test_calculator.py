from calculator import *

try:
    # your code here
    assert add(1, 2) == 3
    assert subtract(8, 4) == 4
    assert multiply(2, 3) == 6
    assert divide(6, 3) == 2
    assert divide(2, 0) == "Error: Division by zero"
    print("All tests passed!")
except AssertionError as e:
    print(e)