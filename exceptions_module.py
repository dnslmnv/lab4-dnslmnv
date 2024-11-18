# Пользовательские исключения (Шаг 6)
class NegativeValueError(Exception):
    """Ошибка: отрицательное значение"""
    pass

class DivisionByZeroError(Exception):
    """Ошибка: деление на ноль"""
    pass

class CustomRangeError(Exception):
    """Ошибка: значение не попадает в диапазон"""
    pass

# Функции, соответствующие шагам

# Шаг 1: Функции без обработчиков исключений
def function1(param1):
    """Шаг 1: Выбрасывает исключение при отрицательном значении"""
    if param1 < 0:
        raise NegativeValueError("Parameter cannot be negative.")
    return param1 ** 2

def function2(param1, param2):
    """Шаг 1: Выбрасывает исключение при делении на ноль"""
    if param2 == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    return param1 / param2

# Шаг 2: Функция с обработчиком общего типа
def function3(param1):
    """Шаг 2: Обрабатывает общее исключение"""
    try:
        if param1 > 100:
            raise CustomRangeError("Parameter exceeds the allowed range.")
        return param1 * 10
    except Exception as e:
        print(f"Handled exception: {e}")

# Шаг 3: Функция с обработчиком и finally
def function4(param1):
    """Шаг 3: Обрабатывает общее исключение с finally"""
    try:
        if param1 < 0:
            raise NegativeValueError("Parameter cannot be negative.")
        return param1 ** 0.5
    except Exception as e:
        print(f"Handled exception: {e}")
    finally:
        print("Execution completed.")

# Шаг 4: Функции с обработкой нескольких типов исключений
def function5(param1):
    """Шаг 4: Обрабатывает несколько типов исключений"""
    try:
        if param1 < 0:
            raise NegativeValueError("Negative value.")
        if param1 == 0:
            raise DivisionByZeroError("Division by zero.")
        if param1 > 100:
            raise CustomRangeError("Value exceeds range.")
        return 100 / param1
    except NegativeValueError as e:
        print(f"Handled NegativeValueError: {e}")
    except DivisionByZeroError as e:
        print(f"Handled DivisionByZeroError: {e}")
    except CustomRangeError as e:
        print(f"Handled CustomRangeError: {e}")
    finally:
        print("Function 5 execution completed.")

def function6(param1):
    """Шаг 4: Обрабатывает несколько исключений с различной логикой"""
    try:
        if not isinstance(param1, int):
            raise TypeError("Expected an integer.")
        if param1 < 10:
            raise ValueError("Value too small.")
        return param1 * 2
    except TypeError as e:
        print(f"Handled TypeError: {e}")
    except ValueError as e:
        print(f"Handled ValueError: {e}")
    finally:
        print("Function 6 execution completed.")

def function7(param1):
    """Шаг 4: Проверка на длину строки"""
    try:
        if len(param1) > 10:
            raise CustomRangeError("String is too long.")
        return param1.upper()
    except CustomRangeError as e:
        print(f"Handled CustomRangeError: {e}")
    finally:
        print("Function 7 execution completed.")

# Шаг 5: Генерация исключений и их обработка
def function8(param1):
    """Шаг 5: Генерация и обработка исключений"""
    try:
        if param1 == 0:
            raise ValueError("Parameter cannot be zero.")
        elif param1 < 0:
            raise NegativeValueError("Negative parameter.")
        return 10 / param1
    except ValueError as e:
        print(f"Handled ValueError: {e}")
    except NegativeValueError as e:
        print(f"Handled NegativeValueError: {e}")
    finally:
        print("Function 8 execution completed.")

# Шаг 7: Использование пользовательского исключения
def function9(param1):
    """Шаг 7: Выбрасывает пользовательское исключение"""
    try:
        if param1 < 0 or param1 > 50:
            raise CustomRangeError("Parameter is out of range.")
        return f"Parameter {param1} is valid."
    except CustomRangeError as e:
        print(f"Handled CustomRangeError: {e}")
    finally:
        print("Function 9 execution completed.")

# Шаг 8: Дополнительные функции для демонстрации исключений
def demo_function1(param1):
    """Демонстрирует обработку деления на ноль"""
    try:
        return 10 / param1
    except ZeroDivisionError:
        return "Cannot divide by zero."

def demo_function2(param1):
    """Демонстрирует обработку преобразования типов"""
    try:
        return int(param1)
    except ValueError:
        return "Invalid integer conversion."

def demo_function3(param1):
    """Демонстрирует обработку индексации"""
    try:
        return param1[10]
    except IndexError:
        return "Index out of range."
