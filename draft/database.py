import sqlite3

   

def showallaccounts():
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    c.execute("SELECT acc_id, * FROM accounts")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close() 


def addaccount(fullname, initialbalance):
   
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
 
    c.execute("INSERT INTO accounts (full_name,initialBalance) VALUES (?,?)",(fullname, initialbalance))
    conn.commit()
    conn.close()
    
def deleteaccount(id):
    
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("DELETE from accounts where acc_id = (?)", id)
    conn.commit()
    conn.close()
    
    
def showalltransactions():
    conn = sqlite3.connect("customer.db")

    c = conn.cursor()
    
    c.execute("SELECT acc_id, * FROM transactions")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close() 

def addtransaction(accountid, transaction, amount):
   
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
 
    c.execute("INSERT INTO transactions (accountid, trasaction_date, amount) VALUES (?,?,?)",(accountid, transaction, amount))
    conn.commit()
    conn.close()
