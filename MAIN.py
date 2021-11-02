#BANKING MANAGEMENT SYSTEM MAIN SOURCE CODE 
import  mysql.connector as sql
import datetime as dt
import random
conn=sql.connect(host='localhost',user='root',passwd='',database='ankur')
cur = conn.cursor()
a='y'
while a=='y':
     print('=========================WELCOME TO NATIONAL BANK============================')
     print(dt.datetime.now())
     print('1.REGISTER')
     print()
     print('2.LOGIN')
     print()
     print('3.QUIT')
     print('=============================================================================')
     n=int(input('ENTER YOUR CHOICE='))
     print()
     if n==1:
          name=input('ENTER USERNAME=')
          print()
          passwd=int(input('ENTER A 4 DIGIT PASSWORD='))
          print()
          query="INSERT  INTO user_table values('{}',{})".format(name,passwd)
          cur.execute(query)
          conn.commit()
          print()
          print('USER CREATED SUCCESFULLY')
          print("PLEASE LOGIN NOW")
          continue
     if n==2 :
          ne=input('ENTER YOUR USERNAME=')
          print()
          pwd=int(input('ENTER YOUR 4 DIGIT PASSWORD='))
          q1="select * from user_table where username='{}' and passwrd={}".format(ne,pwd)
          cur.execute(q1)
          if cur.fetchone() is  None:
               print('INVALID USERNAME/PASSWORD TRY AGAIN')
          else:
               flag='t'
               while flag=='t':
                    print("=======================================================")
                    print("                   NATIONAL BANK")
                    print("=======================================================")
                    print('1.CREATE BANK ACCOUNT')
                    print()
                    print('2.TRANSACTION')
                    print()
                    print('3.CUSTOMER DETAILS')
                    print()
                    print('4.TRANSACTION DETAILS')
                    print()
                    print('5.CLOSE ACCOUNT')
                    print()
                    print('6.MONEY TRANSFER')
                    print()
                    print('7.QUIT')
                    print("=======================================================")
                    g=int(input('ENTER YOUR CHOICE(1/2/3/4/5/6/7)='))
                    print()
                    if g==1:
                         print("===============================================")
                         print("      NATIONAL BANK CREATE ACCOUNT SYSTEM")
                         print("===============================================")
                         acc_no=random.randrange(1,99000)
                         nm=input('ENTER YOUR ACCOUNT NAME=')
                         ph=int(input('ENTER YOUR PHONE NUMBER='))
                         add=input('ENTER YOUR ADDRESS=')
                         cr=int(input('ENTER YOUR CREDIT AMOUNT='))
                         q2="Select * from customer_details where acct_no={}".format(acc_no)
                         cur.execute(q2)
                         if cur.fetchone() is None:
                              ind="INSERT  INTO customer_details values({},'{}',{},'{}',{})".format(acc_no,nm,ph,add,cr)
                              cur.execute(ind)
                              print('ACCOUNT CREATED SUCCESSFULLY!!!!!')
                              print("YOUR ACCOUNT NO IS-",acc_no)
                              conn.commit()
                         else:
                              print("ACCOUNT NUMBER ALREADY EXISTS! TRY AGAIN")
                    elif g==2:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("MAKE A TRANSACTION")
                         print("===============================================")
                         ac=int(input('ENTER YOUR ACCOUNT NUMBER='))
                         cur.execute('select * from customer_details where acct_no={}'.format(ac))
                         data=cur.fetchall()
                         conn.commit()
                         if cur.rowcount==0:
                              print('ACCOUNT NUMBER INVALID')
                         else:
                              print('1.WITHDRAW AMOUNT')
                              print()
                              print('2.ADD AMOUNT')
                              print()
                              x=int(input('ENTER YOUR CHOICE='))
                              if x==1:
                                   amt=int(input('ENTER WITHDRAWAL AMOUNT='))
                                   cur.execute('update customer_details set cr_amt=cr_amt -{} where acct_no={}'.format(amt,ac))
                                   q="INSERT  INTO transactions (acct_no,date,withdrawal_amt) values ({} , '{}' , {}) ".format(ac,dt.datetime.today(),amt)
                                   cur.execute(q)
                                   conn.commit()
                                   print('ACCOUNT UPDATED SUCCESFULLY!!!!!')
                              elif x==2:
                                   amnt=int(input('ENTER AMOUNT TO BE ADDED='))
                                   cur.execute('update customer_details set  cr_amt=cr_amt+{}  where acct_no={}'.format(amnt,ac))
                                   qr="INSERT  INTO transactions (acct_no,date,amount_added) values ({} , '{}' , {}) ".format(ac,dt.datetime.today(),amnt)
                                   cur.execute(qr)
                                   conn.commit()
                                   print('ACCOUNT UPDATED SUCCESFULLY!!!!!')
                              else:
                                   print("INVALID CHOICE! SESSION ABORTED!")
                    elif g==3:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("CUSTOMER DETAILS")
                         print("===============================================")
                         acc=int(input('ENTER YOUR ACCOUNT NUMBER='))
                         cur.execute('select * from customer_details where acct_no={}'.format(acc))
                         if cur.fetchone() is  None:
                              print('INVALID ACCOUNT NUMBER')
                         else:
                              cur.execute('select * from customer_details where acct_no={}'.format(acc))
                              data=cur.fetchall()
                              print("%10s"%"ACCOUNT NO","%10s"%"ACCOUNT NAME","%10s"%"PHONE NUMBER","%20s"%"ADDRESS","%10s"%"cr_amt")
                              for i in data:
                                   print("%10s"%i[0],"%10s"%i[1],"%10s"%i[2],"%20s"%i[3],"%10s"%i[4])
                    
                    elif g==4:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("TRANSACTION DETAILS")
                         print("===============================================")
                         acn=int(input('ENTER YOUR ACCOUNT NUMBER='))
                         cur.execute('select * from customer_details where acct_no={}'.format(acn))
                         if cur.fetchone() is None:
                              print('INVALID ACCOUNT NUMBER! ')
                         else:
                              cur.execute('select * from transactions where acct_no={}'.format(acn))
                              data=cur.fetchall()
                              print("%20s"%"ACCOUNT NO","%20s"%"DATE","%20s"%"WITHDRAWAL AMOUNT","%20s"%"AMOUNT ADDED")
                              for i in data:
                                   print("%20s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3])
                                     
                               

                    elif g==5:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("CLOSE ACCOUNT SYSTEM")
                         print("===============================================")
                         print('CLOSE YOUR ACCOUNT')
                         acc_no=int(input('ENTER YOUR ACCOUNT NUMBER='))
                         cur.execute('select * from customer_details where acct_no={}'.format(acc_no))
                         data=cur.fetchall()
                         conn.commit()
                         if cur.rowcount==0:
                              print('ACCOUNT NUMBER INVALID')
                         else:
                              qer='select* from customer_details where acct_no={}'.format(acc_no)
                              cur.execute(qer)
                              dat=cur.fetchall()
                              print("YOUR ACCOUNT DETAILS ARE:-")
                              for i in dat:
                                   print("ACCOUNT NO-", i[0])
                                   print()
                                   print("ACCOUNT NAME -",i[1])
                                   print()
                                   print("PHONE NUMBER-", i[2])
                                   print()
                                   print("ADDRESS-",i[3])
                                   print()
                                   print("CREDIT AMOUNT-",i[4])
                                   nb=input("ARE YOU SURE YOU WANT TO CLOSE YOUR ACCOUNT?(y/n):")
                                   if nb=='y':
                                        cur.execute('delete from customer_details where acct_no={}'.format(acc_no) )
                                        print('ACCOUNT CLOSED SUCCESFULLY')
                                   elif nb=='n':
                                        print("ACCOUNT NOT CLOSED!")
                                        print("PLEASE CONTINUE WITH YOUR BANKING OPERATIONS")
                                   else:
                                        print("INVALID CHOICE! SESSION ABORTED!")

                    elif g == 6:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("MONEY TRANSFER SYSTEM")
                         print("1.INTRA BANK MONEY TRANSFER")
                         print("2.INTER BANK MONEY TRANSFER")
                         print("===============================================")
                         t=int(input("ENTER YOUR CHOICE(1/2):"))
                         if t==1:
                              a4=int(input("ENTER YOUR ACCOUNT NUMBER:"))
                              a5=int(input("ENTER THE ACCOUNT NUMBER WHERE MONEY IS TO BE TRANSFERRED:"))
                              q3="SELECT* FROM CUSTOMER_DETAILS WHERE ACCT_NO={}".format(a5)
                              cur.execute(q3)
                              if cur.fetchone() is None:
                                   print("ACCOUNT NUMBER DOES NOT EXISTS!")
                              else:
                                   ame=int(input("ENTER THE AMOUNT TO BE TRANSFERRED:"))
                                   q5="UPDATE CUSTOMER_DETAILS SET cr_amt= cr_amt-{} WHERE ACCT_NO={}".format(ame,a4)
                                   q4="UPDATE CUSTOMER_DETAILS SET cr_amt=cr_amt+{} WHERE ACCT_NO={}".format(ame,a5)
                                   cur.execute(q4)
                                   cur.execute(q5)
                                   conn.commit()
                                   print("AMOUNT TRANSFERRED SUCCESFULLY")
                         elif t==2:
                              bank=input("ENTER THE NAME OF THE BANK:")
                              ax=int(input("ENTER YOUR ACCOUNT NUMBER:"))
                              q7="SELECT* FROM CUSTOMER_DETAILS WHERE ACCT_NO={}".format(ax)
                              cur.execute(q7)
                              if cur.fetchone() is None:
                                   print("ACCOUNT NUMBER DOES NOT EXIST:")
                              else:
                                   acno=int(input("ENTER THE ACCOUNT NUMBER WHERE MONEY TO BE TRANSFERRED:"))
                                   money=int(input("ENTER AMOUNT TO BE TRANSFERRED:"))
                                   q8="UPDATE CUSTOMER_DETAILS SET cr_amt=cr_amt-{} WHERE ACCT_NO={}".format(money,ax)
                                   cur.execute(q8)
                                   conn.commit()
                                   print("YOUR REQUEST WILL BE PROCESSED SHORTLY!")
                         else:
                              print("INVALID CHOICE!")
                    elif g==7:
                         print("===============================================")
                         print("NATIONAL BANK")
                         print("THANK YOU FOR USING OUR SERVICES")
                         print("HOPE TO SEE YOU AGAIN")
                         print("===============================================")
                         break
                    else:
                         print("INVALID CHOICE! TRY AGAIN")
     break
     if n==3:
          print("THANK YOU")
          print("QUITTING..")
          break
     else:
          print("INVALID CHOICE! TRY AGAIN")
