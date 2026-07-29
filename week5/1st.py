# d = dict(ram = 90, saumya = 80)
# print(d)

# d = {}
# d[100] = "saumya"
# d["ram"] = 99
# # d[100] = "saumya"
# print(d)
# d["saniya"] = 98
# print(d)

# print(d['ram'])
# # print(d['100'])        ye mat kar dena bhai
# print(d[100])
# print(d['saniya'])
# print(d[1])         bhai indexing nhi hoti yhan 


# malgudi = ["it","was","monday","morning","swaminathan","ramesh","school:","ramesh","building;","ramesh","was","it"]
# print(malgudi)
# s = set(malgudi)
# print(len(malgudi))
# print(len(s))
# print(s)
# malgudi[6] = "school"
# malgudi[8] = "building"
# print(malgudi)

# # pahle set ke sath try karo 
# # for x in s:
# #     d[x] = 0
# # print(s)
# # print(d)

# d = {}
# for x in malgudi:
#     d[x] = 0
# for x in malgudi:
#     d[x] = d[x] + 1
# print(d)

# # Another method
# d = {}

# for x in malgudi:
#     if x not in d:
#         d[x] = 0
#     d[x] = d[x] + 1

# print(d)

# # Another method
# d = {}

# for x in malgudi:
#     d[x] = d.get(x, 0) + 1

# print(d) 


# # finding max
# d = {}
# max = 0
# for x in malgudi:
#     d[x] = 0
# for x in malgudi:
#     d[x] = d[x] + 1
#     if d[x] > max:
#         max = d[x]
#         answer_word = x
# print(d)
# print(max,answer_word)

# list in dictionary
d1 = {}
d1["saumya"] = [98,100,99,99,96,100]
d1["saniya"] = [48,60,59,39,62,10]
d1["ravi"] = 69
print(d1)

print(d1["saumya"])
print(d1["saumya"][2])


# Ek khali dictionary banayi
d = {}

# Dictionary mein data add kiya
d['sudarshan'] = [93, 99, 95, 'sudarshan@iitrpr.ac.in']
d['ajit'] = [74, 63, 82, 'ajit.rao1234@gmail.com']
d['supriya'] = [81, 66, 90, 'supriyahs78921@gmail.com']
print(d)
# Supriya ke list ka index 1 print kiya
print(d['supriya'][1])

# Supriya ke list ka index 3 print kiya
print(d['supriya'][3])
