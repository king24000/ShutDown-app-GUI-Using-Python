from tkinter import *  #GUI module
import os

#shutdown logic
def restart():
    os.system("ShutDown /r /t 1")
def restart_time():
    os.system("ShutDown /r /t 20")
def logout():
    os.system("ShutDown -1")
def shutdown():
    os.system("ShutDown /s /t 1")
st = Tk()  #show the GUI
st.title("ShutDown app") # they are title in project
st.geometry("500x600")  #400 is height and 900 is width
st.config(bg="red")    #using for color

#button using restart
r_button = Button(st, text="Restart", font=("Time New Roman", 30 , "bold"),relief=RAISED, cursor="plus", command="restart")
r_button.place(x=150,y=20, height=50, width=200)
#button using restart Time
rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20 , "bold"),relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150,y=130, height=50, width=200)
#button using log out
lg_button = Button(st, text="Log Out", font=("Time New Roman", 20 , "bold"),relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150,y=240, height=50, width=200)
#button using ShutDown
sd_button = Button(st, text="ShutDown", font=("Time New Roman", 20 , "bold"),relief=RAISED, cursor="plus", command=shutdown)
sd_button.place(x=150,y=340, height=50, width=200)
st.mainloop()  #they are last part
