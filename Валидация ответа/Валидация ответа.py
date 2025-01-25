import sys
import re

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x) + "\n")


def validate_output(count_of_elements, input_data, output_data):

    for data in [input_data, output_data]:
        if "  " in data or "_" in data:
            return "no"


    try:
        input_list = list(map(int, input_data.split()))
        output_list = list(map(int, output_data.split()))
    except ValueError:
        return "no"

    for s in input_list + output_list:
        s = str(s)  # Преобразуем в строку для проверки
        if not bool(re.match(r"^-?\d+$", s)) or "_" in s:
            return "no"
        elif s.lstrip("-").startswith("0") and len(s.lstrip("-")) > 1:  # Лидирующий ноль
            return "no"

    if len(output_list) != count_of_elements:
        return "no"

    if output_list != sorted(input_list):
        return "no"

    return "yes"



def main():
    number_of_tests = int(fast_input())
    for test in range(number_of_tests):

        count_of_elements = int(fast_input())
        input_data = fast_input()  # Входные данные
        output_data = fast_input()  # Выходные данные
        result = validate_output(count_of_elements, input_data, output_data)
        fast_output(result)


if __name__ == "__main__":
    main()