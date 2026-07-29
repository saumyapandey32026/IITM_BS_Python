# def abs_sort(l):
#     x = []
#     # for i in range(len(l)):
#     while len(l) > 0:
#         mini = l[0]
#         # print(i,mini)
#         # print(l[i])           # for ke sath likhoge to line error de degi, i mean is line se error aayega , index out of range
#         for j in range(len(l)):
#             if l[j] < mini:
#                 mini = l[j]
#         x.append(mini)
#         l.remove(mini)
#     print(x)

m = [7,3,2,4,9,1,5,1,3,-1]
# abs_sort(m)


# 2nd method
# def min_list(l):
#     while len(l)>0:
#         mini = l[0]
#         for i in range(len(l)):
#             if l[i] < mini:
#                mini = l[i]
               #print(mini)
            # print(mini)
        # print(mini)
    # print(mini)
# min_list(m)

# 2nd method
def min_list(l):
        mini = l[0]
        for i in range(len(l)):
            if l[i] < mini:
               mini = l[i]
        return mini 
def abs_sort(l):
    x = []
    while len(l) > 0:
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    print (x)
    return x
                
abs_sort(m)




















