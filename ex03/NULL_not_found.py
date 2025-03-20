# python_piscine/ex03/NULL_not_found.py
def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) == float and object != object:  # Проверка NaN
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) == int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) == str and object == "":
        print(f"Empty: {type(object)}")
        return 0
    elif type(object) == bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
