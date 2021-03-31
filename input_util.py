def get_input_range(prompt, error_prompt, start, end):
    val = get_integer_input(prompt, error_prompt)   # Force them to enter an integer
    while val < start or val > end:
        print(error_prompt)
        val = get_integer_input(prompt, error_prompt)
    return val


def get_integer_input(prompt, error_prompt):
    while True:
        try:
            val = int(input(prompt))
            break
        except ValueError:
            print(error_prompt)
    return val


def get_float_input(prompt, error_prompt):
    while True:
        try:
            val = float(input(prompt))
            break
        except ValueError:
            print(error_prompt)
    return val