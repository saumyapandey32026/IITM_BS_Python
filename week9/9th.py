def binary_search(l,k):                  #  l should be sorted 
    begin = 0
    end = len(l) - 1
    while (end-begin) > 1:
        mid = (begin + end)//2

        if l[mid] == k:
            return 1
        if l[mid] > k:
            end = mid - 1
        if l[mid] < k:
            begin = mid + 1
    if l[begin] == k or l[end] == k:
        return 1
    else:
        return 0 

import time 
a = time.time(); print(binary_search(list(range(100000000)),80987)) ; b = time.time() ; print(b-a)

import search
a = time.time(); print(search.obvious_search(list(range(100000000)),80987)) ; b = time.time() ; print(b-a)

#  ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️               
a = time.time(); print(search.obvious_search(list(range(100000000)),-1)) ; b = time.time() ; print(b-a)
a = time.time(); print(binary_search(list(range(100000000)),-1)) ; b = time.time() ; print(b-a)

#  ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
l = list(range(100*10000*100))
a = time.time(); print(search.obvious_search(l,-1)) ; b = time.time() ; print(b-a)
a = time.time(); print(binary_search(l,-1)) ; b = time.time() ; print(b-a)





















































