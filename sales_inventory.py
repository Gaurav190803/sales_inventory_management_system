import tkinter as tk
import mysql.connector as con
import time
from tkinter import messagebox

sql_password = "g"


class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
        container = tk.Frame(self,height = 1920,width = 1080)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        self.container = container
        self.container.grid_columnconfigure(0, weight = 1)
		# initializing frames to an empty array
       
        self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
        for F in (LoginPage,signUp,sales_inventory_admin,sales_inventory,addItem,updatePrice,deleteItem,view_tables_admin,view_tables):

            frame = F(self.container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(LoginPage)

	# to display the current frame passed as
	# parameter
    def show_frame(self, cont):
            for F in (LoginPage,signUp,sales_inventory_admin,sales_inventory,addItem,updatePrice,deleteItem,view_tables_admin,view_tables):
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row = 0, column = 0, sticky ="nsew")   
            frame = self.frames[cont]
            frame.tkraise()

# first window frame startpage

class sales_inventory_admin(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller
    
    def create_widgets(self):
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 80)

        self.addItem = tk.Button(self,text = "Add Item", command = lambda : self.controller.show_frame(addItem))
        self.addItem.pack(side = tk.TOP)

        self.update = tk.Button(self,text = "Update Item Detail",command = lambda : self.controller.show_frame(updatePrice))
        self.update.pack(side = tk.TOP)

        self.deleteItem = tk.Button(self,text = "Delete Item",command = lambda : self.controller.show_frame(deleteItem))
        self.deleteItem.pack(side = tk.TOP)

        self.viewTable = tk.Button(self,text = "View Items",command = lambda : self.controller.show_frame(view_tables_admin))
        self.viewTable.pack(side = tk.TOP)

        self.logOut = tk.Button(self,text="LogOut",command = lambda : self.controller.show_frame(LoginPage))
        self.logOut.pack(side=tk.TOP)

class addItem(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 80)
        self.productId_label = tk.Label(self, text="Product id:")
        self.productId_label.pack(side=tk.TOP)
        self.productId_entry = tk.Entry(self)
        self.productId_entry.pack(side=tk.TOP)

        # create password label and entry
        self.productName_label = tk.Label(self, text="Product name:")
        self.productName_label.pack(side=tk.TOP)
        self.productName_entry = tk.Entry(self)
        self.productName_entry.pack(side=tk.TOP)

        self.productStock_label = tk.Label(self, text="Product stock:")
        self.productStock_label.pack(side=tk.TOP)
        self.productStock_entry = tk.Entry(self)
        self.productStock_entry.pack(side=tk.TOP)

        self.productMfd_label = tk.Label(self, text="Manufacture date:")
        self.productMfd_label.pack(side=tk.TOP)
        self.productMfd_entry = tk.Entry(self)
        self.productMfd_entry.pack(side=tk.TOP)

        self.productExd_label = tk.Label(self, text="Expiry date:")
        self.productExd_label.pack(side=tk.TOP)
        self.productExd_entry = tk.Entry(self)
        self.productExd_entry.pack(side=tk.TOP)

        self.productPrice_label = tk.Label(self, text="Price:")
        self.productPrice_label.pack(side=tk.TOP)
        self.productPrice_entry = tk.Entry(self)
        self.productPrice_entry.pack(side=tk.TOP)


        
        # create login button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.TOP)

        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(sales_inventory_admin))
        self.back_button.pack(side=tk.TOP)

    
    def submit(self):
        product_id = self.productId_entry.get()
        product_name = self.productName_entry.get()
        product_stock = self.productStock_entry.get()
        product_mfd = self.productMfd_entry.get()
        product_exd = self.productExd_entry.get()
        product_price = self.productPrice_entry.get()

        try:
            self.cursor.execute(f'insert into inventory values ("{product_id}","{product_name}","{product_stock}","{product_mfd}","{product_exd}","{product_price}");')
            messagebox.showinfo("Message","Item added succesfully.")
            self.mydb.commit()
            self.productId_entry.delete(0,tk.END)
            self.productName_entry.delete(0,tk.END)
            self.productStock_entry.delete(0,tk.END)
            self.productMfd_entry.delete(0,tk.END)
            self.productExd_entry.delete(0,tk.END)
            self.productPrice_entry.delete(0,tk.END)
        
        except:
            messagebox.showinfo("Message","Please check details.")
        
         
    
class updatePrice(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller
    def create_widgets(self):
        self.space = tk.Label(self, text="")
        self.space.place(relx = 0, rely = 0, anchor = tk.CENTER)
        self.space.pack(side=tk.TOP,pady = 200)
        self.productId_label = tk.Label(self, text="Product id:")
        self.productId_label.pack(side=tk.TOP)
        self.productId_entry = tk.Entry(self)
        self.productId_entry.pack(side=tk.TOP)

        self.productName_label = tk.Label(self, text="Product name:")
        self.productName_label.pack(side=tk.TOP)
        self.productName_label.config(state = "disabled")
        self.productName_entry = tk.Entry(self)
        self.productName_entry.pack(side=tk.TOP)
        self.productName_entry.config(state = "disabled")

        self.productStock_label = tk.Label(self, text="Product stock:")
        self.productStock_label.pack(side=tk.TOP)
        self.productStock_label.config(state = "disabled")
        self.productStock_entry = tk.Entry(self)
        self.productStock_entry.pack(side=tk.TOP)
        self.productStock_entry.config(state = "disabled")

        self.productMfd_label = tk.Label(self, text="Manufacture date:")
        self.productMfd_label.pack(side=tk.TOP)
        self.productMfd_label.config(state = "disabled")
        self.productMfd_entry = tk.Entry(self)
        self.productMfd_entry.pack(side=tk.TOP)
        self.productMfd_entry.config(state = "disabled")

        self.productExd_label = tk.Label(self, text="Expiry date:")
        self.productExd_label.pack(side=tk.TOP)
        self.productExd_label.config(state = "disabled")
        self.productExd_entry = tk.Entry(self)
        self.productExd_entry.pack(side=tk.TOP)
        self.productExd_entry.config(state = "disabled")

        self.productPrice_label = tk.Label(self, text="Price:")
        self.productPrice_label.pack(side=tk.TOP)
        self.productPrice_label.config(state = "disabled")
        self.productPrice_entry = tk.Entry(self)
        self.productPrice_entry.pack(side=tk.TOP)
        self.productPrice_entry.config(state = "disabled")

        
        # create login button
        self.enter = tk.Button(self,text="Get data",command = self.get_data)
        self.enter.pack(side = tk.TOP)
        self.update_button = tk.Button(self, text="Update data", command=self.update)
        self.update_button.pack(side=tk.TOP)
        self.update_button.config(state="disabled")
        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(sales_inventory_admin))
        self.back_button.pack(side=tk.TOP)

    def get_data(self):
        self.productName_entry.config(state = "normal")
        self.productStock_entry.config(state = "normal")
        self.productMfd_entry.config(state = "normal")
        self.productExd_entry.config(state = "normal")
        self.productPrice_entry.config(state = "normal")
        self.update_button.config(state="normal")
        self.productName_entry.delete(0,tk.END)
        self.productStock_entry.delete(0,tk.END)
        self.productMfd_entry.delete(0,tk.END)
        self.productExd_entry.delete(0,tk.END)
        self.productPrice_entry.delete(0,tk.END)
        product_id = int(self.productId_entry.get())
        try:
            self.cursor.execute(f"Select * from inventory where product_id = {product_id};")
            for x in self.cursor:
                self.product_name = x[1]
                self.product_stock = x[2]
                self.product_mfd = x[3]
                self.product_exd = x[4]
                self.product_price = x[5]

            self.productName_entry.insert(0,self.product_name)
            self.productStock_entry.insert(0,self.product_stock)
            self.productMfd_entry.insert(0,self.product_mfd)
            self.productExd_entry.insert(0,self.product_exd)
            self.productPrice_entry.insert(0,self.product_price)

            del(self.product_name)
            del(self.product_stock)
            del(self.product_mfd)
            del(self.product_exd)
            del(self.product_price)
    

        except:
            messagebox.showinfo("Message","Enter correct product id.")
        
        
                # create login button
    def update(self):
        try:
            product_id = self.productId_entry.get()
            product_name = self.productName_entry.get()
            product_stock = self.productStock_entry.get()
            product_mfd = self.productMfd_entry.get()
            product_exd = self.productExd_entry.get()
            product_price = self.productPrice_entry.get()
            self.cursor.execute(f'update inventory set product_name = "{product_name}",product_stock = {int(product_stock)},mfg_date = "{product_mfd}",exp_date = "{product_exd}",price = {int(product_price)} where product_id = {int(product_id)};')
            messagebox.showinfo("Message","Updated Successfully")
            self.mydb.commit()
            self.productName_entry.delete(0,tk.END)
            self.productStock_entry.delete(0,tk.END)
            self.productMfd_entry.delete(0,tk.END)
            self.productExd_entry.delete(0,tk.END)
            self.productPrice_entry.delete(0,tk.END)
            self.productName_entry.config(state = "disabled")
            self.productStock_entry.config(state = "disabled")
            self.productMfd_entry.config(state = "disabled")
            self.productExd_entry.config(state = "disabled")
            self.productPrice_entry.config(state = "disabled")
            self.update_button.config(state="disabled")
        except:
            messagebox.showinfo("Message","Check details and try again.")
        self.controller.show_frame(sales_inventory_admin)

class deleteItem(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 200)
        self.productId_label = tk.Label(self, text="Product id:")
        self.productId_label.pack(side=tk.TOP)
        self.productId_entry = tk.Entry(self)
        self.productId_entry.pack(side=tk.TOP)
        self.delete = tk.Button(self,text="Delete",command = self.delete)
        self.delete.pack(side = tk.TOP)
        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(sales_inventory_admin))
        self.back_button.pack(side=tk.TOP)

    def delete(self):
        product_id = int(self.productId_entry.get())
        try:
            self.cursor.execute(f'Delete from inventory where product_id = {product_id};')
            messagebox.showinfo("Message",f"product_id: {product_id} deleated successfully")
            self.mydb.commit()
        except:
            messagebox.showinfo("Message","Product id incorrect or does not exist")

class sales_inventory(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller
    
    def create_widgets(self):
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 200)
        self.viewTable = tk.Button(self,text = "View Items",command = lambda : self.controller.show_frame(view_tables))
        self.viewTable.pack(side = tk.TOP)
        self.logOut = tk.Button(self,text="LogOut",command = lambda : self.controller.show_frame(LoginPage))
        self.logOut.pack(side=tk.TOP)
        

class LoginPage(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        # create username label and entry
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 80)
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(side=tk.TOP)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(side=tk.TOP)

        # create password label and entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(side=tk.TOP)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(side=tk.TOP)

        # create login button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(side=tk.TOP)

        self.forgot_button = tk.Button(self,text="SignUp",command = lambda : self.controller.show_frame(signUp))
        self.forgot_button.pack(side=tk.TOP)


    def login(self):
        # perform login validation here
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.cursor.execute(f'select password from user_detail where username = "{username}";')
            for x in self.cursor:
                password_true = x
            if password == password_true[0]:
                if username == "admin":
                    messagebox.showinfo("Message","Login succesfull! Welcome admin.")
                    self.controller.show_frame(sales_inventory_admin)
                else:
                    messagebox.showinfo("Message","Login succesfull! Welcome Customer.")
                    self.controller.show_frame(sales_inventory)
                self.username_entry.delete(0,tk.END)
                self.password_entry.delete(0,tk.END)
            else:
                result = "Invalid username or password."
                messagebox.showinfo("Message",result)
        except:
            result = "Invalid username or password."
            messagebox.showinfo("Message",result)
        
            
class signUp(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        # create username label and entry
        self.space = tk.Label(self, text="")
        self.space.pack(side=tk.TOP,pady = 80)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(side=tk.TOP)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side=tk.TOP)

        self.phone_label = tk.Label(self, text="Phone_no:")
        self.phone_label.pack(side=tk.TOP)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack(side=tk.TOP)
    
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(side=tk.TOP)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(side=tk.TOP)

        # create password label and entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(side=tk.TOP)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(side=tk.TOP)

        # create login button
        self.signUp_button = tk.Button(self, text="Sign Up", command=self.signUp)
        self.signUp_button.pack(side=tk.TOP)

        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(LoginPage))
        self.back_button.pack(side=tk.TOP)


    def signUp(self):
        # perform login validation here
        username = self.username_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        try:
            self.cursor.execute(f'insert into user_detail values ("{name}","{phone}","{username}","{password}");')
            result = "SignUp sucessful Please Login"
            self.mydb.commit()
        except:
            result = "Invalid details."
        messagebox.showinfo("Message",result)
        self.controller.show_frame(LoginPage)
class view_tables(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        self.cursor.execute("Select * from inventory")
        r_set = self.cursor.fetchall()
        e=tk.Label(self,width=15,text='productId',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e=tk.Label(self,width=15,text='productName',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e=tk.Label(self,width=15,text='productStock',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e=tk.Label(self,width=15,text='manufactureDate',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        e=tk.Label(self,width=15,text='expiryDate',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=4)
        e=tk.Label(self,width=15,text='price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=5)
        i=1
        j = 5
        for item in r_set:
            for k in range(len(item)):
                e = tk.Entry(self,width = 15,foreground = 'blue')
                e.grid(row = i,column = k)
                e.insert(tk.END,item[k])
            i+=1
        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(sales_inventory))
        self.back_button.grid(row = i+1,column = j+1)

class view_tables_admin(tk.Frame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.mydb = con.connect(host = "localhost", user = "root",password = sql_password)
        self.cursor = self.mydb.cursor()
        self.master = master
        self.cursor.execute("use sales_inventory;")
        self.create_widgets()
        self.controller = controller

    def create_widgets(self):
        self.cursor.execute("Select * from inventory")
        r_set = self.cursor.fetchall()
        e=tk.Label(self,width=15,text='productId',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e=tk.Label(self,width=15,text='productName',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e=tk.Label(self,width=15,text='productStock',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e=tk.Label(self,width=15,text='manufactureDate',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        e=tk.Label(self,width=15,text='expiryDate',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=4)
        e=tk.Label(self,width=15,text='price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=5)
        i=1
        j = 5
        for item in r_set:
            for k in range(len(item)):
                e = tk.Entry(self,width = 15,foreground = 'blue')
                e.grid(row = i,column = k)
                e.insert(tk.END,item[k])
            i+=1
        self.back_button = tk.Button(self, text="Back",command =  lambda : self.controller.show_frame(sales_inventory_admin))
        self.back_button.grid(row = i+1,column = j+1)


if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()