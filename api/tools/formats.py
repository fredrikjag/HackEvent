def format_time_left(time_left: int):
    seconds = time_left % 60
    minutes = time_left // 60 % 60
    hours = time_left // 3600

    return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    None