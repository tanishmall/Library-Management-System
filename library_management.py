import mysql.connector as sqltor
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform
import sys
def clrscreen():
    if platform.system()=="Windows":
        os.system("cls")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#== = = = = = = = = = =BOOK MANAGEMENT = = = = = = = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def display_book():
    try:
        os.system('cls')
        conn = sqltor.connect ( user='root', passwd='', host="localhost",database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        query1 = ("SELECT * FROM book_info")
        print("==="*20)
        print("\n\n\nDISPLAYING RECORD")
        print("==="*20)
        qry='select  b_code , b_name, b_author, b_price, b_publisher , qty ,purchased_on from book_info'
        cursor.execute(qry)
        data=cursor.fetchall()
        count=cursor.rowcount
        print("TOTAL NO OF ROWS RETRIEVED FROM RESULTANTSET:",count)
        for i in data:
            print("~~"*40)
            print("BOOK CODE         :",i[0])
            print("BOOK NAME         :",i[1])
            print("BOOK'S AUTHOR     :",i[2])
            print("PUBLISHER         :",i[3])
            print("QUANTITY AVAILABLE:",i[4])
            print("PURCHASED ON      :",i[5])
            print("~~"*40)
            cursor.close()
        conn.close()
        print("="*40)
        print("ALL DATA IS DISPLAYED!!!!!!")
    except sqltor.Error as fault:
        print(fault)


def delete_book():
    try:
        conn = sqltor.connect(user='root', passwd='',host="localhost",database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        print("==="*20)
        print("\n\n\n\nDATA DELETION")
        print("==="*20)
        b_code=input("ENTER BOOK CODE OF BOOK TO BE DELETED FROM THE LIBRARY	: ")
        query="delete from book_info where b_code = %s"
        data=(b_code,)
        cursor.execute(query,data)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"RECORD(S) DELETED SUCESSFULLY.............")
    except sqltor.Error as fault:
        print(fault)



def update_book_record():
     try:
        conn = sqltor.connect(user='root',passwd='',host="localhost",database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        b_code=input("ENTER BOOK CODE OF BOOK TO BE UPDATED FROM THE LIBRARY	: ")
        query = "SELECT * FROM book_info where b_code = %s ".format(b_code)
        print("==="*20)
        print("\n\n\n\nENTER NEW DATA ")
        print("==="*20)
        b_code=int(input("ENTER BOOK CODE         :"))
        b_name=input("ENTER BOOK NAME          : ")
        b_author=input("ENTER AUTHOR'S NAME	: ")
        b_price=int(input("ENTER PRICE OF BOOK	: "))
        b_publisher=input("ENTER PUBLISHER OF BOOK	: ")
        qty=int(input("ENTER QUANTITY PURCHASED	: "))
        purchased_on=input("ENTER DATE OF PURCHASED (YYYY-MM-DD): ")   
        Qry = ("UPDATE book_info  SET b_code=%s, b_name=%s , b_author=%s ,b_price=%s, b_publisher=%s, qty=%s, purchased_on=%s WHERE b_code=%s")
        data = (b_code,b_name,b_author,b_price,b_publisher, qty, purchased_on,b_code)
        cursor.execute(Qry,data)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"RECORD(S) UPDATED SUCCESSFULLY.............")
     except sqltor.Error as fault:
         print(fault)



def insert_book_record():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        print("==="*20)
        print("\n\n\n\nENTER DATA TO BE INSERT")
        print("==="*20)
        b_code=int(input("ENTER BOOK CODE         :"))
        b_name=input("ENTER BOOK NAME          : ")
        b_author=input("ENTER AUTHOR'S NAME	: ")
        b_price=int(input("ENTER PRICE OF BOOK	: "))
        b_publisher=input("ENTER PUBLISHER OF BOOK	: ")
        qty=int(input("ENTER QUANTITY PURCHASED	:" ))
        purchased_on=input("ENTER DATE OF PURCHASED (YYYY-MM-DD): ")
        Qry = "insert into book_info values({},'{}','{}',{},'{}',{},'{}');" .format(b_code,b_name,b_author,b_price ,b_publisher ,qty, purchased_on)
        cursor.execute(Qry)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"RECORD(S) INSERTED SUCCESSFULLY.............")
    except sqltor.Error as fault:
         print(fault)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#= = = = == = = =MEMBER RECORD MANAGEMENT= = = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def display_member():
    try:
        os.system('cls')
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        query = ("SELECT * FROM member_info")
        qry='select m_no,m_name,mob_no,m_date,address from member_info'
        cursor.execute(qry)
        data=cursor.fetchall()
        count=cursor.rowcount
        print("TOTAL NUMBER OF ROWS RETRIEVED FROM RESULTANTSET:",count)
        for i in data:
            print("~~"*30)
            print("MEMBERSHIP NUMBER        :",i[0])
            print("MEMBER'S NAME            :",i[1])
            print("MOBILE NO                :",i[2])
            print("MEMBERSHIP ACTIVE DATE   :",i[3])
            print("ADDRESS                  :",i[4])
            print("~~"*30)
            print(data)
        cursor.close()
        conn.close()
        print("DONE!!!!")
    except sqltor.Error as fault:
        print(fault)


def insert_member():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE LIBRARY_MANAGEMENT")
        print("=="*20)
        print("\n\n\n\nINSERT MEMBER'S INFORMATION")
        print("=="*20)
        m_no=int(input("ENTER MEMBERSHIP ID         :"))
        m_name=input("ENTER MEMBER'S NAME           : ")
        mob_no=int(input("ENTER MOBILE NUMBER	    : "))
        print("ENTER DATE BELOW IN FORMAT(yyyy-mm-dd) ")
        m_date=input("ENTER ACTIVE MEMBERSHIPDATE:")  
        address=input("ENTER YOUR CURRENT ADDRESS   : ")
        Qry = "INSERT into member_info values({},'{}',{},'{}','{}')" .format(m_no,m_name,mob_no,m_date,address)
        cursor.execute(Qry)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"Record(s) INSERTED Successfully.............")
    except sqltor.Error as err:
        print(err)
        conn.close()


def update_member_record():
     try:
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        m_no=input("ENTER MEMBERSHIP ID TO UPDATE MEMBER'S DETAIL	: ")
        query = "SELECT * FROM member_info where m_no = %s".format(m_no)
        print("=="*20)
        print("\n\n\n\nENTER NEW DATA ")
        print("=="*20)
        m_no=int(input("enter membership id         :"))
        m_name=input("Enter member Name	        : ")
        mob_no=int(input("ENTER MOBILE NUMBER	: "))
        print("enter date in format(yyyy-mm-dd): ")
        m_date=input("Enter ACTIVE MEMBERSHIP DATE	: ")
        address=input("Enter your address	: ")
        Qry = "INSERT into member_info values({},'{}',{},'{}','{}')".format(m_no,m_name,mob_no,m_date,address)
        cursor.execute(Qry)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"RECORD(S) UPDATED SUCCESSFULLY.............")
     except sqltor.Error as fault:
         print(fault)


def delete_member():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost" ,database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        m_no=input("Enter MEMBER ID  to be deleted from the Library	: ")
        query="delete from member_info where m_no= %s"
        data=(m_no,)
        cursor.execute(query,data)
        conn.commit()
        cursor.close()
        conn.close()
        print(cursor.rowcount,"Record(s) Deleted Successfully..........")
    except sqltor.Error as fault:
        print(fault)
        conn.close()

def search_member():
    try:
        os.system('cls')
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        s=int(input("ENTER THE MEMBERSHIP ID :"))
        t=(s,)
        query = ("SELECT  * FROM member_info where m_no=%s")
        cursor.execute(query,t)
        for (m_no,m_name,mob_no,m_date,address) in cursor:
            print("~~"*30)
            print("MEMBER'S ID      :",m_no)
            print("MEMBER'S NAME    :",m_name)
            print("MEMBER MOBILE NUMBER    :",mob_no)
            print("MEMBERSHIP ACTIVATION DATE:",m_date)
            print("MEMBER'S ADDRESS:",address)
            print("~~"*30)
            print("=="*20)
        print("=="*20)
        input("Press any key to continue")
        conn.commit()
        cursor.close()
        conn.close()
    except sqltor as fault:
        print(fault)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
#= = = = = =  = = = = = = =ISSUE BOOKS= = = = = = = = = = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     


def issue_book():
    try:
        conn = sqltor.connect(user='root',passwd="",host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        print("=="*20)
        print("\nINSERT RECORD")
        print()
        try: 
            b_code=int(input("ENTER BOOK ID : "))
        except ValueError as ve:
            print("ERROR OCCUR!!!")
            print("INVALID ENTRY")
        try:
            b_name=input("ENTER BOOK NAME : ")
        except ValueError :
            print("ERROR OCCUR!!!")
            print("INVALID ENTRY")
        m_no=int(input("ENTER MEMBERSHIP ID :"))
        m_name=input("ENTER YOUR NAME:")
        try:
             if m_name.isdigit():
                print("ERROR OCCUR!!!")
                print("INVALID ENTRY")
                issue_book()
        except :
             pass
        
        try:
            issue_no=int(input("ENTER ISSUE NUMBER"))
        except:
            print("INVALID ISSUE NUMBER")
            print("TRY AGAIN")
            issue_book()
        doi=input("ENTER DATE OF ISSUE IN FORMAT (yyyy-mm-dd):")
        try:
            if doi.isalpha():
                print("ERROR OCCUR:INVALID INPUT")
                issue_book()
        except :
                print("INVALID DATE!!!")
                print("TRY TO WRITE IN GIVEN FORMAT (YYYY-MM-DD)")
                issue_book()
        
        
        try:
            q=(b_code,)
            qry=("SELECT  qty FROM book_info WHERE b_code=%s")
            cursor.execute(qry,q)
            Z=cursor.fetchall()
            l=len(Z)
            x=Z[0][0]
            if x==0:
                print()
                print("SORRY",b_name,"IS CURRENTLY NOT AVAILABLE")
                print()
            else:
                Qry = "INSERT INTO book_issue (b_code,b_name,m_no,m_name,issue_no,doi) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (b_code,b_name,m_no,m_name,issue_no,doi)
                cursor.execute(Qry,data)
                cursor.execute("SELECT b_code FROM BOOK_INFO")
                d=cursor.fetchall()   
                for i in range(len(d)):
                    if d[i]==q:
                        sql =cursor.execute("UPDATE BOOK_INFO SET qty=qty-1")
                        cursor.execute(sql)
                        conn.commit()
                        print()
                        print("BOOK ISSUED!!")
                            
        except:
            print("SORRY REQUESTED BOOK FOR ISSUE IS CURRENTLY NOT AVAILABLE")
    except sqltor.Error as fault:
        print(fault)
        
def show_issued_books():
    try:    
        os.system('cls')
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        cursor.execute("SELECT book_issue.b_code , book_issue.b_name, member_info.m_no, member_info.m_name,doi FROM book_issue, member_info;")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("TOTAL NO OF ROWS RETRIEVED FROM RESULTANTSET:",count)
        for i in data:
            print("~~"*30)
            print("BOOK CODE        :",i[0])
            print("BOOK NAME        :",i[1])
            print("MEMBERSHIP IP    :",i[2])
            print("MEMBER NAME      :",i[3])
            print("DATE OF ISSUE    :",i[4])
            print("~~"*30)
        cursor.close()
        conn.close()
    except sqltor.Error as fault:
        print(fault)
        conn.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#= = = == = =  = = = = =RETURN BOOK = = = = = = = = = = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def book_return():
    conn = sqltor.connect(user='root',passwd='',host="localhost",database='library_management')
    cursor = conn.cursor()
    cursor.execute("USE library_management")
    cursor.execute("SELECT b_code FROM book_issue")
    a=cursor.fetchall()
    b_code=int(input("ENTER BOOK ID WHICH YOU WANT TO RETURN:"))
    S=(b_code,)
    cursor.execute("SELECT * FROM BOOK_ISSUE where b_code='{}'  ".format(b_code))
    data=cursor.fetchall()
    lent=len(data)
    try:
        qry="DELETE FROM BOOK_ISSUE WHERE b_code=%s"
        cursor.execute(qry,S)
        cursor.execute("UPDATE book_info SET qty=qty+1")
        print("BOOK RETURNED TO LIBRARY")
        print("~~"*30)
        conn.commit()
    except:
        print("FIRSTLY YOU HAVE TO ISSUE THAT BOOK!!!!")
        print("BOOK HAS NOT BEEN ISSUED FROM LIBRARY ")
        print()
        pass
    else:
        pass


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#= = = = = = =  = = = = DATABASE SETUP = = = = == = == = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_databases():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE if not exists library_management")
        print("database created")
    except sqltor.Error as fault:
        print("fault")

def create_tables():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        print("please wait for a sec!!!!!")
        print("CREATING BOOK_INFO TABLE")
        print(".....")
        query='''create table if not exists book_info(b_code int(7) \
            primary key,\
            b_name varchar(200),\
            b_author varchar(200),\
            b_price double(10,2) ,\
            b_publisher varchar(100), \
            qty int(5),\
            purchased_on date) '''
        cursor.execute(query)
        print("BOOK_INFO SUCCESFULLY CREATED!!")
        print("NOW,")
        print("CREATING MEMBER_INFO TABLE")
        print(".....")
        Qry='''create table if not exists member_info(m_no int(7) \
            primary key,\
            m_name varchar(100),\
            mob_no int(10),\
            m_date date,\
            address varchar(300) )'''
        cursor.execute(Qry)
        print("MEMBER_INFO SUCESSFULLY CREATED!!!")
        qry='''create table if not exists book_issue(b_code int(7), b_name varchar(200), m_no int(4), m_name char(60) ,issue_no int(10) primary key ,doi date , dor date)'''
        cursor.execute(qry)
        print("BOOK_ISSUE CREATED SUCESSFULLY")
        print("....")
    except sqltor.Error as fault:
        print("fault :",fault)
        conn.close()
        

def show_tables():
    try:
        conn = sqltor.connect(user='root',passwd='',host="localhost", database='library_management')
        cursor = conn.cursor()
        cursor.execute("USE library_management")
        print("showing tables")
        cursor.execute("show tables")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("TOTAL NO OF ROWS RETRIEVED FROM RESULTANTSET:",count)
        for row in data:
            print(row)
        
    except sqltor.Error as fault:
        print(fault)

