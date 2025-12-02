import os


def ft_tqdm(iterable):
    """
    Custom tqdm implementation for terminal progress bars
    """
    total = len(iterable)
    for idx, item in enumerate(iterable, 1):
        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80

        percent = int(idx * 100 / total)
        percent_str = f'{percent:3}%'
        curr_over_total = f' {idx}/{total}'

        remain_length = terminal_width - \
            len(percent_str) - len(curr_over_total) - 2

        if remain_length < 10:
            remain_length = 10

        bar = "█" * int((idx / total) * remain_length)
        space = " " * (remain_length - len(bar))
        process_bar = f'|{bar}{space}|'
        print(f"\r{percent_str}{process_bar}{curr_over_total}",
              end="", flush=True)
        yield item
    print()
