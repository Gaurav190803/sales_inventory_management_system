import mysql.connector as con

sql_password = "g"

mydb = con.connect(host = "localhost", user = "root",password = sql_password)
cursor = mydb.cursor()

try:
    cursor.execute("create database sales_inventory;")
    print("Database created successfully!")
except:
    pass

try:
    cursor.execute("use sales_inventory;")
except:
    pass

try:
    cursor.execute("create table user_detail(name varchar(50),phone_num varchar(10),username varchar(20),password varchar(20));")
    print("user_detail table created successfully")
except:
    pass

try:
    cursor.execute('insert into user_detail values("admin","8766335630","admin","admin");')
    cursor.execute('insert into user_detail values("sample","1234567890","user","user");')
except:
    pass

try:
    cursor.execute("create table inventory(product_id int,product_name varchar(30),product_stock int,mfg_date date,exp_date date,price int);")
    print("inventory table created successfully")
except:
    pass

try:
    cursor.execute('insert into inventory values(1,"mango",20,"2023-03-23","2023-03-29",100)')
except:
    pass


print("-------------------------------")
print("run sales_inventory.py")
print("username - admin or user")
print("password - admin or user")
print("-------------------------------")
mydb.commit();
