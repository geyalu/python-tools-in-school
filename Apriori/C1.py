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

def show_column(table_name):
    db=Database()
    sql="show columns from %s" %(table_name)
    data=db.query(sql)
    for row in data:
        print row['Field']
        list_columns=[row['Field'] for row in data]
    return list_columns

def C1():
    db=Database()
    sql="select item_1,item_2,item_3,item_4,item_5,item_6,item_7 from shop_test"
    db.sql(sql)
    data=db.cursor.fetchall()
    list_item=[]
    for row in data:
        row=list(row)
        list_item+=row

    print list_item
    for item in list_item:
        db=Database()
        sql="alter table c1 add %s INT DEFAULT 1" %(item)
        db.sql(sql)

    C1_Columns=show_column("c1")
    sql="insert into c1 (hering) VALUE (1)"
    db.sql(sql)
    for item in C1_Columns:
        count=list_item.count(item)
        sql="update c1 SET %s=%s" %(item,count)
        db.sql(sql)

    print "C1 Finish!"

def Cut(min_suppt,table_name):
    db=Database()
    colum_list=show_column(table_name)
    for item in colum_list:
        key=item
        sql="select %s from %s"  %(key,table_name)
        db.sql(sql)
        data=db.cursor.fetchall()
        for t in data:
            num=int(t[0])
            print num

            if num<=min_suppt:
                sql="alter table %s drop column  %s" %(table_name,key)
                db.sql(sql)
                print sql
            else:
                print num
    print "Cut Finish!"

def C2(old_tb):
    db=Database()
    column_list=show_column(old_tb)
    new_list=list(itertools.combinations(column_list,2))
    print new_list

    for i in range(len(new_list)):
        new_list[i]=new_list[i][0][:3]+'_'+new_list[i][1][:3]
        column_name=new_list[i]
        sql="alter table %s add %s INT DEFAULT 1" %('c2',column_name)
        db.sql(sql)
        print sql


    db=Database()
    sql="select item_1,item_2,item_3,item_4,item_5,item_6,item_7 from shop_test"
    db.sql(sql)
    data=db.cursor.fetchall()
    list_item=[]
    for row in data:
        row=list(row)
        #list_item+=row

        for item in new_list:
            item[]




if __name__ == '__main__':

    #C1()
    #Cut(2,'c1')
    C2('c1')



