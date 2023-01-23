from functools import cmp_to_key

with open('input13.txt') as f:
    input = f.read()

lines = input.strip().split('\n\n')
parts = input.strip().replace('\n\n','\n').split('\n')



# print(pairs)

# pairs = []
# for i in range(0,len(lines),3):
#     currPair = []
#     line1 = []
#     for c in lines[i][1:len(lines[i])-2]:
#         if c != ',':
#             if c == '[' or c == ']':
#                 line1.append(c)
#             else:
#                 line1.append(int(c))
#     line2 = []
#     for c in lines[i+1][1:len(lines[i+1])-2]:
#         if c != ',':
#             if c == '[' or c == ']':
#                 line2.append(c)
#             else:
#                 line2.append(int(c))
#     stack = []
#     curr = []
#     # print(line1)
#     for c in line1:
#         if c == '[':
#             stack.append(curr)
#             curr = []
#         elif c == ']':
#             new = stack.pop()
#             new.append(curr)
#             curr = new
#         else:
#             curr.append(c)
#     currPair.append(curr)
#     stack = []
#     curr = []
#     # print(line1)
#     for c in line2:
#         if c == '[':
#             stack.append(curr)
#             curr = []
#         elif c == ']':
#             new = stack.pop()
#             new.append(curr)
#             curr = new
#         else:
#             curr.append(c)
#     currPair.append(curr)
#     pairs.append(currPair)
# def rec(first,second):
#     for i in range(len(first)):
#             if i >= len(second):
#                 return False
#             if type(first[i]) == int and type(second[i]) == int:
#                 if first[i] < second[i]:
#                     return True
#             elif type(first[i]) == list and type(second[i]) == list:
#                 if not rec(first[i],second[i]):
#                     return False
#             elif type(first[i]) == int and type(second[i]) == list:
#                 if not rec(list(first[i]),second[i]):
#                     return False
#             elif type(first[i]) == list and type(second[i]) == int:
#                 if not rec(first[i],list(second[i])):
#                     return False
#             else:
#                 print("You suc")
    # def help():
    #     for i in range(len(first)):
    #         print(first[i])
    #         if i >= len(second):
    #             return False
    #         if type(first[i]) == int and type(second[i]) == int:
    #             if first[i] < second[i]:
    #                 return True
    #         elif type(first[i]) == list and type(second[i]) == list:
    #             if not rec(first[i],second[i]):
    #                 return False
    #         elif type(first[i]) == int and type(second[i]) == list:
    #             if not rec(list(first[i]),second[i]):
    #                 return False
    #         elif type(first[i]) == list and type(second[i]) == int:
    #             if not rec(first[i],list(second[i])):
    #                 return False
    #         else:
    #             print("You suc")
def valid(first,second):
        for i in range(len(first)):
            if i >= len(second):
                return -1
            
            if type(first[i]) == int and type(second[i]) == int:
                if first[i] < second[i]:
                    return 1
                elif first[i] > second[i]:
                    return -1
                
            elif type(first[i]) == list and type(second[i]) == list:
                if valid(first[i],second[i]) == 1: return 1
                elif valid(first[i],second[i]) == -1: return -1
            
            elif type(first[i]) == int and type(second[i]) == list:
                return valid([first[i]],second[i])
            
            elif type(first[i]) == list and type(second[i]) == int:
                return valid(first[i],[second[i]])
            
            else:
                print("you suc")
        if len(second) > len(first):
            return 1
        else:
            return 0
def valid2(first,second):
    if type(first) == int and type(second) == list:
        first = [first]
    
    elif type(first) == list and type(second) == int:
        second = [second]
        
    elif type(first) == int and type(second) == int:
        if first < second:
            return 1
        elif first == second:
            return 0
        else:
            return -1
    if type(first) == list and type(second) == list:
        i = 0
        while i < len(first) and i < len(second):
            x = valid2(first[i],second[i])
            if x == 1:
                return 1
            if x == -1:
                return -1
            i+=1
        if i == len(first):
            if len(first) == len(second):
                return 0
            return 1
        if i == len(second):
            return -1
    
    else:
        print("you suc")

# i,ans = 0,0
# for pair in pairs:
#     i+=1
#     is_right = valid2(pair[0],pair[1])
#     ans += i if is_right == 1 else 0
    # print(pair[0],pair[1])
ans = 0
for i,line in enumerate(lines):
    first,second = map(eval,line.split('\n'))
    if valid2(first,second) == 1:
        ans += i+1
print(ans)
lists = list(map(eval,parts))
lists.append([[2]])
lists.append([[6]])

lists = sorted(lists,key=cmp_to_key(valid2),reverse=True)

for i,li in enumerate(lists):
    if li == [[2]]:
        a = i+1
    if li == [[6]]:
        b = i+1
print(a*b)