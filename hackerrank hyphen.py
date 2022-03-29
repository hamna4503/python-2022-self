def split_and_join(line):
    line_split = line.split()
    x = ""
    for i in line_split:
        x += i + "-"
    final = x[0:-1]
    return (final)

    # write your code here
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)