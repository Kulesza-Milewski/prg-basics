import csv

def f(value):
    count = 0
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None) 
            
            for row in reader:
                for item in row:
                    try:
                        salary = float(item)
                        if salary >= value:
                            count += 1
                            break 
                    except ValueError:
                        continue
        return count
    except FileNotFoundError:
        return 0

print(f(9200))