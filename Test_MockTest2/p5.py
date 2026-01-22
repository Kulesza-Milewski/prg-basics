def f(first_letter, last_letter):
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            count = 0
            for word in words:
                clean_word = word.strip(".,!?;:")
                if clean_word and clean_word.startswith(first_letter) and clean_word.endswith(last_letter):
                    count += 1
            return count
    except FileNotFoundError:
        return 0

print(f("w", "d"))