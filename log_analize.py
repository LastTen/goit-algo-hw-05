import sys


def parse_log_line(line: str) -> dict:
    log = {}
    list_of_lines = line.split(" ")
    log["date"] = list_of_lines[0]
    log["time"] = list_of_lines[1]
    log["method"] = list_of_lines[2]
    log["text"] = " ".join(map(str, list_of_lines[3:])).replace("\n", "")
    return log


def load_logs(file_path: str) -> list:
    list_dict = []
    with open(file_path, "r", encoding="utf8") as fh:
        for line in fh:
            list_dict.append(parse_log_line(line))
    return list_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x["method"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    result = {}
    for log in logs:
        if log["method"] in result:
            result[log["method"]] += 1
        else:
            result[log["method"]] = 1
    return result


def display_log_counts(counts: dict):
    print("\nLogging level | Count")
    print("--------------|----------")

    for key, value in counts.items():
        print(f"{key.ljust(13)} | {value}")


display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))

# print(count_logs_by_level(load_logs(sys.argv[1])))

# print(filter_logs_by_level(load_logs(sys.argv[1]), sys.argv[2]))
