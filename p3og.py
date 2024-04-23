import sys

def suniq(lines, count=False, duplicate=False, ignore_case=False, unique=False):
    unique_lines = []
    counts = {}

    prev_line = None
    for line in lines:
        line_key = line if not ignore_case else line.lower()

        if line_key != prev_line:
            unique_lines.append(line)
            prev_line = line_key
            counts[line_key] = 1
        else:
            counts[line_key] += 1

    output_lines = []

    if count:
        for line in unique_lines:
            count = counts[line.lower()] if ignore_case else counts[line]
            output_lines.append(f"{count:7d} {line}")
    elif duplicate:
        for line in unique_lines:
            line_key = line.lower() if ignore_case else line
            count = counts[line_key]
            if count > 1:
                output_lines.append(line)
    elif unique:
        for line in unique_lines:
            line_key = line.lower() if ignore_case else line
            if counts[line_key] == 1:
                output_lines.append(line)
    else:
        output_lines = unique_lines

    return output_lines


def main():
    count = False
    duplicate = False
    ignore_case = False
    unique = False

    args = sys.argv[1:]

    while args and args[0].startswith('-'):
        options = args.pop(0)[1:]
        for option in options:
            if option == 'c':
                count = True
            elif option == 'd':
                duplicate = True
            elif option == 'i':
                ignore_case = True
            elif option == 'u':
                unique = True
            else:
                print("Unknown option:", option)
                sys.exit(1)

    if args:
        with open(args[0], 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    output_lines = suniq(lines, count, duplicate, ignore_case, unique)

    for line in output_lines:
        print(line, end='')

if __name__ == "__main__":
    main()
