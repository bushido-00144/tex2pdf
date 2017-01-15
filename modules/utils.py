import string
import random

def randomStr(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
