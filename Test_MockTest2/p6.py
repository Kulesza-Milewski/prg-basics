import json

def f(years, course, average_grade):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            
        count = 0
        for student in data:
            if student.get("age") >= years:
                studies = student.get("studies", {}) 
                
                if course in studies:
                    grades = studies[course]
                    if isinstance(grades, (int, float)):
                        avg = grades
                    elif isinstance(grades, list):
                        avg = sum(grades) / len(grades)
                    else:
                        avg = 0
                        
                    if avg >= average_grade:
                        count += 1
        return count
    except FileNotFoundError:
        return 0

print(f(21, "statistics", 4))