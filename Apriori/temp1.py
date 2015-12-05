import itertools

dic={('corned_b', 'B'): 0, ('ham', 'ice_crea'): 0, ('corned_b', 'A'): 0, ('olives', 'corned_b'): 0,('corned_b', 'C'): 0,('olives', 'ooo'): 0,('corned_b', 'D'): 0,}
#dic={('ham', 'heineken'): 0, ('turkey', 'hering'): 0, ('ham', 'corned_b'): 0, ('bourbon', 'ice_crea'): 0, ('coke', 'hering'): 0, ('turkey', 'ham'): 0, ('turkey', 'ice_crea'): 0, ('ham', 'ice_crea'): 0, ('hering', 'bourbon'): 0, ('turkey', 'bourbon'): 0, ('olives', 'heineken'): 0, ('corned_b', 'hering'): 0, ('olives', 'coke'): 0, ('heineken', 'ice_crea'): 0, ('ham', 'hering'): 0, ('turkey', 'olives'): 0, ('heineken', 'bourbon'): 0, ('corned_b', 'heineken'): 0, ('olives', 'corned_b'): 0, ('ham', 'coke'): 0, ('corned_b', 'ice_crea'): 0, ('heineken', 'hering'): 0, ('olives', 'hering'): 0, ('corned_b', 'coke'): 0, ('ham', 'bourbon'): 0, ('olives', 'ham'): 0, ('corned_b', 'bourbon'): 0, ('olives', 'bourbon'): 0, ('olives', 'ice_crea'): 0, ('hering', 'ice_crea'): 0, ('heineken', 'coke'): 0, ('turkey', 'corned_b'): 0, ('turkey', 'coke'): 0, ('coke', 'bourbon'): 0, ('turkey', 'heineken'): 0, ('coke', 'ice_crea'): 0}


temp_list=[]
tup=[]
dic_tmp={}
ll=[]
new_list=[]
for item in dic:

    for item2 in dic:
        if cmp(item[0],item2[0])==0:
            ll.append(item[1])
            ll.append(item2[1])

    ll_sort= list(set(ll))
    ll=[]


    new_list=list(itertools.combinations(ll_sort,2))

    for i in new_list:

        temp=item[0]

        t = tuple([x for x in temp])
        e = tuple(temp.split(","))
        q=(e+i)

        temp_list.append(q)


l2 = list(set(temp_list))

for item in l2:

    for i,item2 in enumerate(l2):
        if item[0]==item2[0] and item[1]==item2[2] and item2[1]==item[2]:

            del l2[i]

for item in l2:
    a=tuple(item)
    dic_tmp[a]=0















'''
for item in dic:
    lenth=len(item)
    i=0
    for x in range(lenth+1):
        if i==lenth:
            print item
            break

        if item[i] in row and i<=lenth:
            i+=1
        else:
            break
'''