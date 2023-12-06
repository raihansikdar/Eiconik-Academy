import sys
import math
input = sys.stdin.readline


for _ in range(int(input())):
   abul, babul = map(int, input().split())
   list_1 = list(map(int, input().split()))
   list_2 = list(map(int, input().split()))
   list_1.sort()
   for i in list_2:
       t = False
       for j in range(abul):
           if i > list_1[j]:list_1[j] = i;t = True; break
      
       if not t:list_1[0] = i;list_1.sort()
       else:t = False; list_1.sort()
   print(sum(list_1))