from tkinter import *
from tkinter import messagebox
import sqlite3

bgcolour="#a2e1ff"
password="123456"
root=Tk()
root.title("SkyBus")
root.configure(background="#a2e1ff")
bus_icon=PhotoImage(file="icon.png")
root.iconphoto(True, bus_icon)

#info_popup
def info_popup():
    info=messagebox.showinfo("Project 1","APL & DBMS Project\nSubmitted to-\nDr. Mahesh Kumar\nDr. Nileshkumar Patel\nDr. Amit Kumar Srivatava\n\nSubmitted by-191B134                          ")

#Home frame
frame_home=Frame(root,bg="#a2e1ff",bd = 0)
frame_home.grid(row=0,column=0)

frame_admin=Frame(root,bd = 0)

frame_traveller=Frame(root,bd = 0)

frame_result=Frame(root,bd = 0)

#Admin frame--------------------------------------------------------------------
def open_admin_frame():

    frame_admin.grid_forget()
    frame_traveller.grid_forget()
    frame_result.grid_forget()
    frame_admin.grid(row=1,column=0,sticky="nesw")

    #Labels,Entries,Drop-Downs...
    label0=Label(frame_admin,text=  "---Enter Details---------------------------------")
    label1=Label(frame_admin,text="Bus Type",           anchor='w')
    label2=Label(frame_admin,text="From",               anchor='w')
    label3=Label(frame_admin,text="To",                 anchor='w')
    label4=Label(frame_admin,text="Seats",              anchor='w')
    label8=Label(frame_admin,text="Date(DD-MM-YY)",     anchor='w')
    label5=Label(frame_admin,text="Dept. Time(HHMM)",   anchor='w')
    label6=Label(frame_admin,text="Arr. Time(HHMM)",    anchor='w')
    label7=Label(frame_admin,text="Fare",               anchor='w')



    label0.grid(row=0,column=0,columnspan=3,sticky="nesw")
    label1.grid(row=1,column=0,columnspan=1,sticky="nesw")
    label2.grid(row=2,column=0,columnspan=1,sticky="nesw")
    label3.grid(row=3,column=0,columnspan=1,sticky="nesw")
    label4.grid(row=4,column=0,columnspan=1,sticky="nesw")
    label5.grid(row=5,column=0,columnspan=1,sticky="nesw")
    label6.grid(row=6,column=0,columnspan=1,sticky="nesw")
    label7.grid(row=7,column=0,columnspan=1,sticky="nesw")
    label8.grid(row=8,column=0,columnspan=1,sticky="nesw")

    o1=StringVar()  #Bus Type
    o2=StringVar()  #From
    o3=StringVar()  #To
    o4=StringVar()  #Seats

    choice1=[
                "AC",
                "AC-Sleeper",
                "Wind",
                "Wind-Sleeper",
                "Himachal Air"
            ]

    choice2=[
                "Ujjain",
                "Guna",
                "Indore",
                "Ratlam",
                "Bhopal"
            ]

    choice3=[
                "Ujjain",
                "Guna",
                "Indore",
                "Ratlam",
                "Bhopal"
            ]

    choice4=[
                "MINI(16)",
                "STANDARD(32)",
                "SLEEPER(20)",
                "BIGBUS(56)"
            ]


    drop1=OptionMenu(frame_admin,o1,*choice1)
    drop2=OptionMenu(frame_admin,o2,*choice2)
    drop3=OptionMenu(frame_admin,o3,*choice3)
    drop4=OptionMenu(frame_admin,o4,*choice4)

    drop1.grid(row=1,column=1,columnspan=2,sticky="nesw")
    drop2.grid(row=2,column=1,columnspan=2,sticky="nesw")
    drop3.grid(row=3,column=1,columnspan=2,sticky="nesw")
    drop4.grid(row=4,column=1,columnspan=2,sticky="nesw")


    e1=Entry(frame_admin)
    e2=Entry(frame_admin)
    e3=Entry(frame_admin)
    e4=Entry(frame_admin)

    e1.grid(row=5,column=1,columnspan=2,sticky="nesw")
    e2.grid(row=6,column=1,columnspan=2,sticky="nesw")
    e3.grid(row=7,column=1,columnspan=2,sticky="nesw")
    e4.grid(row=8,column=1,columnspan=2,sticky="nesw")

    def submit_entry(): #Submission---Submission---Submission---Submission---Submission---Submission---Submission---Submission---Submission---Submission---Submission---

        bus_type=o1.get()
        source=o2.get()
        dest=o3.get()
        seats=o4.get()
        dept_time=e1.get()
        arr_time=e2.get()
        fare=e3.get()
        date=e4.get()

        #blank field error---blank field error---blank field error---
        c1=len(bus_type)
        c2=len(source)
        c3=len(dest)
        c4=len(seats)
        c5=len(dept_time)
        c6=len(arr_time)
        c7=len(fare)
        c8=len(date)
        checklen=c1+c2+c3+c4+c5+c6+c7+c8
        if(checklen>=35):

            insert_data=(bus_type,source,dest,seats,dept_time,arr_time,fare,date)
            insert_query="INSERT INTO buslist values(?,?,?,?,?,?,?,?)"

            conn=sqlite3.connect("database.db")
            conn.execute(insert_query,insert_data)
            conn.commit()
            conn.close()

            status_info=messagebox.showinfo("Database Alert.","Record Saved")

            open_admin_frame()
        else:
            status_info=messagebox.showwarning("Alert.","Fill All Details")

    button_submit=Button(frame_admin,text="Submit",command=submit_entry)
    button_submit.grid(row=9,column=1,columnspan=2,sticky="nesw")

#Traveller frame---Traveller frame---Traveller frame---Traveller frame---Traveller frame---Traveller frame---Traveller frame---Traveller frame---Traveller frame---
def open_traveller_frame():

    frame_admin.grid_forget()
    frame_traveller.grid_forget()
    frame_result.grid_forget()
    frame_traveller.grid(row=1,column=0,sticky="nesw")

    #Labels,Entries,Drop-Downs...
    label0=Label(frame_traveller,text="---Search Buses--------------------------------")

    label2=Label(frame_traveller,text="From",            anchor='w')
    label3=Label(frame_traveller,text="To",              anchor='w')
    label8=Label(frame_traveller,text="Date(DD-MM-YY)",  anchor='w')

    label0.grid(row=0,column=0,columnspan=3,sticky="nesw")
    label2.grid(row=1,column=0,columnspan=1,sticky="nesw")
    label3.grid(row=2,column=0,columnspan=1,sticky="nesw")
    label8.grid(row=3,column=0,columnspan=1,sticky="nesw")

    o2=StringVar()  #From
    o3=StringVar()  #To

    choice2=[
                "Ujjain",
                "Guna",
                "Indore",
                "Ratlam",
                "Bhopal"
            ]

    choice3=[
                "Ujjain",
                "Guna",
                "Indore",
                "Ratlam",
                "Bhopal"
            ]

    drop2=OptionMenu(frame_traveller,o2,*choice2)
    drop3=OptionMenu(frame_traveller,o3,*choice3)

    drop2.grid(row=1,column=1,columnspan=2,sticky="nesw")
    drop3.grid(row=2,column=1,columnspan=2,sticky="nesw")

    e1=Entry(frame_traveller)
    e1.grid(row=3,column=1,columnspan=2,sticky="nesw")

    #Search---Search---Search---Search---Search---Search---Search---Search---Search---Search---Search---Search---Search---
    def search():
        message=messagebox.showerror("Sorry","Sorry. Find buses doesn't work. The added records from Admin are saved in the database file. Bad time management and prioritisation.")

    button_find=Button(frame_traveller,text="Find Buses",command=search)
    button_find.grid(row=4,column=1,columnspan=2,sticky="nesw")

#------------------------------------------------------------------------------
#--------------------------------------------------------------------------
image_header=PhotoImage(file="JellyBusSquare.gif") #400x400
Label(frame_home,image=image_header,bd=0).grid(row=1,column=1,columnspan=5)

button_admin=Button(frame_home,text=    "Admin"    ,command=open_admin_frame)
button_traveller=Button(frame_home,text="Traveller",command=open_traveller_frame)
button_info=Button(frame_home,text=     "Info"     ,command=info_popup)
button_admin.grid(row=2,    column=1,columnspan=1,sticky="nesw")
button_traveller.grid(row=2,column=2,columnspan=3,sticky="nesw")
button_info.grid(row=2,     column=5,columnspan=1,sticky="nesw")

root.mainloop()
