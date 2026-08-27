# def rbinary_search(l,k,begin,end):
#     if begin > end :
#         return 0
#     mid = (begin + end)//2
#     if l[mid] == k:
#         return 1
#     elif l[mid] > k:
#         return rbinary_search(l,k,begin,mid-1)
#     else:
#         return rbinary_search(l,k,mid+1,end)
    
# l = [39,90,20,39,78,98,76]
# print(rbinary_search(sorted(l),20,0,len(l)-1))




# METHOD 2 

def rbinary_search(l,k,begin,end):              # l should be sorted since you are going to use recursion 
    if begin == end:
        if l[begin] == k:
            return 1
        else:
            return 0
    if end - begin == 1:
        if l[begin] == k or l[end] == k:
            return 1 
        else:
            return 0
    if end - begin > 0:
        mid = (begin+end)//2
        if l[mid] == k:
            return 1
        if l[mid] > k:
            end = mid - 1
        if l[mid] < k:
            begin = mid + 1
    if end - begin < 0 :
        return 0

    return rbinary_search(l,k,begin,end)


l = [0,1,3,4,56,78,98,99]
print(rbinary_search(l,3,0,len(l)-1))
















































