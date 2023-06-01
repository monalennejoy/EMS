import sqlite3

def connect():
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, aydi integer, name text, address text, \
                     gender text, mobno integer,email text, department text, designation text)")

       conn.commit()
       conn.close()

def insert(aydi = " ", name = " ", address = " ", gender = " ", mobno = " ", email = " ", department = " ", designation = " "):
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO Employee VALUES (NULL,?,?,?,?,?,?,?,?)", (aydi, name, address, gender , mobno, email, department, designation))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM Employee")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM Employee WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,aydi = " ", name = " ", address = " ", gender = " ", mobno = " ", email = " ", department = " ", designation = " "):
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("UPDATE Employee SET aydi = ? OR name = ? OR addess = ? OR gender = ? OR mobno = ? OR email = ? OR department = ? OR designation = ?", \
                   (aydi, name, address, gender , mobno, email, department, designation))

       conn.commit()
       conn.close()

def search(aydi = " ", name = " ", address = " ", gender = " ", mobno = " ", email = " ", department = " ", designation = " "):
       conn = sqlite3.connect("Employee.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM Employee WHERE aydi = ? OR name = ? OR address = ? OR gender = ? OR mobno = ? OR email = ? OR department = ? OR designation = ?", (aydi,name,address,gender,mobno,email,department,designation))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
