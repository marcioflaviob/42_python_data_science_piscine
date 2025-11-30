from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    if not args:
        for _ in kwargs:
            print("ERROR")
        return

    data = sorted(args)
    n = len(data)

    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(data) / n
            print(f"mean : {mean}")
        elif value == "median":
            if n % 2 == 0:
                median = (data[n // 2 - 1] + data[n // 2]) / 2
            else:
                median = data[n // 2]
            print(f"median : {median}")
        elif value == "quartile":
            q1_pos = (n - 1) * 0.25
            q3_pos = (n - 1) * 0.75
            q1 = data[int(q1_pos)] + (q1_pos - int(q1_pos)) * (
                data[int(q1_pos) + 1] - data[int(q1_pos)]
                ) if q1_pos % 1 else data[int(q1_pos)]
            q3 = data[int(q3_pos)] + (q3_pos - int(q3_pos)) * (
                data[int(q3_pos) + 1] - data[int(q3_pos)]
                ) if q3_pos % 1 else data[int(q3_pos)]
            print(f"quartile : [{float(q1)}, {float(q3)}]")
        elif value == "std":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            std = variance ** 0.5
            print(f"std : {std}")
        elif value == "var":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            print(f"var : {variance}")
