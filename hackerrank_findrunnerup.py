#find the runner up from an array taken from the user as input(hackerrank ques)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    h=set(arr)
    arr_list=list(h)
    arr_list.sort()
    print(arr_list[-2])
