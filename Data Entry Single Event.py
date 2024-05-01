import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3



#Button Functions
def enter_data():
    #Name Info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    

    if firstname and lastname:
        gender = gender_box.get()
        fiftyfree = fifty_free_entry.get()

        print("First Name: ", firstname, "Last Name: ", lastname) 
        print("Gender: ", gender, "50Free: ", fiftyfree)
            
        conn = sqlite3.connect('data.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
            (firstname TEXT, lastname TEXT, gender TEXT, fiftyfree INT)
        '''




        conn.close()




    else:
        tkinter.messagebox.showwarning(title="Error", message="First Name and Last Name are Required Fields")

    








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

#Padding for Event Widgets
for widget in event_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

#Entry Button
button = tkinter.Button(frame, text= "Submit Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)




#Loop for Operation
window.mainloop() 