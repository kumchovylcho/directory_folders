import os
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        executed_in = end_time - start_time
        print(f"Executed in {executed_in:.3f} seconds.\n")
        return result
    return wrapper


@execution_time
def count_nested_directories(path: str):
    max_depth = 0
    max_depth_dir = ''

    for root, dirs, _ in os.walk(path):
        depth = root.count(os.sep)
        if depth > max_depth:
            max_depth = depth
            max_depth_dir = root

    return max_depth_dir, max_depth


def prepare_result(start_path, dir_list, indent=2):
    output = [f"Base Path -> {start_path}",
              f"Nested Folders -> {len(dir_list) + 1}",
              "Tree Structure:"]

    indent_setter = 0
    for i in range(len(dir_list)):
        output.append(f"- {' ' * indent_setter}{dir_list[i]}")
        indent_setter += indent

    return "\n".join(output)


def main():
    starting_path = input("Enter the directory path to start: ").replace("/", "\\")

    if not os.path.isdir(starting_path):
        print("Invalid directory path.")
        return

    print("Please wait ...\n")

    max_nested_dir, max_depth = count_nested_directories(starting_path)

    avoid_paths = len(starting_path.split("\\"))
    nested_folders = max_nested_dir.split("\\")[avoid_paths:]
    result = prepare_result(starting_path,
                            nested_folders
                           )
    print(result)


if __name__ == "__main__":
    main()