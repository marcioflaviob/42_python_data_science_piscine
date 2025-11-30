import sys


def main(number):
    try:
        converted_number = int(number)
    except ValueError:
        raise AssertionError("argument is not an integer")
    if converted_number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        if sys.argv.__len__() > 2:
            raise AssertionError("more than one argument is provided")
        elif sys.argv.__len__() == 2:
            main(sys.argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
