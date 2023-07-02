def func_verification_palindrom(p):
    new_p = ""
    for sym in reversed(p):
        new_p = new_p + sym
    if p == new_p:
        conclusion = True
    else:
        conclusion = False
    return conclusion

palindrom = input('Введите образец для проверки падижром или нет:')

print(func_verification_palindrom(palindrom))