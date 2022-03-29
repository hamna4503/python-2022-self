def swap_case(s):
    x = ""
    for i in str(s):
        if i.islower() == True:
            k = i.upper()
            x += k
        else:
            j = i.lower()
            x += j

    return (x)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)