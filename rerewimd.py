# ss = "practice sql"
# index = ss.find(" ")
# # print(ss[index+1:len(ss)])
# # print(ss[0: index])
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
# print(names[-2:-2])
# info = ((('Emma', 26), ('Frank', 32)), (('Grace', 29), ('Henry', 27)), (('Ivy', 30), ('Jack', 25)), (('Kate', 28), ('Leo', 31)))
# aa = [age for i in info for (name,age) in i if name[-1] == "y" ]
# print(aa)
#
# data = [[['a', 'b', 'c'], ['d', 'e', 'f']], [['g', 'h', 'i'], ['j', 'k', 'l']]]
# cc = [vowels for i in data for k in i for vowels in k if vowels not in 'aeiou' ]
# print(cc)
#
# data = {'A': {'x': [1, 2, 3]}, 'B': {'y': [4, 5, 6]}}
# dd = {key: sum(value) for values in data.values() for key,value in values.items()}
# print(dd)
# num = int(input("Enter numbers in the Fibonacci : "))
# n1, n2 = 0, 1
# n3 = 0
# if num == 1:
#     print(n1)
# else:
#     print(n1, n2, end=" ")
# while n3 <= num:
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
# num = int(input("Enter numbers to cout : "))
# c = 0
# while num !=  0 :
#      num = num //10
#      c = c + 1
# print(c)
# x = int(input("Enter the x : "))
# y = int(input("Enter the y : "))
# p= 1
# i = 1
# while(i <= y):
#     p = p * x
#     i = i + 1
# print(p)
# nested_list = [1, [2, [3, [4, [5]]]]]
# list = []
# i = 1
# while len(list) <= 5:
#   print(nested_list)
#   list.append(nested_list[0])
#   nested_list.pop(0)
#   print(list)
#   print(nested_list)


# nested_list = [1, [2, [3, [4, [5]]]]]
# list = nested_list.pop(1)
# # print(nested_list)
# lll = []
# for i in range(4):
#     lll.append([i,i**2,i**3])
# print(lll)
#
# fll = [ oo for kll in lll for oo in kll]
# print(fll)
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
# print(names)
# # fll.append(names)
# # print(fll)
# fll.extend(names)
# print(fll)
#
# for index,element in enumerate(fll):
#     print(f'Index : {index}, Element : {element}')
#
# nested_dict = {
#     'New York': {
#         'Manhattan': 1636268,
#         'Brooklyn': 2559903,
#         'Queens': 2253858,
#         'Bronx': 1418207,
#         'Staten Island': 476015
#     },
#     'Los Angeles': {
#         'Central LA': 1253400,
#         'Westside': 1297759,
#         'San Fernando Valley': 1764282,
#         'South LA': 1114964
#     },
#     'Chicago': {
#         'Downtown': 2716000,
#         'North Side': 1973000,
#         'South Side': 1745000
#     }
# }
#
# high = [city for city, neighborhoods in nested_dict.items()  if sum(neighborhoods.values()) >= 8000000]
# print(high)

# string_list = ["You have a list of", "strings where each string", "represents a sentence"]
# vowels = 'aeiouAEIOU'
# Count = {}
# for s in string_list:
#     count = 0
#     for i in vowels:
#         if i in vowels:
#             count += 1
#     Count[s] = count
# print(Count)


nested_list = [1, [2, [3, [4, [5]]]]]
lll = nested_list[:]
flat_list = []
while lll:
    print(lll)
    item = lll.pop(0)
    print('item ef loop',item)
 0    if type(item) == list :
        lll = lll + item
        print('2d',lll)
    else:
        flat_list.append(item)
print(flat_list)
# lll.append(nested_list.pop(0))
# print(nested_list)
# print(lll)
# print(type([[2, [3, [4, [5]]]]]))
# print(type([2, [3, [4, [5]]]]))