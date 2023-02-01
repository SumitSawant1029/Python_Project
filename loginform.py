from tkinter import *
from sqlite3 import *
from PIL import ImageTk,Image
# import my_canvas
root = Tk()
root.title('Car Rental System')
root.geometry('925x500+300+200')
root.iconbitmap('car.ico')
root.resizable(False,False)
root.config(bg='#fff')

img1 = PhotoImage(file='login3.png')
lab1 = Label(root,image=img1,bg='white').place(x=50,y=50)

frame1 = Frame(root,width=350,height=350,bg='white')
frame1.place(x=480,y=70)

lab2 = Label(frame1,text='SIGN UP',fg='#1CC0A9',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
lab2.place(x=130,y=5)

def on_enter(e):
    user.delete(0,END)
def on_leave(e):
    user.insert(0,'Username')

def on_enter1(e):
    pass1.delete(0,END)
def on_leave1(e):
    pass1.insert(0,'Password')

user = Entry(frame1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
user.place(x=90,y=100)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

pass1 = Entry(frame1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,))
pass1.place(x=90,y=160)
pass1.insert(0,'Password')
pass1.bind('<FocusIn>',on_enter1)
pass1.bind('<FocusOut>',on_leave1)

log_in = Button(frame1,text='Log In',border=0,borderwidth=0.5,width=15,font=9,fg='white',bg='#1CC0A9',cursor='hand2')
log_in.place(x=120,y=205)

my_canvas=Canvas(frame1,width=228,height=2.0,bg='#1CC0A9',highlightthickness=0)
my_canvas.place(x=90,y=122)

my_canvas=Canvas(frame1,width=228,height=2.0,bg='#1CC0A9',highlightthickness=0)
my_canvas.place(x=90,y=182)

lab6=Label(frame1,text="Don't have an account?",fg='black',bg='white')
lab6.place(x=120,y=250)

sign_up =Button(frame1,text='Sign Up',bg='white',fg='#1CC0A9',border=0,cursor='hand2')
sign_up.place(x=247,y=250)
root.mainloop()
