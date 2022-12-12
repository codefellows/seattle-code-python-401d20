import calendar
list1 = list([name for name in calendar.month_name if name])

# list1 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# print(list1)


# print('This is a listing of each item in the List')
# for i in list1:
#     print(i)


















# print('This is a counter using the items in the list')
# for i in range(len(list1)):
#     print(i)



























# print('This is a listing of each item in the List and the counter')
# j = 0
# for i in list1:
#     print(j, i)
#     j += 1


























# print('printing the tuples in object directly')
# for i in enumerate(list1):
#     print(i)



























print('changing index and printing separately with optional counter change')
for i, j in enumerate(list1):
    print(i, j)
