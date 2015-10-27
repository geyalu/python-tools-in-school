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

dic={('ham', 'heineken'): 0, ('turkey', 'hering'): 0, ('ham', 'corned_b'): 0, ('bourbon', 'ice_crea'): 0, ('coke', 'hering'): 0, ('turkey', 'ham'): 0, ('turkey', 'ice_crea'): 0, ('ham', 'ice_crea'): 0, ('hering', 'bourbon'): 0, ('turkey', 'bourbon'): 0, ('olives', 'heineken'): 0, ('corned_b', 'hering'): 0, ('olives', 'coke'): 0, ('heineken', 'ice_crea'): 0, ('ham', 'hering'): 0, ('turkey', 'olives'): 0, ('heineken', 'bourbon'): 0, ('corned_b', 'heineken'): 0, ('olives', 'corned_b'): 0, ('ham', 'coke'): 0, ('corned_b', 'ice_crea'): 0, ('heineken', 'hering'): 0, ('olives', 'hering'): 0, ('corned_b', 'coke'): 0, ('ham', 'bourbon'): 0, ('olives', 'ham'): 0, ('corned_b', 'bourbon'): 0, ('olives', 'bourbon'): 0, ('olives', 'ice_crea'): 0, ('hering', 'ice_crea'): 0, ('heineken', 'coke'): 0, ('turkey', 'corned_b'): 0, ('turkey', 'coke'): 0, ('coke', 'bourbon'): 0, ('turkey', 'heineken'): 0, ('coke', 'ice_crea'): 0}




def Count(dic):
    DB_table="shop_test"
    db=Database()
    sql="select item_1,item_2,item_3,item_4,item_5,item_6,item_7 from %s" %(DB_table)
    db.sql(sql)
    data=db.cursor.fetchall()
    list_item=[]
    for row in data:
        row=list(row)
        list_item+=row
        print "--- Scan Line: ---"
        print row

        for item in dic:
            lenth=len(item)
            i=0
            for x in range(lenth+1):
                if i==lenth:
                    print item
                    dic[item]=dic[item]+1
                    print "-------------------"
                    break

                if item[i] in row and i<=lenth:
                    i+=1
                else:
                    break




if __name__ == '__main__':
    Count(dic)
    print dic