def f(subjects):
    best_avg = 0
    best_subject = ""
    
    for subject, grades in subjects.items():
        if len(grades) > 0:
            avg = sum(grades) / len(grades)
            if avg > best_avg:
                best_avg = avg
                best_subject = subject
                
    return best_subject


print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))