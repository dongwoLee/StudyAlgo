
def earnMoney(dice):
    if(dice[0]==dice[1] and dice[1]==dice[2]):
        return 10000+dice[0]*1000
    elif(dice[0]==dice[1]):
        return 1000+dice[0]*100
    elif(dice[1]==dice[2]):
        return 1000+dice[1]*100
    elif(dice[0]==dice[2]):
        return 1000+dice[0]*100
    else:
        return max(dice)*100

if __name__ == '__main__':

    a=list(map(int,input().split()))
    print(earnMoney(a))




