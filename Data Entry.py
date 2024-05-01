import tkinter
from tkinter import ttk

#Button Functions
def enter_data():
    #Name Info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    gender = gender_box.get()
    fiftyfree = fifty_free_entry.get()

    print("First Name: ", firstname, "Last Name: ", lastname, "Gender: ", gender, "50Fr: ", fiftyfree)

#Root Window 
window = tkinter.Tk()
window.title("Data Entry Form")

#Frame within Window (make + pack)
frame = tkinter.Frame(window)
frame.pack()

#Frame within Frame within Window
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row= 0, column= 0, padx= 20, pady= 10)


#Name Info (full_name_label)
first_name_label = tkinter.Label(user_info_frame, text="First Name: ")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name: ")
last_name_label.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

#Competition Gender Info (gender_label, gender_box)
gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_box = ttk.Combobox(user_info_frame, values=["M", "F"])
gender_label.grid(row=0, column=2)
gender_box.grid(row=1, column=2) 


#Padding for Widgets
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

#Event Frame
event_frame = tkinter.LabelFrame(frame, text="Event Times")
event_frame.grid(row= 1, column=0, sticky="news", padx=20, pady=20)

#Event Frame Widgets
##Free
fifty_free = tkinter.Label(event_frame, text="50 Free: ")
fifty_free.grid(row=0,column=0)
fifty_free_entry = tkinter.Entry(event_frame)
fifty_free_entry.grid(row=1, column=0)
##100 Free
hundred_free = tkinter.Label(event_frame, text="100 Free: ")
hundred_free.grid(row=0,column=1)
hundred_free_entry = tkinter.Entry(event_frame)
hundred_free_entry.grid(row=1, column=1)
##200 Free
two_hundred_free = tkinter.Label(event_frame, text="200 Free: ")
two_hundred_free.grid(row=0,column=2)
two_hundred_free_entry = tkinter.Entry(event_frame)
two_hundred_free_entry.grid(row=1, column=2)

##Fly
fifty_fly = tkinter.Label(event_frame, text="50 Fly: ")
fifty_fly.grid(row=2,column=0)
fifty_fly_entry = tkinter.Entry(event_frame)
fifty_fly_entry.grid(row=3, column=0)
##100 Fly
hundred_fly = tkinter.Label(event_frame, text="100 Fly: ")
hundred_fly.grid(row=2,column=1)
hundred_fly_entry = tkinter.Entry(event_frame)
hundred_fly_entry.grid(row=3, column=1)
##200 Fly
two_hundred_fly = tkinter.Label(event_frame, text="200 Fly: ")
two_hundred_fly.grid(row=2,column=2)
two_hundred_fly_entry = tkinter.Entry(event_frame)
two_hundred_fly_entry.grid(row=3, column=2)

##Breast
fifty_br = tkinter.Label(event_frame, text="50 Breast: ")
fifty_br.grid(row=4,column=0)
fifty_br_entry = tkinter.Entry(event_frame)
fifty_br_entry.grid(row=5, column=0)
##100 BR
hundred_br = tkinter.Label(event_frame, text="100 Breast: ")
hundred_br.grid(row=4,column=1)
hundred_br_entry = tkinter.Entry(event_frame)
hundred_br_entry.grid(row=5, column=1)
##200 BR
two_hundred_br = tkinter.Label(event_frame, text="200 Breast: ")
two_hundred_br.grid(row=4,column=2)
two_hundred_br_entry = tkinter.Entry(event_frame)
two_hundred_br_entry.grid(row=5, column=2)

##Back
fifty_bk = tkinter.Label(event_frame, text="50 Back: ")
fifty_bk.grid(row=6,column=0)
fifty_bk_entry = tkinter.Entry(event_frame)
fifty_bk_entry.grid(row=7, column=0)
##100 BK
hundred_bk = tkinter.Label(event_frame, text="100 Back: ")
hundred_bk.grid(row=6,column=1)
hundred_bk_entry = tkinter.Entry(event_frame)
hundred_bk_entry.grid(row=7, column=1)
##200 BK
two_hundred_bk = tkinter.Label(event_frame, text="200 Back: ")
two_hundred_bk.grid(row=6,column=2)
two_hundred_bk_entry = tkinter.Entry(event_frame)
two_hundred_bk_entry.grid(row=7, column=2)

#IM
##100 IM
hundred_im = tkinter.Label(event_frame, text="100 IM: ")
hundred_im.grid(row=8,column=0)
hundred_im_entry = tkinter.Entry(event_frame)
hundred_im_entry.grid(row=9, column=0)
##200 IM
two_hundred_im = tkinter.Label(event_frame, text="200 IM: ")
two_hundred_im.grid(row=8,column=1)
two_hundred_im_entry = tkinter.Entry(event_frame)
two_hundred_im_entry.grid(row=9, column=1)
#400 IM
four_hundred_im = tkinter.Label(event_frame, text="400 IM: ")
four_hundred_im.grid(row=8,column=2)
four_hundred_im_entry = tkinter.Entry(event_frame)
four_hundred_im_entry.grid(row=9, column=2)

#Padding for Event Widgets
for widget in event_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

#Entry Button
button = tkinter.Button(frame, text= "Submit Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)




#Loop for Operation
window.mainloop()
