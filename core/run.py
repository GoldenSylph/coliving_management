from utils import calculate_whole, calculate_per_day


def main(whole: bool) -> None:
    if whole:
        calculate_whole()
    else:
        calculate_per_day()


if __name__ == "__main__":
    main(True)
