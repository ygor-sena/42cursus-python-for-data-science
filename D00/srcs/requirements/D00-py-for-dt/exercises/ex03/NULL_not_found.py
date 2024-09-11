def NULL_not_found(object: any) -> int:
    if object is None:
        print(f'Nothing: {object} {type(object)}')
    elif type(object) is float and object != object:
        print(f'Cheese: {object} {type(object)}')
    elif type(object) is int and object == 0:
        print(f'Zero: {object} {type(object)}')
    elif type(object) is str and not object:
        print(f'Empty: {object} {type(object)}')
    elif type(object) is bool and not object:
        print(f'Fake: {object} {type(object)}')
    else:
        print('Type not found')

    return 1
