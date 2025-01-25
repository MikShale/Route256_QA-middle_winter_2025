import sys


def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x) + "\n")


def find_max_salary():
    number_of_tests = int(fast_input())

    for test in range(number_of_tests):
        salary = fast_input()
        if len(salary) == 1: # если строка состоит всего из 1 элемента
            fast_output(0)   # выводи 0
            continue
        elif salary == salary[0] * len(salary): # если все элементы в строке одинаковые
            fast_output(salary[1:])           # удаляй 1 и выводи
            continue

        for s in range(len(salary)-1):

            if salary[s] == salary[s + 1] and s + 2 < len(salary):  # если элементы равны и существует третий
                continue

            elif salary[s+1] > salary[s]: #если второй больше первого - удаляй первый
                fast_output(salary[:s] + salary[s+1:])
                break

            elif salary[s] > salary[s+1] and s + 2 < len(salary): #если второй меньше первого и существует 3
                continue
            else:
                fast_output(salary[:s+1] + salary[s + 2:]) #удаляй второй
                break




if __name__ == '__main__':


    find_max_salary()