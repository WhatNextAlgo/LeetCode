def kWeakestRows(mat, k):
    lst =[]
    for x in range(len(mat)):
        lst.append((x,sum(mat[x])))
    lst.sort(key=lambda x:x[1])
    return [x[0] for x in lst[:k]]
    
# def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#     lst =[]
#     for ind,x in enumerate(mat):
#         count = 0
#         for y in x:
#             if y == 1:
#                 count += 1
#             else:
#                 break
#         lst.append((ind,count))
#     lst.sort(key=lambda x:x[1])
#     return [x[0] for x in lst[:k]]

print(kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))