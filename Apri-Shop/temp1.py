
row=['hering', 'corned_b', 'olives', 'ham', 'turkey', 'bourbon', 'ice_crea']
dic={('corned_b', 'heineken'): 0, ('ham', 'ice_crea','turkey'): 0, ('corned_b', 'heineken'): 0, ('olives', 'corned_b'): 0}

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