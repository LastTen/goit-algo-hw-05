import sys


def parse_log_line(line: str) -> dict:
    """
    This function parses a log line and returns a dictionary containing the date, time, method, and text.
    """
    log = {}
    list_of_lines = line.split(" ")
    log["date"] = list_of_lines[0]
    log["time"] = list_of_lines[1]
    log["method"] = list_of_lines[2]
    log["text"] = " ".join(map(str, list_of_lines[3:])).replace("\n", "")
    return log


def load_logs(file_path: str) -> list:
    """
    This function takes a file path and returns a list of log dictionaries.
    """
    list_dict = []
    with open(file_path, "r", encoding="utf8") as fh:
        for line in fh:
            list_dict.append(parse_log_line(line))
    return list_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    This function takes a list of log dictionaries and a logging level and returns a filtered list of log dictionaries.
    """
    return list(filter(lambda x: x["method"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    This function takes a list of log dictionaries and returns a dictionary of logging levels and their counts.
    """
    result = {}
    for log in logs:
        if log["method"] in result:
            result[log["method"]] += 1
        else:
            result[log["method"]] = 1
    return result


def display_log_counts(counts: dict):
    """
    This function takes a dictionary of logging levels and their counts and displays them in a formatted table.
    """

    print("\nLogging level | Count")
    print("--------------|----------")

    for key, value in counts.items():
        print(f"{key.ljust(13)} | {value}")


def main():
    try:
        if len(sys.argv) == 2:
            display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))

        if len(sys.argv) == 3:
            display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))
            dict = filter_logs_by_level(load_logs(sys.argv[1]), sys.argv[2])
            if len(dict):
                print(f"\nLogs found for level {sys.argv[2]}")
                for el in dict:
                    print(f"{el['date']} {el['time']} - {el['text']}")
            else:
                print(f"No logs found for level {sys.argv[2]}")

        if len(sys.argv) < 2:
            print("Empty file name")
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found")


if __name__ == "__main__":
    main()


# print(count_logs_by_level(load_logs(sys.argv[1])))

# print(filter_logs_by_level(load_logs(sys.argv[1]), sys.argv[2]))
