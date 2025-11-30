

def ft_tqdm(iterable):
    """
    Custom tqdm implementation for terminal progress bars
    """
    line_length = 80
    total = len(iterable)
    for idx, item in enumerate(iterable, 1):
        percent = int(idx * 100 / total)
        percent_str = f'{percent:3}%'
        curr_over_total = f' {idx}/{total}'
        remain_length = line_length - len(
            percent_str) - len(curr_over_total) - 2
        bar = "█" * int((idx / total) * remain_length)
        space = " " * (remain_length - len(bar))
        process_bar = f'|{bar}{space}|'
        print(f"\r{percent_str}{process_bar}{curr_over_total}", end="")
        yield item
    print()
