n ,room = map(int,input().split())

lst = list([] for _ in range(12))

cut = 6 

for i in range(n) :
    sex,grade = map(int,input().split())
    if sex==1 :
        lst[grade-1].append(1)
    else :
        lst[grade+5].append(1)
print(lst)
lst3=[]
for search in lst :
    if search==[] :
        continue
    lst3.append(search)

for search in lst3 :
    if len(search)>room :
        lst2 = []
        while len(search)>room :
            search.remove(1)
            lst2.append(1)
        lst3.append(lst2)
print(len(lst3))