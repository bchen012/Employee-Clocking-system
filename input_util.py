def get_input_range(promt, start, end):
    val = int(input(promt))
    while val < start or val > end:
        val = int(input("Please enter a number between " + str(start) + " and " + str(end) + ":"))
    return str(val)