from tkinter import*
import tkinter.messagebox
import time

class signup:

    L={"Zubair Naseer":"zubair123","Hamza Khan":"M.123"}

    Balance={'Zubair':'50000','Zubair Naseer':'150000'}    
    
    def save(self):

        self.saving1 = str(self.entrySpace1.get())
        self.saving2 = str(self.entrySpace2.get())
        self.saving3 = str(self.entrySpace3.get())
        
        ObjectK.L[self.saving1] = self.saving2

        ObjectK.Balance[self.saving1] = self.saving3

        tkinter.messagebox.showinfo("","Account Has been Created Successfully")

        self.window1.destroy()

    def signupfun(self):
    
        self.window1=Tk()
        self.window1.title("SignUp")

        label=Label(self.window1,text="Name:")
        label.grid(row=0,column=0)

        label2=Label(self.window1,text="Password:")
        label2.grid(row=2,column=0)

        label2=Label(self.window1,text="Balance:")
        label2.grid(row=3,column=0)

        self.entrySpace1=Entry(self.window1)
        self.entrySpace1.bind(ObjectK.save)
        self.entrySpace1.grid(row=0,column=1)

        self.entrySpace2=Entry(self.window1, show = "*")
        self.entrySpace2.bind(ObjectK.save)
        self.entrySpace2.grid(row=2,column=1)

        self.entrySpace3=Entry(self.window1)
        self.entrySpace3.bind(ObjectK.save)
        self.entrySpace3.grid(row=3,column=1)

        button2=Button(self.window1,text="Create Account",fg="Black",command=ObjectK.save)
        button2.grid(row=6,columnspan=2)

        button4=Checkbutton(self.window1,text="Show Password",fg="Black")
        button4.grid(row=5,columnspan=2)

        self.window1.mainloop()

ObjectK=signup()


class FirstClass:

    name="None"

    def verify(self):

        self.name=str(entrySpace.get())
        self.password=str(entrySpace2.get())
        
        if self.name in ObjectK.L :
            if ObjectK.L[self.name]==self.password:
                tkinter.messagebox.showinfo("","Account Opened")
                Object1.name=self.name
                Object2.account()
            else:
                tkinter.messagebox.showinfo("","Password is incorrect")
        else:
            tkinter.messagebox.showinfo("","User name is wrong OR You don't have account")

Object1=FirstClass()

class Account:

    def account(self):

        window.destroy()

        self.window2 = Tk()
        self.window2.geometry('400x400+0+0')
        self.window2.title('Hello Bank')

        frame = Frame(self.window2,bg="light green")
        frame.pack(fill=BOTH)

        toplabel2=Label(frame,font=('calibri',18), bg='light green',fg="Black")
        toplabel2.pack()

        def ti():
            global time1
            time2=time.strftime('%I:%M:%S%p')
            date=time.strftime('%d-%B-%y')
            toplabel2.config(text=('Time:',time2,',Date:',date))
            toplabel2.after(200,ti)

        ti()

        toplabel=Label(frame,text="Welcome to Hello Bank",font=('calibri',30 , 'bold italic underline'), bg='light green',fg="Black")
        toplabel.pack()

        toplabel1=Label(frame,text=Object1.name,font=('calibri',20), bg='light green',fg="Black")

        toplabel1.pack()

        toplabel4=Label(frame,text="Choose Your Account ",font=('calibri',30,'bold italic underline'), bg='light green',fg="Black")
        toplabel4.pack()

        button1=Button(frame, font=('arial', 20, ' roman'), bd=10, text='CURRENT ACCOUNT', pady=3, padx=111,command=Object3.CA)
        button1.pack()

        button2=Button(frame, font=('arial', 20, ' roman'), bd=10, text='SAVING ACCOUNT', pady=3, padx=111,command=Object5.profit)
        button2.pack()

        button3=Button(frame, font=('arial', 20, ' roman'), text='SIGN OUT',bg='Blue',command=self.window2.destroy)
        button3.pack()

        self.window2.mainloop()

Object2=Account()

class CurrentAccount:

    with_draw_limit=25000
    amount=0
    balance=0
    
    def process(self):

        self.amount=eval(self.input1.get())

        Object3.amount=self.amount

        self.root.destroy()

        if Object3.amount>Object3.with_draw_limit:
            tkinter.messagebox.showinfo("",'Transaction cannot be proceeded.Limit for with draw is 25000.')
        else:
            if Object3.amount>Object3.balance:
                tkinter.messagebox.showinfo('','Transaction cannot be proceeded. You dont have sufficient balance.')
            else:
                Object3.balance=Object3.balance-Object3.amount
                ObjectK.Balance[Object1.name]=Object3.balance
                Object4.trnsctn()
                
    def destroy(self):

        self.root.destroy()
    
    def CA(self):

        Object3.balance=int(ObjectK.Balance[Object1.name])
        
        self.root=Tk()
        self.root.geometry("350x430")
        self.root.title("Current Account")

        frame=Frame(self.root,bg='light blue')
        frame.pack(fill=BOTH)

        label=Label(frame,font=('calibri',15 ), bg='Black',fg="White")
        label.pack()
        
        def ti():
            global time1
            time2=time.strftime('%I:%M:%S%p')
            date=time.strftime('%d-%B-%y')
            label.config(text=('Time:',time2,',Date:',date))
            label.after(200,ti)

        ti()

        label1=Label(frame,text="Current Account",font=('calibri',30 , 'bold italic underline'), bg='light blue',fg="Yellow")
        label1.pack()

        label2=Label(frame,text=Object1.name,font=('calibri',30 , 'bold italic'), bg='light blue',fg="Green")
        label2.pack()

        label3=Label(frame,text="Your Current Balance is:",font=('calibri',20 , 'bold italic'), bg='light blue',fg="Black")
        label3.pack()

        label4=Label(frame,text=Object3.balance,font=('calibri',20 , 'bold italic underline'), bg='light blue',fg="Black")
        label4.pack()

        label5=Label(frame,text="How much amount you \nwant to withdraw?",font=('calibri',20 , 'bold italic '), bg='light blue',fg="Black")
        label5.pack()

        self.input1=Entry(frame,width=20)
        self.input1.bind(Object3.process)
        self.input1.pack(ipady=10)

        button1 = Button(frame, text='Process',command=Object3.process, font=('arial', 23, 'roman'), bd=6)
        button1.pack()

        button2 = Button(frame, font=('arial', 23, 'roman'), text='Back',command=Object3.destroy, padx=22, pady=8, bg='light green')
        button2.pack(side="bottom", fill=X)

        self.root.mainloop()

Object3=CurrentAccount()

class transaction:

    def trnsctn(self):

        self.root2=Tk()
        self.root2.geometry('220x20')
        self.root2.title('Process')

        label=Label(self.root2,text="Your transaction is in process...",font=20,bg="black",fg="White")
        label.pack()

        Object4.aftertrnsctn()
        
        self.root2.mainloop()
        
    def aftertrnsctn(self):
        
        self.root2.destroy()

        tkinter.messagebox.showinfo("","Transaction Successfully")
        
        time.sleep(2)
        
        self.root3=Tk()
        self.root3.title('Hello Bank')
        self.root3.geometry('300x272')

        frame1=Frame(self.root3,bg='green')
        frame1.pack(fill=BOTH)

        labelL=Label(frame1,text='Hello Bank',font=('calibri',30),fg='Black')
        labelL.grid(row=0,columnspan=5)

        labelS=Label(frame1,text='',bg='green',font=('calibri',9),fg='White')
        labelS.grid(row=1,columnspan=2)

        label=Label(frame1,text=' Your balance after transaction is:',bg='green',font=('calibri',15),fg='White')
        label.grid(row=2,columnspan=4)

        label1=Label(frame1,text=Object3.balance,font=('calibri',20),bg='green',fg='White')
        label1.grid(row=3,columnspan=4)

        label=Label(frame1,text='\nDo you want to conitnue\ntransaction is:',bg='green',font=('calibri',15),fg='White')
        label.grid(row=4,columnspan=15)

        button1 = Button(frame1, text='YES', font=('arial', 13, 'roman'), bd=8,command=Object4.Continue)
        button1.grid(row=5,column=1)

        button2 = Button(frame1, text='NO', font=('arial', 14, 'roman'), bd=8,command=self.root3.destroy)
        button2.grid(row=5,column=3)

        self.root3.mainloop()

    def Continue(self):

        self.root3.destroy()

        Object3.CA()

Object4=transaction()

class SavingAccount:

    sbalance=0
    ProfitAmount=0
    
    def profit(self):

        if Object3.balance==0:
            Object5.sbalance=int(ObjectK.Balance[Object1.name])
        else:
            Object5.sbalance=Object3.balance
        
        self.profit = Object5.sbalance * 0.05
        self.ProfitAmount = Object5.sbalance + self.profit

        Object5.ProfitAmount=self.ProfitAmount

        Object5.SA()
        
    def SA(self):

        self.root4=Tk()
        self.root4.title('Hello Bank')
        self.root4.geometry('240x280')

        frame1=Frame(self.root4,bg='green')
        frame1.pack(fill=BOTH)

        labelL=Label(frame1,text='Hello Bank',font=('calibri',30),fg='Black')
        labelL.grid(row=0,column=1)

        labelS=Label(frame1,text='',bg='green',font=('calibri',9),fg='White')
        labelS.grid(row=1,column=2)

        label=Label(frame1,text=' Your current balance is:',bg='green',font=('calibri',15),fg='White')
        label.grid(row=2,columnspan=2)

        label1=Label(frame1,text=Object5.sbalance,font=('calibri',20),bg='green',fg='White')
        label1.grid(row=3,columnspan=10)

        label2=Label(frame1,text=' Your balance after month\nwith profit will be:',bg='green',font=('calibri',15),fg='White')
        label2.grid(row=4,columnspan=2)

        label3=Label(frame1,text=Object5.ProfitAmount,font=('calibri',20),bg='green',fg='White')
        label3.grid(row=5,columnspan=4)

        bttn1=Button(frame1,text="EXIT", font=('arial', 14, 'roman'), bd=8,command=self.root4.destroy)        
        bttn1.grid(row=6,columnspan=4)
        self.root4.mainloop()

Object5=SavingAccount()
window=Tk()
window.title("LogIn")

label=Label(window,text="Name:")
label.grid(row=0,column=0)

label2=Label(window,text="Password:")
label2.grid(row=2,column=0)

entrySpace=Entry(window)
entrySpace.bind(Object1.verify)
entrySpace.grid(row=0,column=1)

entrySpace2=Entry(window, show = "*")
entrySpace2.bind(Object1.verify)
entrySpace2.grid(row=2,column=1)

button1=Button(window,text="LogIN",fg="Black",command=Object1.verify)
button1.grid(row=5,column=1)

button2=Button(window,text="SignUp",fg="Black",command=ObjectK.signupfun)
button2.grid(row=5,column=0)

button3=Checkbutton(window,text="Remember Password",fg="Black")
button3.grid(row=4,columnspan=4)

button4=Checkbutton(window,text="Show Password",fg="Black")
button4.grid(row=3,columnspan=2)

window.mainloop()
