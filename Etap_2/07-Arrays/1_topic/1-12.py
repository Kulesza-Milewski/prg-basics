categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

top_expencive = max(expenses)

index_of_top = expenses.index(top_expencive)

top_category = categories[index_of_top]

print(top_category,":",top_expencive,"zl")