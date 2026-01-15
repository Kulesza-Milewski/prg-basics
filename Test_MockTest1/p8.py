def f(palindrom):
    odwrocony = "".join(reversed(palindrom))
    if odwrocony == palindrom:
        return True
    else:
        return False
    
print(f("12-11-21"))