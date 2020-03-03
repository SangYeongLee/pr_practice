from itertools import permutations
from itertools import combinations
from collections import deque

a=[(5,'a'),(7,'ss'),(4,'da'),(3,'ab'),(2,'aa')]
a.sort(key= lambda a:a[-1])

print(a)
items= ['A','B','C','A']

a=set()
b=set()
for i in list(combinations(items,2)):
    a.add(i)
print(a)

for i in list(permutations(items,2)):
    b.add(i)
print(b)

nums=deque([1,3,4])
print(nums[-1])
for i in range(len(nums)):
    print(nums.pop())
print()
nums=deque([1,3,4])
nums.append(12)
for i in range(len(nums)):
    print(nums.popleft())
a = [1,[2,3],(4,5,6)]
b = list(a) # 또는 a[:]

if a == b:
    print ("a와 b 는 값이 같다")

if a is b:
    print ("a 와 b 는 같은 객체이다")
