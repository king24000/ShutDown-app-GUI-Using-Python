from customtkinter import *
import os

# Shutdown logic
def restart():
    os.system("ShutDown /r /t 1")

def restart_time():
    os.system("ShutDown /r /t 20")

def logout():
    os.system("ShutDown -1")

def shutdown():
    os.system("ShutDown /s /t 1")

st = Tk()
st.title("Shutdown app")
st.geometry("500x600")
st.config(bg="red")

# Button for restart
r_button = Button(st, text="Restart", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=20, height=50, width=200)

# Button for restart with time
rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=130, height=50, width=200)

# Button for logout
lg_button = Button(st, text="Log Out", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=240, height=50, width=200)

# Button for shutdown
sd_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=shutdown)
sd_button.place(x=150, y=340, height=50, width=200)

st.mainloop()
