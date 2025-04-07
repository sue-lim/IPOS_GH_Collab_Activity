def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    result = a - b  # <--- fix this here for subtract
    print(f"subtract({a}, {b}) = {result}") # print for debugging
    return result


# uncomment the following test in step 5
def test_subtract():
   assert subtract(2, 3) == -1

# call subtract for different print results
subtract(2, 3) # output -1
subtract(5, 6) # output -1
subtract(10, 4) # output 6
subtract(20, 15) # output 5


# invoke pytest with "python -m pytest"