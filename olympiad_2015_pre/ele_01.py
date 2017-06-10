
def ban_car(number,list):
    cnt = 0
    for i in range(len(list)):
        if(number == list[i]):
            cnt +=1

    return cnt

if __name__ == '__main__':
    n = int(input())

    car_number =list(map(int,input().split()))

    print (ban_car(n,car_number))



