ll=[('turkey', 'coke', 'ice_crea'), ('hering', 'bourbon', 'ice_crea'), ('heineken', 'hering', 'ice_crea'), ('corned_b', 'bourbon', 'ice_crea'), ('corned_b', 'bourbon', 'coke'), ('olives', 'heineken', 'bourbon'), ('corned_b', 'heineken', 'coke'), ('turkey', 'hering', 'bourbon'), ('heineken', 'bourbon', 'coke'), ('coke', 'hering', 'ice_crea'), ('olives', 'hering', 'bourbon'), ('turkey', 'coke', 'hering'), ('turkey', 'corned_b', 'coke'), ('olives', 'ham', 'hering'), ('turkey', 'corned_b', 'heineken'), ('ham', 'heineken', 'ice_crea'), ('ham', 'corned_b', 'hering'), ('corned_b', 'heineken', 'ice_crea'), ('heineken', 'coke', 'bourbon'), ('turkey', 'olives', 'coke'), ('olives', 'heineken', 'ice_crea'), ('turkey', 'olives', 'heineken'), ('olives', 'bourbon', 'ice_crea'), ('heineken', 'coke', 'hering'), ('turkey', 'coke', 'bourbon'), ('olives', 'ham', 'ice_crea'), ('corned_b', 'hering', 'ice_crea'), ('ham', 'corned_b', 'bourbon'), ('olives', 'ham', 'corned_b'), ('turkey', 'ham', 'ice_crea'), ('olives', 'corned_b', 'coke'), ('turkey', 'olives', 'corned_b'), ('turkey', 'ham', 'heineken'), ('ham', 'hering', 'ice_crea'), ('turkey', 'olives', 'bourbon'), ('turkey', 'heineken', 'coke'), ('turkey', 'corned_b', 'hering'), ('ham', 'corned_b', 'heineken'), ('turkey', 'heineken', 'bourbon'), ('olives', 'corned_b', 'hering'), ('heineken', 'ice_crea', 'bourbon'), ('olives', 'corned_b', 'heineken'), ('heineken', 'coke', 'ice_crea'), ('turkey', 'ham', 'coke'), ('heineken', 'bourbon', 'hering'), ('ham', 'heineken', 'bourbon'), ('coke', 'bourbon', 'hering'), ('corned_b', 'coke', 'bourbon'), ('corned_b', 'coke', 'hering'), ('ham', 'bourbon', 'ice_crea'), ('heineken', 'ice_crea', 'hering'), ('olives', 'corned_b', 'bourbon'), ('turkey', 'corned_b', 'ice_crea'), ('olives', 'hering', 'ice_crea'), ('turkey', 'heineken', 'hering'), ('ham', 'heineken', 'hering'), ('ham', 'corned_b', 'ice_crea'), ('turkey', 'corned_b', 'bourbon'), ('turkey', 'olives', 'hering'), ('turkey', 'hering', 'ice_crea'), ('heineken', 'bourbon', 'ice_crea'), ('turkey', 'bourbon', 'ice_crea'), ('coke', 'ice_crea', 'hering'), ('coke', 'bourbon', 'ice_crea'), ('corned_b', 'coke', 'ice_crea'), ('olives', 'coke', 'bourbon'), ('olives', 'coke', 'ice_crea'), ('corned_b', 'heineken', 'bourbon'), ('ham', 'coke', 'bourbon'), ('turkey', 'olives', 'ice_crea'), ('turkey', 'ham', 'hering'), ('olives', 'ham', 'heineken'), ('turkey', 'ham', 'bourbon'), ('olives', 'ham', 'coke'), ('ham', 'heineken', 'coke'), ('olives', 'heineken', 'coke'), ('olives', 'ham', 'bourbon'), ('turkey', 'olives', 'ham'), ('olives', 'corned_b', 'ice_crea'), ('olives', 'coke', 'hering'), ('ham', 'coke', 'hering'), ('corned_b', 'heineken', 'hering'), ('olives', 'heineken', 'hering'), ('corned_b', 'bourbon', 'hering'), ('turkey', 'heineken', 'ice_crea'), ('ham', 'corned_b', 'coke'), ('ham', 'hering', 'bourbon'), ('turkey', 'ham', 'corned_b'), ('ham', 'coke', 'ice_crea'), ('corned_b', 'ice_crea', 'hering')]


for item in ll:
    print len(ll)

    for i,item2 in enumerate(ll):
        if item[0]==item2[0] and item[1]==item2[2] and item2[1]==item[2]:
            print item
            print item2
            del ll[i]


print ll