#효율 좀 안 좋은거

def partition(num, cnt):
    if cnt==1: return [[num]]
    else:
        ret=[]
        for i in range(1,num-cnt+2):
            for j in partition(num-i,cnt-1):
                temp=[i]+j
                ret.append(temp)
        return ret

def check_sorted(lst):
    for i in range(1,len(lst)):
        if lst[i-1]>lst[i]: return False
    return True

def calc_dis(lst,n):
    ret=[]
    for cur in lst:
        temp=0
        for i in range(len(cur)-1):
            if cur[i]>cur[i+1]:
                temp+=n-cur[i]+cur[i+1]
            else:
                temp+=cur[i+1]-cur[i]
        ret.append(temp)
    return ret

def solution(n, weak, dist):
    answer = 0
    dist = sorted(dist,reverse=True)

    for i in range(len(dist)):
        member = dist[:i+1]
        lst = partition(len(weak),i+1)
        '''
        for j in partition(len(weak),i+1):
            if check_sorted(j): lst.append(j)
        '''
        for part in lst:
            for idx in range(len(weak)):
                weak_partition = []
                cnt=0
                for cur in part:
                    temp = []
                    for j in range(cur):
                        temp.append(weak[(idx+cnt)%len(weak)])
                        cnt+=1
                    weak_partition.append(temp)

                dis_list = sorted(calc_dis(weak_partition,n),reverse=True)
                flag=True
                for j in range(len(dis_list)):
                    if member[j]<dis_list[j]:
                        flag=False
                        break

                if flag:
                    return i+1
    return -1