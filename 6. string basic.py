#2020/12/03

def solution(s):
    if (len(s) == 4 or len(s) ==6) and s.isdigit():
        return True
    else : 
      return False

def solution2(s):
    return s.isdigit() and len(s) in (4, 6)