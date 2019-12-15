
#remove duplicates in string

str = 'helloworld'
#str = ''.join(set(str))
# print(str)
# print(str[0:11])

def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      str1.count(c)
      return index
  return "None"

print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))




def removeduplicate(str):
    lst= set()
    for x in str:
        lst.add(x)
        if x in lst:

            break

        #if x in lst:

    print(lst)


        #break

    #str1 =''.join(lst)
    #return str1

print(removeduplicate(str))
a = ["asd","def","ase","dfg","asd","def","dfg"]
#seen = set()
result = []
for item in a:
    if item not in result:
        #seen.add(item)
        result.append(item)
print(result)
from collections import OrderedDict
def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))


print(remove_duplicate('ravindrasharma'))
