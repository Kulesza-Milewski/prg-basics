import re

def f(dates):
    # Używamy wyrażenia regularnego (Regex)
    # \d{4} - cztery cyfry (rok)
    # - myślnik
    # \d{2} - dwie cyfry (miesiąc)
    # - myślnik
    # \d{2} - dwie cyfry (dzień)
    # findall zwróci listę wszystkich dopasowań
    return re.findall(r"\d{4}-\d{2}-\d{2}", dates)