#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
conn=sqlite3.connect('BBQ.db')
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS meat")
cursor.execute('''
               CREATE TABLE IF NOT EXISTS meat(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   price INTEGER,
                   quantity INTEGER
                   )''')
               
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('chiken',30,5)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('beef',55,10)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('pork',40,15)")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("肉類列表:")
for BBQ in meat:
    print(BBQ)
    
cursor.execute("UPDATE meat SET price=35 WHERE name='pork'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("肉類列表:")
for BBQ in meat:
    print(BBQ)
    
cursor.execute("UPDATE meat SET quantity=30 WHERE name='chiken'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("肉類列表:")
for BBQ in meat:
    print(BBQ)

cursor.execute("DELETE FROM meat WHERE price='40'")
conn.commit()
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("肉類列表:")
for BBQ in meat:
    print(BBQ)



# In[ ]:




