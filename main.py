import mysql.connector as sqltor
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform
import sys
import library_management
def clrscreen():
    if platform.system()=="Windows":
        os.system("cls")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#= = = = = = =  = = = = MAIN = = = = == = == = = = = 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    clrscreen()
    print("~~"*30)
    print("\t\t\t\tLIBRARY MANAGEMENT")
    print("~~"*30)
    print("MAIN MENU\n")
    print("1.BOOK MANAGEMENT")
    print("2.MEMBER MANAGEMENT")
    print("3.DETAILS OF ISSUED BOOK")
    print("4.RETURN ANY BOOK")
    print("5.DATABASE MANAGEMENT")
    print("6.EXIT")
    choice=int(input("ENTER YOUR CHOICE B/W 1-6 :"))
    if choice == 1:
        while True:
            print("~~"*30)
            print("\t\t\t\tBOOK MANAGEMENT")
            print("~~"*30)
            print("A. DISPLAY BOOK RECORDS")
            print("B. INSERT BOOK RECORD")
            print("C. UPDATE BOOK RECORD")
            print("D. DELETE BOOK RECORD")
            print("E. BACK TO MAIN MENU")
            n=input("ENTER YOUR CHOICE B/W A-E :")
            if n in ['a','A']:
                library_management.display_book()                
            elif n in ['b','B']:
                library_management.insert_book_record()
            elif n in ['c','C']:
                library_management.update_book_record()
            elif n in ['d','D']:
                library_management.delete_book()
            else:
                break

    elif choice==2:
        while True:
            print("~~"*30)
            print("\t\t\tMEMBER MANAGMENT")
            print("~~"*30)
            print("A. DISPLAY MEMBER(S) INFORMATION")
            print("B. UPDATE MEMBER(S) DETAILS")
            print("C. ADD NEW MEMBER(S) RECORD")
            print("D. DELETE MEMBER(S) RECORD")
            print("E. SEARCH FOR A MEMBER'S DETAILS")
            print("F. BACK TO MAIN MENU")
            n=input("ENTER YOUR CHOICE B/W A-F :")
            if n in ['a','A']:
                library_management.display_member()
            elif n in ['b','B']:
                library_management.update_member_record()
            elif n in ['c','C']:
                library_management.insert_member()
            elif n in ['d','D']:
                library_management.delete_member()
            elif n in ['e','E']:
                library_management.search_member()
            else:
                break

    elif choice==3:
        while True:
            print("~~"*30)
            print("\t\t\tMANAGMENT FOR ISSUED BOOK")
            print("~~"*30)
            print("A. DISPLAY RECORD OF BOOK ISSUED")
            print("B. ISSUE BOOK")
            print("C. BACK TO MAIN MENU")
            m=input("ENTER YOUR CHOICE B/W A-D :")
            if m in ['a','A']:
                library_management.show_issued_books()
            elif m in ['b','B']:
                library_management.issue_book()
            else:
                break

    elif choice ==4:
        while True:
            print("~~"*30)
            print("\t\t\tMANAGMENT FOR RETURN A BOOK")
            print("~~"*30)
            L=int(input("ENTER HOW MANY BOOK DO YOU WANT TO RETURN"))
            for i in range(L):
                library_management.book_return()
            print("=="*30)
            
    elif choice ==5:
        while True:
            print("~~"*30)
            print("\t\t\tDATABASE MANAGMENT")
            print("~~"*30)
            print("A. DATABASE CREATION")
            print("B. TABLE CREATION")
            print("C. LIST TABLES")
            print("D. BACK TO MAIN MENU")
            o=input("ENTER YOUR CHOICE B/W A-C :")
            if o in ['a','A']:
                library_management.create_databases()
            elif o in ['b','B']:
                library_management.create_tables()
            elif o in ['c','C']:
                library_management.show_tables()
            else:
                break

    else:
        sys.exit()