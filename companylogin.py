from tkinter import *
import dbmswork
import create_account
import mainpagewindow
import tkinter.messagebox
def main():
    window=Tk()
    app=Login_window(window)
    # window.config(bg='red')
    window.mainloop()
class Login_window:
    def __init__(self,master):
        self.master=master
        self.master.title("Login Page")
        self.master.geometry("800x500")
        self.master.config(bg="light blue")
        quote='''a little 
PROGRESS
EACH DAY
adds up to
BIG
results!'''
        self.lblfr=LabelFrame(self.master,width=450,height=90,relief='sunken',bg='pink',bd=5)
        self.lblfr.place(x=0,y=0,height=500,width=450)
        self.lblimg=Label(self.lblfr,text=quote,font=("Freestyle Script",45,"bold"),fg="purple",bg="violet",height=200,width=200)
        self.lblimg.place(x=0,y=0,height=500,width=450)
        self.lblimg.pack(expand=True)

        self.frame=Frame(self.master,bg="orange")
        self.frame.place(x=450,y=0,width=350,height=500)
       
        self.LoginFrame1 = LabelFrame(self.frame,width=350,height=90,relief='sunken',bg='yellow',bd=10)
        self.LoginFrame1.pack()

        self.lb1=Label(self.LoginFrame1,text="Login",width=350,height=80,font=('Harrington',45,'bold'),bg="yellow")
        self.lb1.place(x=0,y=0,height=80,width=350)

        self.Username = StringVar()
        self.Password= StringVar()

        self.lbUsrId=Label(self.frame,text="User ID : ",bg="orange",font=('Kristen ITC',18,'bold'))
        self.lbUsrId.place(x=0,y=130,height=30,width=150)
        self.txtUsrId=Entry(self.frame,font=('Kristen ITC',10),textvariable=self.Username)
        self.txtUsrId.place(x=170,y=130,height=30,width=170)

        self.lbPass=Label(self.frame,text="Password:",bg="orange",font=('Kristen ITC',18,'bold'))
        self.lbPass.place(x=0,y=190,height=30,width=150)
        self.txtPass=Entry(self.frame,font=('Kristen ITC',15,'bold'),show="*",textvariable=self.Password)
        self.txtPass.place(x=170,y=190,height=30,width=170)

        self.btnLogin=Button(self.frame,text="Login",bg="gold",font=('Comic Sans MS',13,'bold'),command=self.login)
        self.btnLogin.place(x=25,y=280,height=35,width=80)
        self.btnReset=Button(self.frame,text="Reset",bg="gold",font=('Comic Sans MS',13,'bold'),command=self.reset)
        self.btnReset.place(x=135,y=280,height=35,width=80)
        self.btnExit=Button(self.frame,text="Exit",bg="gold",font=('Comic Sans MS',13,'bold'),command=self.exit)
        self.btnExit.place(x=245,y=280,height=35,width=80)

        self.lbl_create=Label(self.frame,text="Click on the following button to \n CREATE a NEW ACCOUNT :",font=('Comic Sans MS',13,'bold'),fg="blue",bg="orange")
        self.lbl_create.place(x=15,y=345,height=55,width=350)
        self.btn_create_new_account=Button(self.frame,text="Create New Account",bg="pink",font=('Comic Sans MS',13,'bold'),command=self.create_acc)
        self.btn_create_new_account.place(x=55,y=420,height=35,width=250)

    def reset(self):
        self.Username.set('')
        self.Password.set('')
    def exit(self):
        exit()
    def login(self):
        uid=(self.Username.get())
        pwd=(self.Password.get())
        flag=dbmswork.chk_login(uid,pwd)
        if flag:
            self.Username.set("")
            self.Password.set("")
            self.window2=Toplevel(self.master)
            self.app=mainpagewindow.NewWindow(self.window2,uid)
        else:
            tkinter.messagebox.askyesno('Error!','Invalid UserId or Password....')
            self.Username.set("")
            self.Password.set("")
            self.txtUsrId.focus()
    def create_acc(self):
        self.create_window=Tk()
        app=create_account.Create_New_Account(self.create_window)
if __name__=="__main__":
    main()