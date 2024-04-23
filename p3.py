import sys

def suniq(lines, count=False, duplicate=False, ignore_case=False):
    lines = [line.strip().lower() if ignore_case else line.strip() for 
line in lines]

    unique_lines = []
    counts = {}

    prev_line = None
    for line in lines:
        if line != prev_line:
            unique_lines.append(line)
            prev_line = line
            counts[line] = 1
        else:
            counts[line] += 1

    output_lines = []

    if count:
        for line in unique_lines:
            count = str(counts[line])
            output_lines.append(f"{count:7d} {line}")
    elif duplicate:
        for line in lines:
            if line not in unique_lines and counts[line] > 1:
                output_lines.append(line)
    elif True:  # This is equivalent to "unique"
        for line in unique_lines:
            if counts[line] == 1:
                output_lines.append(line)

    return output_lines

def main():
    count = False
    duplicate = False
    ignore_case = False
    unique = False

    args = sys.argv[1:]

    while args and args[0].startswith('-'):
        option = args.pop(0)
        if option == '-c':
            count = True
        elif option == '-d':
            duplicate = True
        elif option == '-i':
            ignore_case = True
        elif option == '-u':
            unique = True
        else:
            print("Unknown option:", option)
            sys.exit(1)

    if args:
        with open(args[0], 'r') as file:
            lines = file.readlines()
    else:
        lines = [line.strip() for line in sys.stdin.readlines()]

    output_lines = suniq(lines, count, duplicate, ignore_case)

    for line in output_lines:
        print(line, end='')

if __name__ == "__main__":
    main()
