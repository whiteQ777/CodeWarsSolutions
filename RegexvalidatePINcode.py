import re
def validate_pin(pin):
    #return true or false
    flag = True
    pattern1 = re.compile(r'\d{4}')
    pattern2 = re.compile(r'\d{6}')
    if len(pin) == 4 and pattern1.match(pin) is None:
        flag = False
    if len(pin) == 6 and pattern2.match(pin) is None:
        flag = False
    if len(pin) not in [4,6]:
        flag = False
    return flag
      