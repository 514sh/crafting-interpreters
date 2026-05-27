from pylox import scanner


def run(source):
    my_scanner = scanner.Scanner(source)
    scanned_tokens = my_scanner.scan_tokens()
    for tokens in scanned_tokens:
        print(str(tokens))


def run_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    return run("".join(lines))


def run_prompt():
    lines = []
    while True:
        print("[pylox] > ", end="")
        line = input()
        if not line:
            print("\nExited pylox repl...\n")
            break
        lines.append(line)
    return run("".join(lines))


def report(line, where, message):
    print(f"[line {line} ] Error {where}: {message}")


def error(line, message):
    report(line, "", message)


def main():
    import sys

    my_args = len(sys.argv)

    if my_args >= 2:
        return run_file(sys.argv[1])
    elif my_args == 1:
        return run_prompt()
    else:
        raise Exception("Invalid run...")


if __name__ == "__main__":
    main()
