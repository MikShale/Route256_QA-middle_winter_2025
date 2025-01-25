import sys


letters = "abcdefghijklmnopqrstuvwxyz"
vowels_lower = "euioay"
vowels_upper = ''.join(x.upper() for x in vowels_lower)
vowels = vowels_lower + vowels_upper
consonant_lower = ''.join(x for x in letters if x not in vowels_lower)
consonant_upper = ''.join(x.upper() for x in consonant_lower)
consonant = consonant_lower + consonant_upper



def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x) + "\n")

'''
 хотя бы одну прописную букву (букву в верхнем регистре);
 хотя бы одну строчную букву (букву в нижнем регистре);
 хотя бы одну гласную букву;
 хотя бы одну согласную букву;
 хотя бы одну цифру.
 '''




def check_password(password):
    if not any(i in consonant for i in password):
        if not any(i.isupper() for i in password):
            password += consonant_upper[1]
        else:
            password += consonant_lower[1]

    if not any(i in vowels for i in password):
        if not any(i.isupper() for i in password):
            password += vowels_upper[1]
        else:
            password += vowels_lower[1]

    if not any(i.islower() for i in password): # есть ли в нижнем регистре
        password += consonant_lower[1] # добавляется маленькая согласная
    if not any(i.isdigit() for i in password): # есть ли цифра
        password += '1' # добавляется цифра
    if not any(i.isupper() for i in password): # есть ли заглавная буква
        password += consonant_upper[1] # добавляется согласная

    return password


def main():
    number_of_tests = int(fast_input())

    for test in range(number_of_tests):
        right_password = check_password(fast_input())
        fast_output(right_password)


if __name__ == "__main__":
    main()