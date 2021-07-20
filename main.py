# main.py
def print_message(message: str, symbol: str = "*", length: int = 64) -> None:

    full_symbols = symbol * length
    start_end_symbols = symbol.ljust(length - 1) + symbol

    center = int(length / 2) - int(len(message) / 2)
    punchline = symbol.ljust(center - len(message) % 2) + message + symbol.rjust(center)

    to_print = [
        full_symbols,
        start_end_symbols,
        punchline,
        start_end_symbols,
        full_symbols,
    ]

    for v in to_print:
        print(v)


if __name__ == "__main__":
    print_message(">>> From DMTX with luv. <<<", "*", 120)
    input()
