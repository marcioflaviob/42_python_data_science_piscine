import sys

from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = S.split()

        filtered = ft_filter(lambda w: len(w) > N, words)
        result = [word for word in filtered]
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

# def isEven(num):
#     return num % 2 == 0

# def main():
#     print(ft_filter.__doc__)
#     print(filter.__doc__)
#     # compare with real function filter
#     print(list(ft_filter(isEven, range(10))))
#     print(list(filter(isEven, range(10))))
#     print(list(ft_filter(None, ['', 'a', 0, 1, False, True])))
#     print(list(filter(None, ['', 'a', 0, 1, False, True])))

# if __name__ == "__main__":
#     main()
