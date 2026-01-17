def f(files):
    # lambda x: x.split('.')[-1] bierze ostatni element po rozdzieleniu kropką
    # Przykład: "a.txt" -> "txt"
    return sorted(files, key=lambda x: x.split('.')[-1])