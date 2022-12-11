def switch_case_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(switch_case_dict('mul', 2, 8))

print(switch_case_dict('unknown', 2, 8))