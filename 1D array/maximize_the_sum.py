#fsm here

#Solution for hackerearth problem to maximum sum
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-sum-0423b95e/
t=int(input())
for test in range(t):
    ans=[]
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    # print(a)
    num_arr=[0]*n
    arr.sort()
    last_item=arr[-1]
    i=0
    while len(arr)>0:
        if(arr[-1]<0):
            break
        if(last_item!=arr[-1]):
            # print(last_item,arr[-1])
            i+=1
        last_item=arr[-1]
        num_arr[i]+=arr[-1]
        arr.pop()

    num_arr.sort()
    print(sum(num_arr[-k:]))
        

        