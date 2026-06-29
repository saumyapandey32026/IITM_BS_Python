# import calendar as cd  
# # print(cd.month(2026,6))
# print(cd.calendar(2026))


# from calendar import *
# print(month(2026,6))
# print(calendar(2026))

from calendar import month
print(month(2026,6))
# print(calendar(2026))     ye error dega since you imported only month

from calendar import month, calendar
print(calendar(2026))   # ab error nhi aayega since you imported calendar as well this time 

from calendar import month as m
print(m(2026,6))





















