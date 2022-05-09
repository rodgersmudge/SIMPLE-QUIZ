ffrom tkinter import *
from tkinter import ttk
y=0
a=ttk.Notebook()#helps to organise multiple tabs effectively
frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)

window=ttk.Frame(a)
def quiz(y):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="completed")
    Label(frame1,text="Which city is called as Pink city?", font=("Arial",30,"bold")).grid(row=2,column=1)
    Button(frame1, text="hyderabad", font=("Arial",15,"bold"), bg="white", fg="red", command=a1_wrong).grid(row=3,column=2)
    Button(frame1, text="jaipur", font=("Arial", 15, "bold"), bg="white", fg="pink", command=a1_correct).grid(row=4, column=2)
    Button(frame1, text="delhi", font=("Arial", 15, "bold"), bg="white", fg="blue", command=a1_wrong).grid(row=5, column=2)

    Label(frame2, text="Between which countries is ashes played?", font=("Arial",30,"bold")).grid(row=2,column=1)
    Button(frame2, text="india vs pakistan", font=("Arial", 15, "bold"), bg="white", fg="blue", command=a2_wrong).grid(row=3, column=2)
    Button(frame2, text="australia vs england", font=("Arial", 15, "bold"), bg="white", fg="red", command=a2_correct).grid(row=4, column=2)
    Button(frame2, text="inida vs australia", font=("Arial", 15, "bold"), bg="white", fg="yellow", command=a2_wrong).grid(row=5, column=2)

    Label(frame3, text="what is CGI?", font=("Arial",30,"bold")).grid(row=2,column=1)
    Button(frame3, text="common goods interface", font=("Arial", 15, "bold"), bg="white", fg="red", command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text=" common gateway interface", font=("Arial", 15, "bold"), bg="white" , fg="brown", command=a3_correct).grid(row=4,column=2)
    Button(frame3, text="common gateway interrupt", font=("Arial", 15, "bold"), bg="white", fg="blue", command=a3_wrong).grid(row=5, column=2)

    Label(frame4, text="what is <tr> attribute?", font=("Arial", 30, "bold")).grid(row=2, column=1)
    Button(frame4, text="title read", font=("Arial", 15, "bold"), bg="white", fg="red", command=a4_wrong).grid(row=3, column=2)
    Button(frame4, text="table row", font=("Arial", 15, "bold"), bg="white", fg="brown", command=a4_correct).grid(row=4, column=2)
    Button(frame4, text="table read", font=("Arial", 15, "bold"), bg="white", fg="blue", command=a4_wrong).grid(row=5, column=2)

    Label(frame5,text="CONGRATULATIONS!!"
                                        "YOU COMPLETED YOUR QUIZ", font=("italics",30, "bold")).grid(row=4,column=4)

def a1_correct():
    Label(frame1, text="correct", font=("Arial",20,"bold"), bg="black", fg="white").grid(row=1,column=6)
    Label(frame1, text="marks obtained: 1", font=("Arial",15,"bold"), bg="black", fg="white").grid(row=1,column=6)
def a1_wrong():
    Label(frame1, text="incorrect", font=("Arial",20 , "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame1, text="marks obtained: 0", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)


def a2_correct():
    Label(frame2, text="correct", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame2, text="marks obtained: 1", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)
def a2_wrong():
    Label(frame2, text="incorrect", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame2, text="marks obtained: 0", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)

def a3_correct():
    Label(frame3, text="correct", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame3, text="marks obtained: 1", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)
def a3_wrong():
    Label(frame3, text="incorrect", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame3, text="marks obtained: 0", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)


def a4_correct():
    Label(frame4, text="correct", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame4, text="marks obtained: 1", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)
def a4_wrong():
    Label(frame4, text="incorrect", font=("Arial", 20, "bold"), bg="black", fg="white").grid(row=1, column=6)
    Label(frame4, text="marks obtained: 0", font=("Arial", 15, "bold"), bg="black", fg="white").grid(row=1, column=6)


quiz(y)
a.pack()
a.mainloop()