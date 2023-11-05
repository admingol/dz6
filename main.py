result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або дорівнювати b")
        if b == 0:
            raise ZeroDivisionError("b не може бути нулем")
        if b > 100:
            raise IndexError("b не має бути більше 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)