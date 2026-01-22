import re

def f(array):
    count = 0
    pattern = r"^[a-z0-9_]{4,12}$"
    
    for username in array:
        if re.match(pattern, username):
            count += 1
    return count

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))