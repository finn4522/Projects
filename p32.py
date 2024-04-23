import sys

def suniq(file, opts):
    # Initialize variables
    count = 1
    prev_line = None
    ignore_case = '-i' in opts
    count_prefix = '-c' in opts
    only_duplicates = '-d' in opts
    only_uniques = '-u' in opts

    # Read from file or standard input
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    # Process lines
    for line in lines:
        # Ignore case if specified
        if ignore_case:
            line = line.lower()

        # Check for duplicates or uniques
        if prev_line and prev_line == line:
            count += 1
        else:
            if only_duplicates and count < 2:
                count = 1
                prev_line = line
                continue
            elif only_uniques and count > 1:
                count = 1
                prev_line = line
                continue

            # Print line with count prefix if specified
            if count_prefix:
                print(f'{count:7d} {line.strip()}')
            else:
                print(line.strip())

            count = 1
            prev_line = line

if __name__ == '__main__':
    opts = sys.argv[1:-1]
    file = sys.argv[-1] if len(sys.argv) > 1 else None
    suniq(file, opts)
