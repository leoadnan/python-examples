def print_hello_world_twice():
    print("Hello World1")
    print("Hello World2")


def print_hello_world_multiple_times(times):
    for i in range(1, times+1):
        print("Hello World")


def print_squares_of_numbers_upto(times):
    for i in range(1, times+1):
        print(i*i)


def print_squares_of_even_numbers_upto(times):
    for i in range(2, times+1, 2):
        print(i*i)


def print_numbers_in_reverse(times):
    for i in range(times, 0, -1):
        print(i)


def print_multiplication_table(table=5, start=1, end=10):
    for i in range (start, end+1,):
        print(f"{table} x {i} = {table*i}")


print_multiplication_table()
print_multiplication_table(2, 1, 10)