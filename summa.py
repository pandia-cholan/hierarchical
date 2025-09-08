# def countsofwordsinstring(string):
#     ''' 3. Count words without using split()
#     Example:
#     Input: "I love Python"
#     Output: 3'''
#     wordslist = []
#     start = 0
#     end = 0
#     while end < len(string):
#         if string[end] == " ":
#             substring = string[start: end]
#             if substring:
#                 wordslist.append(substring)
#             end += 1
#             start = end
#         else:
#             end += 1
#         print(start,end)
#     print(len(string))
#
#     wordslist.append(string[start:end])
#
#     print(wordslist)
#     return len(wordslist)
#
#
# # print(countsofwordsinstring("I love Python"))
# # print(countsofwordsinstring("I HEllo Words jamal venna"))
# # print(countsofwordsinstring("I "))
# print(countsofwordsinstring("   I HEllo Words jamal venna     "))



from datetime import datetime

print(datetime.now())
print(datetime.date())



