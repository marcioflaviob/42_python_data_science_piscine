import sys


def main():
    if len(sys.argv) == 1:
        print("What is the text to count?")
        string = sys.stdin.read()
    elif sys.argv.__len__() > 2:
        raise AssertionError("more than one argument is provided")
    elif sys.argv.__len__() == 2:
        string = sys.argv[1]
    print(f"The text contains {len(string)} characters:")
    print(f"{sum(1 for c in string if c.isupper())} upper letters")
    print(f"{sum(1 for c in string if c.islower())} lower letters")
    print(f"{sum(1 for c in string
                 if c in
                 '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')} punctuation marks")
    print(f"{sum(1 for c in string if c.isspace())} spaces")
    print(f"{sum(1 for c in string if c.isdigit())} digits")


if __name__ == "__main__":
    main()
