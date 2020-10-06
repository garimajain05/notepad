import sqlite3
def Select_Query(dbnm,query):
    connection=sqlite3.connect(dbnm)
    cur=connection.cursor()
    cur.execute(query)
    row=cur.fetchall()
    connection.commit()
    connection.close()
    return row
def Create_Query(dbnm,query):
        connection=sqlite3.connect(dbnm)
        cur=connection.cursor()
        cur.execute(query)
        connection.commit()
        connection.close()

def chk_login(uid,pwd):
    query="select * from details"
    data_list=Select_Query("project.db",query)
    flag=False
    length=len(data_list)
    for i in range(length):
        # print(list[i][0],list[i][1])
        if uid==data_list[i][0] and pwd==data_list[i][1]:
            flag=True
    return flag    
def chk_uid(uid):
        query="select * from details"
        data_list=Select_Query("project.db",query)
        flag=False
        length=len(data_list)
        for i in range(length):
                # print(list[i][0],list[i][1])
                if uid==data_list[i][0]:
                        flag=True
        return flag
def create_new_acc(uid,pwd,contact,add,eid,nm):
        cntct=int(contact)
        query=f'insert into details values("{uid}","{pwd}",{cntct},"{add}","{eid}","{nm}")'
        Create_Query("project.db",query)
        return True

def customer_info(uid):
        query=f"select * from details where UserId={uid}"
        info=Select_Query("project.db",query)
        return info