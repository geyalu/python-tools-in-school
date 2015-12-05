import MySQLdb

conn=MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='1234',
        db ='apri',
        )
cur=conn.cursor()

def insert_db(filepath):
    fd = file(filepath)
    lines=fd.readlines()

    list=[]
    i=0

    for line in lines:
        line=line.strip('\n')

        if len(list)==7:

            print list

            sql="insert INTO shop (item_1,item_2,item_3,item_4,item_5,item_6,item_7) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,list)
            conn.commit()
            list=[]
            temp=line[2:]
            list.append(temp)

        else:

            temp=line[2:]
            list.append(temp)

if __name__ == '__main__':

    table_name="shop"
    sql="create TABLE %s (person INT(10) primary key not  null  auto_increment," \
        "item_1 VARCHAR (50)," \
        "item_2 VARCHAR (50)," \
        "item_3 VARCHAR (50)," \
        "item_4 VARCHAR (50)," \
        "item_5 VARCHAR (50)," \
        "item_6 VARCHAR (50)," \
        "item_7 VARCHAR (50))" %(table_name)

    cur.execute(sql)
    conn.commit()

    insert_db(r'D:\shoptest2.txt')