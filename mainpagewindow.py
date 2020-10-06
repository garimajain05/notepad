from tkinter import *
import dbmswork
from functools import partial
class NewWindow:
    def __init__(self,master,uid):
        self.uid=uid
        self.master=master
        self.master.geometry("1250x650")
        self.master.config(bg="purple")
        self.master.title("Welcome to the Main Page")
        
        info=dbmswork.customer_info(uid)
        self.contact=info[0][2]
        self.address=info[0][3]
        self.email=info[0][4]
        self.name=info[0][5]

        self.lbframe1=LabelFrame(self.master,bd=5,bg="purple")
        self.lbframe1.place(x=0,y=0,height=650,width=950)
        self.lbframe2=LabelFrame(self.master,bd=5,bg="aqua")
        self.lbframe2.place(x=950,y=0,height=650,width=300)

        self.lbl_nm=Label(self.lbframe1,bg="purple",fg="white",text="Welcome "+self.name+",",font=('Kristen ITC',25,'bold'))
        self.lbl_nm.place(x=5,y=35,width=350,height=30)

        txt_info=f'''User ID:{self.uid}
Contact:{self.contact}
Address:{self.address}
Email  :{self.email}'''

        self.lbl_personal_info=Label(self.lbframe1,bg="purple",fg="hotpink",text=txt_info,font=('Kristen ITC',15))
        self.lbl_personal_info.place(x=600,y=0,height=150,width=300)
        heading="Items\tCost per item\tQty\tCost"
        self.label_item=Label(self.lbframe1,bg="purple",fg="springgreen",text=heading,font=('Curlz MT',25,'bold'))
        self.label_item.place(x=0,y=150,height=45,width=900)
        
        self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        
        self.chkbox_pencils=Checkbutton(self.lbframe1,variable=self.c0,text="Pencils",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_pencils.place(x=55,y=210)
        self.chkbox_eraser=Checkbutton(self.lbframe1,variable=self.c1,text="Erasers",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_eraser.place(x=55,y=250)
        self.chkbox_sharpner=Checkbutton(self.lbframe1,variable=self.c2,text="Sharpners",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_sharpner.place(x=55,y=290)
        self.chkbox_pencilcolors=Checkbutton(self.lbframe1,variable=self.c3,text="Pencil Colours",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_pencilcolors.place(x=55,y=360)
        self.chkbox_gelpens=Checkbutton(self.lbframe1,variable=self.c4,text="Gel Pens",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_gelpens.place(x=55,y=410,height=20)
        self.chkbox_crayons=Checkbutton(self.lbframe1,variable=self.c5,text="Crayons",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_crayons.place(x=55,y=440,height=25)
        self.chkbox_notebooks=Checkbutton(self.lbframe1,variable=self.c6,text="Notebooks",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_notebooks.place(x=55,y=480,height=20)
        self.chkbox_watercolor=Checkbutton(self.lbframe1,variable=self.c7,text="Water Color",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_watercolor.place(x=55,y=520,height=20)
        self.chkbox_sketchpen=Checkbutton(self.lbframe1,variable=self.c8,text="Sketch Pens",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.chkbox_sketchpen.place(x=55,y=560,height=20)

        self.cost=Label(self.lbframe1,text="35\n5\n5\n\n250\n100\n350\n500\n550\n200",font=('Comic Sans MS',20),bg='purple',fg="coral")
        self.cost.place(x=350,y=210)
        
        self.txt_qty=[]
        for i in range(9):
            self.txt_qty.append(Entry(self.lbframe1,fg="grey",font=('Comic Sans MS',20,'bold')))
        self.txt_qty[0].place(x=575,y=210,width=50,height=30)
        self.txt_qty[1].place(x=575,y=250,width=50,height=30)
        self.txt_qty[2].place(x=575,y=290,width=50,height=30)
        self.txt_qty[3].place(x=575,y=360,width=50,height=30)
        self.txt_qty[4].place(x=575,y=410,width=50,height=30)
        self.txt_qty[5].place(x=575,y=445,width=50,height=30)
        self.txt_qty[6].place(x=575,y=480,width=50,height=30)
        self.txt_qty[7].place(x=575,y=520,width=50,height=30)
        self.txt_qty[8].place(x=575,y=560,width=50,height=30)

        self.btn_submit=Button(self.lbframe1,text="Submit",bg="limegreen",font=('Comic Sans MS',25),fg="white",command=self.submit)
        self.btn_submit.place(x=15,y=100,height=45,width=150)

        self.master.mainloop()
    def submit(self):
        cost0,cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8=0,0,0,0,0,0,0,0,0
        if self.c0.get()==1:
            qty0=self.txt_qty[0].get()
            if qty0=="":
                qty0=0
            else:
                qty0=int(qty0)
            cost0=(35*qty0)
            self.lbl0=Label(self.lbframe1,text=cost0,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl0.place(x=800,y=210)
        if self.c1.get()==1:
            qty1=self.txt_qty[1].get()
            if qty1=="":
                qty1=0
            else:
                qty1=int(qty1)
            cost1=(5*qty1)
            self.lbl1=Label(self.lbframe1,text=cost1,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl1.place(x=800,y=250)
        if self.c2.get()==1:
            qty2=self.txt_qty[2].get()
            if qty2=="":
                qty2=0
            else:
                qty2=int(qty2)
            cost2=(5*qty2)
            self.lbl2=Label(self.lbframe1,text=cost2,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl2.place(x=800,y=290)
        if self.c3.get()==1:
            qty3=self.txt_qty[3].get()
            if qty3=="":
                qty3=0
            else:
                qty3=int(qty3)
            cost3=(250*qty3)
            self.lbl3=Label(self.lbframe1,text=cost3,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl3.place(x=800,y=360)
        if self.c4.get()==1:
            qty4=self.txt_qty[4].get()
            if qty4=="":
                qty4=0
            else:
                qty4=int(qty4)
            cost4=(100*qty4)
            self.lbl4=Label(self.lbframe1,text=cost4,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl4.place(x=800,y=410)
        if self.c5.get()==1:
            qty5=self.txt_qty[5].get()
            if qty5=="":
                qty5=0
            else:
                qty5=int(qty5)
            cost5=(350*qty5)
            self.lbl5=Label(self.lbframe1,text=cost5,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl5.place(x=800,y=440)
        if self.c6.get()==1:
            qty6=self.txt_qty[6].get()
            if qty6=="":
                qty6=0
            else:
                qty6=int(qty6)
            cost6=(500*qty6)
            self.lbl6=Label(self.lbframe1,text=cost6,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl6.place(x=800,y=480)
        if self.c7.get()==1:
            qty7=self.txt_qty[7].get()
            if qty7=="":
                qty7=0
            else:
                qty7=int(qty7)
            cost7=(550*qty7)
            self.lbl7=Label(self.lbframe1,text=cost7,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl7.place(x=800,y=520)
        if self.c8.get()==1:
            qty8=self.txt_qty[8].get()
            if qty8=="":
                qty8=0
            else:
                qty8=int(qty8)
            cost8=(200*qty8)
            self.lbl8=Label(self.lbframe1,text=cost8,font=('Comic Sans MS',20),bg='purple',fg="coral")
            self.lbl8.place(x=800,y=560)
        total_cost=cost0+cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8
        txt_tc=f"Total Cost : {total_cost}\nPurchase Successfull..\nCome Soon To \nSHOP Again"
        self.lbl_total_cost=Label(self.lbframe2,text=txt_tc,font=('Comic Sans MS',20),bg='aqua',fg="purple")
        self.lbl_total_cost.place(x=0,y=0)
        
    