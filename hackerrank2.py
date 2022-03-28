if __name__ == '__main__':
    l = []
    marks = set()
    second_lowest_l = []
    for _ in range(int(input())):
        k = []
        name = input()
        score = float(input())
        k.append(name)
        k.append(score)
        marks.add(score)
        l.append(k)
    marks_l = list(marks)
    marks_l.sort()
    second_lowest = marks_l[1]
    for i in range(len(l)):
        if second_lowest in l[i]:
            second_lowest_l.append(l[i][0])
    second_lowest_l.sort()
    for i in second_lowest_l:
        print(i)
