import MySQLdb
import itertools

class Database:

    host='localhost'
    port = 3306
    user='root'
    passwd='1234'
    db ='apri'

    def __init__(self):
        self.connection = MySQLdb.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db
        )
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def sql(self,sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            self.connection.rollback()

    def commit(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()

def CreateDic(DB_table="shop"):
    """
    read data from database shop_test;
    Create a dic;
    return dic
    Example:
    dic={'turkey': 5, 'baguette': 1, 'olives': 5, 'steak': 1, 'ham': 4, 'corned_b': 3, 'heineken': 4, 'coke': 3, 'sardines': 2}

    """
    db=Database()
    sql="select item_1,item_2,item_3,item_4,item_5,item_6,item_7 from %s" %(DB_table)
    db.sql(sql)
    data=db.cursor.fetchall()
    list_item=[]
    for row in data:
        row=list(row)
        list_item+=row

    dic_C1={}
    for item in list_item:
        count=list_item.count(item)
        dic_C1[item]=count

    return dic_C1

def Cut(min_suppt,dic):
    pre_del=[]
    for item in dic:
        if dic[item]<min_suppt:
            pre_del.append(item)

    for item in pre_del:
        del dic[item]

    return dic

def CreateItemSet_2(dic,num=2):
    temp_list=[]
    for item in dic:
        temp_list.append(item)
    new_list=list(itertools.combinations(temp_list,num))
    dic={}
    for item in new_list:
        dic[item]=0
    return dic

def CreateItemSet_3(dic,num=3):
    temp_list=[]
    dic_tmp={}
    ll=[]
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
            e = tuple(temp.split(","))
            q=(e+i)
            temp_list.append(q)

    l2 = list(set(temp_list))
    for item in l2:

        for i,item2 in enumerate(l2):
            if item[0]==item2[0] and item[1]==item2[2] and item2[1]==item[2]:

                del l2[i]

    temp_list_2=l2[:]
    for i in temp_list:
        if len(i)<num:
            temp_list_2.remove(i)

    for item in temp_list_2:
        a=tuple(item)
        dic_tmp[a]=0
    return dic_tmp

def CreateItemSet_4(dic,num=4):

    temp_list=[]
    dic_tmp={}
    ll=[]
    for item in dic:

        for item2 in dic:
            if cmp(item[0],item2[0])==0 and cmp(item[1],item2[1])==0:
                ll.append(item[1])
                ll.append(item2[1])

        ll_sort= list(set(ll))
        ll=[]

        new_list=list(itertools.combinations(ll_sort,2))

        for i in new_list:

            temp=item[0]

            e = tuple(temp.split(","))
            q=(e+i)

            temp_list.append(q)

    l2 = list(set(temp_list))
    for item in l2:

        for i,item2 in enumerate(l2):
            if item[0]==item2[0] and item[1]==item2[2] and item2[1]==item[2]:

                del l2[i]

    temp_list_2=l2[:]
    for i in temp_list:
        if len(i)<num:
            temp_list_2.remove(i)

    for item in temp_list_2:
        a=tuple(item)
        dic_tmp[a]=0
    return dic_tmp

def Count(dic,DB_table="shop"):
    DB_table=DB_table
    db=Database()
    sql="select item_1,item_2,item_3,item_4,item_5,item_6,item_7 from %s" %(DB_table)
    db.sql(sql)
    data=db.cursor.fetchall()
    list_item=[]
    for row in data:
        row=list(row)
        list_item+=row
        #print "--- Scan Line: ---"
        #print row

        for item in dic:
            lenth=len(item)
            i=0
            for x in range(lenth+1):
                if i==lenth:
                    #print item
                    dic[item]=dic[item]+1
                    #print "-------------------"
                    break

                if item[i] in row and i<=lenth:
                    i+=1
                else:
                    break
    return dic


if __name__ == '__main__':

    min_support=200

    dic_1=CreateDic()  # Create dic first time

    print "--- First Dic ---"
    print dic_1

    print "--- Cut First Dic ---"
    dic_1_Cutted=Cut(min_support,dic_1)   # 3  min support
    print dic_1_Cutted


    print "------ Item Set 2 ------ "

    ItemSet_2=CreateItemSet_2(dic_1_Cutted,2)
    print  "Item Set 2: ", ItemSet_2

    ItemSet_2_Counted=Count(ItemSet_2)
    print  "Item Set 2 Counted: ", ItemSet_2_Counted

    ItemSet_2_Cutted=Cut(min_support,ItemSet_2_Counted)
    print  "Item Set 2 Cutted: "  ,ItemSet_2_Cutted


    print "------ Item Set 3 ------"
    ItemSet_3=CreateItemSet_3(ItemSet_2_Cutted)
    print  "Item Set 3: %s "  %(ItemSet_3)

    ItemSet_3_Counted=Count(ItemSet_3)
    print  "Item Set 3 Counted: %s" %(ItemSet_3_Counted)

    ItemSet_3_Cutted=Cut(min_support,ItemSet_3_Counted)
    print  "Item Set 3 Cutted:  %s "  % (ItemSet_3_Cutted)

    print "------ Item Set 4 ------"
    ItemSet_4=CreateItemSet_4(ItemSet_3_Cutted)
    print  "Item Set 4: %s "  %(ItemSet_4)

    ItemSet_4_Counted=Count(ItemSet_4)
    print  "Item Set 4 Counted: %s" %(ItemSet_4_Counted)

    ItemSet_4_Cutted=Cut(min_support,ItemSet_4_Counted)
    print  "Item Set 4 Cutted:  %s "  % (ItemSet_4_Cutted)

