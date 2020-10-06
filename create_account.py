from tkinter import *
import dbmswork
import tkinter.messagebox
class Create_New_Account:
    def __init__(self,master):
        self.master=master
        self.master.geometry("600x600")
        self.master.config(bg="light blue")        
        self.master.title("Create New Account")
        
        self.UserId=StringVar()
        
        self.lb1=Label(self.master,text="Sign Up",width=300,height=80,font=('Harrington',50,'bold'),bg="light blue")
        self.lb1.place(x=20,y=0,height=80,width=300)
        self.lb1=Label(self.master,text="It's  free and always will be.",width=350,height=80,font=('French Script MT',25,'bold'),bg="light blue")
        self.lb1.place(x=15,y=80,height=40,width=350)

        self.lbNm=Label(self.master,text="Name",bg="light blue",font=('Rockwell',18))
        self.lbNm.place(x=20,y=150,height=30,width=100)
        self.txtNm=Entry(self.master,font=('Rockwell',10))
        self.txtNm.place(x=150,y=150,height=30,width=250)

        self.lbContact=Label(self.master,text="Contact",bg="light blue",font=('Rockwell',18))
        self.lbContact.place(x=20,y=200,height=30,width=100)
        self.txtContact=Entry(self.master,font=('Rockwell',10))
        self.txtContact.place(x=150,y=200,height=30,width=250)

        self.lbAddress=Label(self.master,text="Address",bg="light blue",font=('Rockwell',18))
        self.lbAddress.place(x=20,y=250,height=30,width=100)
        self.txtAddress=Entry(self.master,font=('Rockwell',10))
        self.txtAddress.place(x=150,y=250,height=30,width=250)

        self.lbEmailId=Label(self.master,text="Email Id",bg="light blue",font=('Rockwell',18))
        self.lbEmailId.place(x=20,y=300,height=30,width=100)
        self.txtEmailId=Entry(self.master,font=('Rockwell',10))
        self.txtEmailId.place(x=150,y=300,height=30,width=250)

        self.lbUserId=Label(self.master,text="User Id",bg="light blue",font=('Rockwell',18),textvariable=self.UserId)
        self.lbUserId.place(x=20,y=350,height=30,width=100)
        self.txtUserId=Entry(self.master,font=('Rockwell',10))
        self.txtUserId.place(x=150,y=350,height=30,width=250)

        self.lbPassword=Label(self.master,text="Password",bg="light blue",font=('Rockwell',18))
        self.lbPassword.place(x=15,y=400,height=30,width=120)
        self.txtPassword=Entry(self.master,font=('Rockwell',10),show='*')
        self.txtPassword.place(x=150,y=400,height=30,width=250)

        self.btn_sign_up=Button(self.master,text="Sign Up",bg="green",font=('Comic Sans MS',25),fg="white",command=self.sign_up)
        self.btn_sign_up.place(x=15,y=500,height=60,width=150)

        self.master.mainloop()
    def sign_up(self):
        Name=self.txtNm.get()
        Contact=self.txtContact.get()
        Address=self.txtAddress.get()
        EmailId=self.txtEmailId.get()
        uid=self.txtUserId.get()
        Password=self.txtPassword.get()
        flag=dbmswork.chk_uid(uid)
        if flag:
            tkinter.messagebox.askyesno("Error","It seems this ID is already been used up.Try again !")
            self.UserId.set("")
            self.txtUserId.focus()
        else:
            flg=dbmswork.create_new_acc(uid,Password,Contact,Address,EmailId,Name)
            if flg:
                exit()