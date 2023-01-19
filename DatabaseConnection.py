import sqlite3
import tkinter
root = tkinter.Tk()
#Create database or Connect to one database
da = sqlite3.connect('CarRentalSystemDB')


#Create Cursor to  access rows of database
c = da.cursor()

# c.execute(""" CREATE TABLE addresses (
#     first_name text,
#     second_name text,
#     zipcode integer
#     )
#     """)
root.title("Car Rental System")
f_name = tkinter.Entry(root,width=30)
f_name.grid(row=0 ,column =6 ,padx=20)

l_name = tkinter.Entry(root,width=30)
l_name.grid(row=1 ,column =6 ,padx=20)

zip_code = tkinter.Entry(root,width=30)
zip_code.grid(row=2 ,column =6 ,padx=20)

root.mainloop()



da.commit()

da.close()
