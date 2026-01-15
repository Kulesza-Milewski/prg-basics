text = "I completely agree with you"
split_text = text.split()

calc = list(map(lambda x:len(x), split_text))

print(calc)