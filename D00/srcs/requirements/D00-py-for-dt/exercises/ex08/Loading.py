def ft_tqdm(lst: range) -> None:
    """
    Displays a progress bar in the console for the given iterable.

    Args:
        lst (range): The iterable to display the progress for.

    Yields:
        item: The next item in the iterable.
    """
    BAR_LENGTH = 30
    for i, item in enumerate(lst, start=1):
        time_elapse = len(lst)
        percentage = i * 100 // len(lst)
        bar_progress = "█" * (percentage * BAR_LENGTH // 100)
        print("\r{:>3}%|{}| {}/{}".format(
            percentage, bar_progress, i, time_elapse), end="", flush=True)
        yield item
