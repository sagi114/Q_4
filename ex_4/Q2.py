import math
def sort_merg(arr):
    n=len(arr)
    if n==1:
        return arr
    half=n/2
    f_l = []
    s_l = []
    for i in range(n):
        if i<half:
            f_l.append(arr[i])
        else:
            s_l.append(arr[i])
    f_l=sort_merg(f_l)
    s_l=sort_merg(s_l)
    f_len=len(f_l)
    s_len = len(s_l)
    f_count=0
    s_count = 0
    arr_1=[]
    f_s_len=f_len+s_len
    f_s_count=f_count+s_count
    while (f_s_len)>f_s_count:
        if (f_count == f_len):
            arr_1.append(s_l[s_count])
            f_count += 1
            f_s_count += 1
        elif (s_count == s_len):
            arr_1.append(f_l[f_count])
            s_count += 1
            f_s_count += 1
        elif (f_count!=f_len ) and (f_l[f_count][0])<(s_l[s_count][0]):
           arr_1.append(f_l[f_count])
           f_count+=1
           f_s_count+=1
        elif ((s_count!=s_len) and (f_l[f_count][0])>=(s_l[s_count][0])):
            arr_1.append(s_l[s_count])
            s_count += 1
            f_s_count += 1




    return arr_1
def create_one_arr_from_two_arr(B,A):
    arr=[]
    l=len(B)
    for i in range(l):
        arr.append([B[i],A[i]])
    return arr
def create_two_from_one(arr):
    n=len(arr)
    A=[]
    B=[]
    for i in range(n):
        A.append(arr[i][1])
        B.append(arr[i][0])
    return B,A
def hotel_schedule(A,B,C):
    arr = create_one_arr_from_two_arr(B, A)
    print(type(arr))
    list_arr = sort_merg(arr)
    B_tmp, A_tmp = create_two_from_one(list_arr)
    num = 0
    j = 0
    i = 0
    l_b=len(B_tmp)
    l_a=len(A_tmp)
    while i < l_b or j < l_a:
        if((i+j)==(l_a+l_b)-1):return True
        elif B_tmp[i] > A_tmp[j]:
            num += 1
            j += 1
        elif B_tmp[i] <= A_tmp[j]:
            num -= 1
            i += 1
        if C < num or C<0: return False
    return True
"""""
if __name__ == '__main__':
    A = [1, 3, 5]
    B = [2, 6, 8]
    c = 1
    print(hotel_schedule(c,A,B))
    A = [1, 3, 7]
    B = [2, 6, 8]
    c = 1
    print(hotel_schedule(c, A, B))

    #hotel_schedule(c, A, B)
"""""