#2020/12/28

def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]