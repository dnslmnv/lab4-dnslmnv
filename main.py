
from exceptions_module import (
    function1, function2, function3, function4, function5,
    function6, function7, function8, function9,
    demo_function1, demo_function2, demo_function3
)

def call_all_functions():
    """Шаг 9: Последовательный вызов всех функций"""
    print(function1(5))  # Шаг 1
    try:
        print(function2(10, 0))  # Шаг 1
    except Exception as e:
        print(f"Caught exception: {e}")

    function3(150)  # Шаг 2
    function4(-5)  # Шаг 3
    function5(0)  # Шаг 4
    function6("abc")  # Шаг 4
    function7("This is a long string")  # Шаг 4
    function8(0)  # Шаг 5
    function9(60)  # Шаг 7

    print(demo_function1(0))  # Шаг 8
    print(demo_function2("abc"))  # Шаг 8
    print(demo_function3("short"))  # Шаг 8

if __name__ == "__main__":
    call_all_functions()
